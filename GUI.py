'''
The name from the tool is iOSCrashChecker. Get a list with all crash from your iDevice. 
Copyright (C) 2013  Louis Kremer aka. @3x7R00Tripper

This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program; if not, see <http://www.gnu.org/licenses/>.
'''

#!/usr/bin/python
import Tkinter 
import tkMessageBox
from Tkinter import * 
import os
import sys

root = Tk()
root.minsize(450,100) 
root.geometry("400x100")
root.title("iOSCrashChecker") 

def spy():
   cmd = 'python check.py'
   os.system(cmd)
   os.system('clear')
   os.system('exit')
   sys.exit()

L = Label(root, text="All Crashes: /devices/YourDeviceName/crash.txt Last crash: crash.plist \n", font=("Helvetica", 13))

z = Label(root, text="\n ", font=("Helvetica", 1)) 

B = Tkinter.Button(root, text ="Get Crashes", command=spy, width=30) 

z.pack()
L.pack()
B.pack() 
root.mainloop()
