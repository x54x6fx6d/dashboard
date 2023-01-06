import psutil

def free():
	diskspace = str(psutil.disk_usage("/").free / (2**30))
	freespace = diskspace.split(".")
	return str(freespace[0])

def used():
	diskspace = str(psutil.disk_usage("/").used / (2**30))
	usedspace = diskspace.split(".")
	return str(usedspace[0])

def total():
	diskspace = str(psutil.disk_usage("/").total / (2**30))
	totalspace = diskspace.split(".")
	return str(totalspace[0])

def percent():
	diskspace = str(psutil.disk_usage("/").percent)
	return str(diskspace)