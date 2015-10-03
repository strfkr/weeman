#
# misc.py - usefull functions
#
# This file if part of weeman project
#
# See 'LICENSE' file for copying 
#


import sys
import time

# help options
help_options = {"url" : "The URL of the webpage, with https:// or http://.",
                "action_url" : "The form action URL of the webpage.",
                "port" : "The port weeman will listen",
                "user_agent" : "Weeman User-Agent string."}

def printt(s, msg):
    if s == 1:
        print("\033[01;31m[%s] Error: %s\033[00m" %(time.strftime("%H:%M:%S"),msg))
        sys.exit(1)
    elif s == 2:
        print("\033[01;32m[%s] %s\033[00m" %(time.strftime("%H:%M:%S"),msg))
    elif s == 3: 
        print("\033[01;01m[%s] %s\033[00m" %(time.strftime("%H:%M:%S"),msg))
    else:
        print("\033[01;01m[%s] %s\033[00m" %(time.strftime("%H:%M:%S"),msg))

def print_help():
    print("\t\033[01;32mshow   : show default settings.")
    print("\tset    : set settings (set port 80).")
    print("\trun    : start the server.")
    print("\tclear  : clear screen.")
    print("\thelp   : show help.")
    print("\tquit   : bye bye.\033[00m")

def print_help_option(option):
    found = 0

    for opt in help_options.items():
        if opt[0] == option:
            found = 1
            printt(32, "%s - %s" %(option, opt[1]))
    if not found:
        printt(3, "Error: option \'%s\' not found." %option)

def isroot():
    if os.getuid() !=0:
        printt(1,"Please run weeman as root.")


