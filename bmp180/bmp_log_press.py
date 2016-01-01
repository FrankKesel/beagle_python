#!/usr/bin/python
# -*- coding: UTF-8 -*-

#--------------------------------------------------------------------
#File: 	bmp_logger.py
#Author: F.Kesel
#Date: 	29.12.2015
#Purpose:Read the values from the BMP180 sensor and 
#			store pressure in log-file
#--------------------------------------------------------------------

import os, time, sys
sys.path.append('/home/frank/python/lib/')
import bmp_util #Local module with utilities


#Read BMP180 sensor data, bmpVal[0]: temperature, bmpVal[1] pressure
bmpVal = bmp_util.readBMP180()


#Append data to pressure log-file
with open(bmp_util.logPress, "a") as outfile:
	line = bmp_util.day + " " + bmpVal[1] + "\n"
	outfile.write(line)

