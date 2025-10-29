import psutil
import datetime
def get_battery_status():
    """Get battery percentage"""
    battery = psutil.sensors_battery()
    
    if battery is None:
        return "Sir, this device doesn't have a battery (desktop PC)."
    
    percent = battery.percent
    plugged = battery.power_plugged
    
    if plugged:
        return f"Battery is at {percent}% and charging, Sir."
    else:
        return f"Battery is at {percent}%, Sir."

def get_cpu_usage():
    """Get CPU usage percentage"""
    cpu_percent = psutil.cpu_percent(interval=1)
    return f"CPU usage is at {cpu_percent}%, Sir."

def get_memory_usage():
    """Get RAM usage"""
    memory = psutil.virtual_memory()
    used_gb = memory.used / (1024**3)  # Convert bytes to GB
    total_gb = memory.total / (1024**3)
    percent = memory.percent
    
    return f"Memory usage: {used_gb:.1f} GB out of {total_gb:.1f} GB ({percent}%), Sir."    