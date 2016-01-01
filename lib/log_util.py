#--------------------------------------------------------------------
#File: 	log_util.py
#Author: F.Kesel
#Date: 	29.12.2015
#Purpose:Functions for log-file handling 
#--------------------------------------------------------------------



#Read data from log file "fileName"
#x: x-axis, y: y-axis
def readLogFile(fileName, x, y ):
	thefile = open(fileName, "r")
	while thefile:
		line = thefile.readline()
		if len(line) < 2:
			break
		elements = line.split()
		x.append(elements[0])
		y.append(elements[1])
	thefile.close()


