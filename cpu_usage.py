import psutil

def check_cpu_usage(percent):
    usage = psutil.cpu_percent()
    return usage < percent
if not check_cpu_usage(75):
    print("CPU is overloaded")
else:
    print("Everything ok")
check_cpu_usage(70)
