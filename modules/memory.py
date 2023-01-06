import psutil

def memory():
    mem = str(psutil.virtual_memory().percent)

    return mem