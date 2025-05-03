import docker
import time
from datetime import datetime, timedelta

client = docker.from_env()
containers_to_monitor = ["datahub", "webnode"]
start_time = datetime.now()

def check_status_and_restart():
    for container_name in containers_to_monitor:
        try:
            container = client.containers.get(container_name)
            if container.status != "running":
                print(f"[{datetime.now()}] {container_name} was not running. Restarting.")
                container.restart()
        except docker.errors.NotFound:
            print(f"[{datetime.now()}] {container_name} not found.")

def restart_daily_if_needed():
    global start_time
    now = datetime.now()
    if now - start_time >= timedelta(days=1):
        print(f"[{now}] Daily restart initiated.")
        for container_name in containers_to_monitor:
            try:
                client.containers.get(container_name).restart()
            except docker.errors.NotFound:
                print(f"[{now}] {container_name} missing during daily restart.")
        start_time = now

def scan_recent_logs():
    for container_name in containers_to_monitor:
        try:
            logs = client.containers.get(container_name).logs(tail=10).decode().lower()
            if "error" in logs or "warning" in logs:
                print(f"[{datetime.now()}] Issues in {container_name} logs:")
                print(logs)
        except docker.errors.NotFound:
            continue

if __name__ == "__main__":
    while True:
        check_status_and_restart()
        restart_daily_if_needed()
        scan_recent_logs()
        time.sleep(10)
