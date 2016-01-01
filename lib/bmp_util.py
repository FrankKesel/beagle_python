#--------------------------------------------------------------------
#File: 	bmp_util.py
#Author: F.Kesel
#Date: 	29.12.2015
#Purpose:Functions for the BMP180 sensor 
#--------------------------------------------------------------------

import os, time, sys
import re
import subprocess

dateTime = time.localtime() #Get time and date
day = time.strftime("%d.%m", dateTime)
month = time.strftime("%m.%y", dateTime)
hour = time.strftime("%H:%M", dateTime)
date = time.strftime("%d.%m.%Y", dateTime)

#logfiles
logTemp = "/home/frank/python/bmp180/logs/temp" + day 
logPress = "/home/frank/python/bmp180/logs/press" + month 

#Read temperature and pressure from BMP180 sensor
#return: list with 2 strings: [0]: temperature, [1]: pressure (sea level)
def readBMP180():
	values = ["", ""]
	#Start bmp180 program
	output = subprocess.Popen(["/home/frank/bin/bmp180"], stdout=subprocess.PIPE)
	#Read values from stdout of bmp180
	valueString = output.stdout.read()
	#Find the numbers in stdout (must be temperature and pressure)
	numbers = re.findall(r"[-+]?\d*\.\d+|\d+", valueString)
	temperature = numbers[0]
	pressure = float(numbers[1])
	pSea = pressure * 1.058 #Calculate pressure at sea level
	values[0] = temperature
	values[1] = str("{:.2f}".format(pSea)) #2 digits after comma
	return values
