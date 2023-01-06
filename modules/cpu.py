import psutil

def cpu():
    return str(psutil.cpu_percent())

def width():
    a = str(psutil.cpu_percent()).split(".")
    return int(a[0])