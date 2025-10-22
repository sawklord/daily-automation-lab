import platform, psutil, json

info = {
    "os": platform.system(),
    "release": platform.release(),
    "cpu": psutil.cpu_percent(interval=1),
    "memory": psutil.virtual_memory().percent
}

print(json.dumps(info, indent=2))
