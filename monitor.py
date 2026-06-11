import psutil
import datetime

def get_system_stats():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    return {
        "cpu_usage": cpu,
        "memory_used": memory.percent,
        "disk_used": disk.percent,  
    }

def log_stats(stats):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} - CPU: {stats['cpu_usage']}%, Memory: {stats['memory_used']}%, Disk: {stats['disk_used']}%\n"

    with open("system_stats.log", "a") as f:
        f.write(log_entry)

def check_alerts(stats):
    if stats['cpu_usage']>80:
        print("ALERT: High CPU usage!")
    if stats['memory_used']>80:
        print("ALERT: High Memory usage!")
    if stats['disk_used']>90:
        print("ALERT: High Disk usage!")

for i in range(5):
    stats = get_system_stats()
    log_stats(stats)
    check_alerts(stats)    