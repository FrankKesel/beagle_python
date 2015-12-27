#!/usr/bin/python
# A program to program the LEDs
# Author: Frank Kesel
# Date: 6-12-2015

import sys
LED_PATH = "/sys/class/leds/beaglebone:green:"
LED0 = "usr0"
LED1 = "usr1"
LED2 = "usr2"
LED3 = "usr3"

#-------------------------------------------------------------------------------
# Write to the corresponding filename of the LED
#-------------------------------------------------------------------------------
def writeLED ( filename, value, nrPath ):
   path = LED_PATH + nrPath + filename
   fo = open( path,"w")
   fo.write(value)
   fo.close()
   return

#-------------------------------------------------------------------------------
# Remove trigger from LED
#-------------------------------------------------------------------------------
def removeTrigger( nrPath ):
   writeLED (filename="/trigger", value="none", nrPath = nrPath)
   return

def ledOn( nrPath ):
   removeTrigger(nrPath = nrPath)
   writeLED (filename="/brightness", value="1", nrPath = nrPath)
   return

def ledOff( nrPath ):
   removeTrigger(nrPath = nrPath)
   writeLED (filename="/brightness", value="0", nrPath = nrPath)
   return

def ledFlash( nrPath ):
   writeLED (filename="/trigger", value="timer", nrPath = nrPath)
   writeLED (filename="/delay_on", value="100", nrPath = nrPath)
   writeLED (filename="/delay_off", value="100", nrPath = nrPath)
   return

#-------------------------------------------------------------------------------
# Main
#-------------------------------------------------------------------------------
print "-----------------BeaglePython------------------------"
if len(sys.argv)!=3:
   print "There are an incorrect number of arguments"
   print "  usage is:  pythonLED.py LED command"
   print "  where command is one of on, off, flash or status."
   print "  and LED is the LED number (0-3)"
   print "-----------------------------------------------------"
   sys.exit(2)
ledNr = sys.argv[1]
mode = sys.argv[2]
if ledNr == '0':
   nrPath = LED0
elif ledNr == '1':
   nrPath = LED1
elif ledNr == '2':
   nrPath = LED2
elif ledNr == '3':
   nrPath = LED3
elif ledNr == 'all':
   print "All LEDs selected!"
else:
   print "ERROR: LED number should be 0-3 or all. Exiting ..."
   print "-----------------------------------------------------"
   sys.exit(2)

if mode=="on":
   print "Turning LED " + ledNr + " on"
   if ledNr == "all":
      ledOn( LED0)
      ledOn( LED1)
      ledOn( LED2)
      ledOn( LED3)
   else:
      ledOn( nrPath )
elif mode=="off":
   print "Turning LED " + ledNr + " off"
   if ledNr == "all":
      ledOff( LED0)
      ledOff( LED1)
      ledOff( LED2)
      ledOff( LED3)
   else:
      ledOff( nrPath )
elif mode=="flash":
   print "Flashing LED " + ledNr
   if ledNr == "all":
      ledFlash( LED0)
      ledFlash( LED1)
      ledFlash( LED2)
      ledFlash( LED3)
   else:
      ledFlash( nrPath )
elif mode=="status":
   if ledNr == "all":
      print "ERROR: Status only for a single LED. Exiting ..."
      print "-----------------------------------------------------"
      sys.exit(2)
   else:
      print "Getting the LED trigger status for LED " + ledNr
      fo = open( LED_PATH + nrPath + "/trigger", "r")
      print fo.read()
      fo.close()
else:
   print "ERROR: Invalid Command. Exiting ..."
print "-----------------------------------------------------"
