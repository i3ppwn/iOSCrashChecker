#!/usr/bin/python
'''
The name from the tool is iOSCrashChecker. Get a list with all crash from your iDevice. 
Copyright (C) 2013  Louis Kremer aka. @3x7R00Tripper

This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program; if not, see <http://www.gnu.org/licenses/>.
'''
import socket
import time
import os
import random
import sys
from os import *

host = "localhost" #Host to your iPhone(SSH)
clear = lambda: os.system('clear')

def devicename(ip_ad):
	getcommand = 'ssh -p 2222 root@'+ip_ad+' "uname -n"' #2222 SSH Port to your iPhone
	com = os.popen(getcommand)
	getcom = com.read()
	if getcom:
		clear()
		print getcom
		clear()
	else:
		clear()
		print " Unknown Error "
	com.close()
	return getcom

def checkforcrash(ip):
	springboard = '/private/var/mobile/Library/Logs/CrashReporter/LatestCrash.plist'
	commcenter = '/private/var/logs/CrashReporter/LatestCrash.plist'
	command = 'ssh -p 2222 root@'+ip+' "cat %s 2>/dev/null; cat %s 2>/dev/null"' % (commcenter, springboard)
	kernel = '/private/var/mobile/Library/Logs/panic.log'
	c = os.popen(command)
	crash = c.read()
	if crash:
		clear()
		print crash
		print "\n\n\n"
		clear()
	else:
		clear()
		print " ERROR: "
		print " The crash plist was cleaning  "
		print " You must wait for a new crash. "
		print " Later a new crash, your iDevice make a new crash plist "
	c.close()
	return crash

if __name__ == '__main__':
    readc = checkforcrash(host)
    readd = devicename(host)
    verz = 'devices/'+readd
    dir = os.path.dirname(verz)
    if not os.path.exists(verz):
    	mkdir(verz)
    datz = verz+'/'+'crash.plist'
    datzt = verz+'/'+'crash.txt'
    myfile = file(datz, 'w')
    myfile.write('')
    myfile.write(readc)
    myfile.close()
    f = file(datzt, 'w')
    f.write('')
    f.write(readc)
    f.close()
