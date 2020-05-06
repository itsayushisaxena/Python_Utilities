##This code checks whether the CPU is under too much load or not


import psutil
#psutil (python system and process utilities) is a cross-platform
#library for retrieving information on running processes and
#system utilization (CPU, memory, disks, network, sensors) in Python.

def check_cpu_usage(percent):
    #cpu_percent() return a float representing the current system-wide
    #CPU utilization as a percentage. 
    usage = psutil.cpu_percent(interval = 1)
    return usage < percent
if not check_cpu_usage(75):
    print("CPU is overloaded")
else:
    print("Everything ok")





# gives a single float value
print(psutil.cpu_percent())
# gives an object with many fields
print(psutil.virtual_memory())  #physical memory usage
# you can convert that object to a dictionary 
print(dict(psutil.virtual_memory()._asdict()))

print('memory % used:', psutil.virtual_memory()[2])
