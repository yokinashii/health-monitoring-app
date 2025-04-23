import docker
import time

client = docker.from_env()
SERVICE_NAME = "health-monitoring-app-ai_service-1"
CPU_THRESHOLD = 70
SCALE_UP_SUFFIX = "_clone"
CHECK_INTERVAL = 10

def get_container_cpu_usage(container_name):
    container = client.containers.get(container_name)
    stats = container.stats(stream=False)
    cpu_delta = stats["cpu_stats"]["cpu_usage"]["total_usage"] - stats["precpu_stats"]["cpu_usage"]["total_usage"]
    system_delta = stats["cpu_stats"]["system_cpu_usage"] - stats["precpu_stats"]["system_cpu_usage"]
    if system_delta > 0.0:
        return (cpu_delta / system_delta) * len(stats["cpu_stats"]["cpu_usage"]["percpu_usage"]) * 100.0
    return 0.0


def scale_up(container_name):
    new_name = container_name + SCALE_UP_SUFFIX

    try:
        existing = client.containers.get(new_name)
        if existing.status != 'running':
            existing.start()
            print(f"▶️ Started stopped container: {new_name}")
        else:
            print(f"🚫 Clone already running: {new_name}")
        return
    except docker.errors.NotFound:
        pass

    original = client.containers.get(container_name)

    client.containers.run(
        original.image.tags[0],
        name=new_name,
        detach=True,
        environment=original.attrs["Config"]["Env"],
        network=original.attrs["HostConfig"]["NetworkMode"]
    )

    print(f"✅ Started clone: {new_name}")


while True:
    usage = get_container_cpu_usage(SERVICE_NAME)
    print(f"CPU usage: {usage:.2f}%")
    if usage > CPU_THRESHOLD:
        scale_up(SERVICE_NAME)
    time.sleep(CHECK_INTERVAL)
