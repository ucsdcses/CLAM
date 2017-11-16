#!/usr/bin/env python
"""clam.py: Python script file to help check the lab computer status"""

import subprocess
import sys

#username we're going to use
USERNAME=""
#string literals to construct our final host name
START="@ieng6-"
END=".ucsd.edu"
#command we execute to check login status
COMMAND="users"
#dictionary to correspond computer to login status
STATUS=dict()

#use loop to access each computer on the system
for(compIndex=0;compIndex<;compIndex++)
    construct=USERNAME+START+compIndex+END
    #ssh step
    ssh=subprocess.Popen(["ssh","%s"% construct,COMMAND],
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
    #record some results
    response=ssh.stdout.readline()
    if response == USERNAME:
        STATUS[compIndex]=False
    else:
        STATUS[compIndex]=True

#put response into mongodb
