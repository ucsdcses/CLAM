#!/usr/bin/env python

# clam.py: Python script file to help check the lab computer status

import subprocess
import sys

# username we're going to use
USERNAME="cs15xie"
# string literals to construct our final host name
START="@its-cseb"
END=".ucsd.edu"
# integers to signify the starting computer
# TODO Need to check these numbers
STARTLOC=1;
ENDLOC=50;
# command we execute to check login status
COMMAND="users"
# dictionary to correspond computer to login status
STATUS=dict()
labs=[230,240,250,260,270]

# use loop to access each computer on the system
for labIndex in labs:
    for compIndex in xrange(STARTLOC,ENDLOC):
        if (compIndex < 10): 
            compString = "0" + str(compIndex)
        else:
            compString = str(compIndex)
        construct = USERNAME+START+str(labIndex)+"-"+compString+END
        # ssh step
        ssh = subprocess.Popen(["ssh", "%s"% construct, COMMAND],
                shell = False,
                stdout = subprocess.PIPE,
                stderr = subprocess.PIPE)
        # record some results
        #response = ssh.stdout.readline()
        response = subprocess.check_output(COMMAND)
        print(response)
        if response == USERNAME:
            STATUS[compIndex] = False
            print(str(labIndex)+"-"+str(compIndex))
        else:
            print("response != cs15xie")
            STATUS[compIndex] = True
        
# put response into mongodb
