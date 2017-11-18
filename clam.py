#!/usr/bin/env python
"""clam.py: Python script file to help check the lab computer status"""

import subprocess
import sys

#username we're going to use
USERNAME="cs15xie"
#string literals to construct our final host name
START="@its-cseb"
END=".ucsd.edu"
#integers to signify the starting computer
STARTLOC=1;
ENDLOC=50;
#command we execute to check login status
COMMAND="users"
#dictionary to correspond computer to login status
STATUS=dict()
labs=[220,230,240,250,260]
#use loop to access each computer on the system
for labIndex in labs:
    for compIndex in xrange(STARTLOC,ENDLOC):
        construct=USERNAME+START+str(labIndex)+"-"+str(compIndex)+END
        #ssh step
        ssh=subprocess.Popen(["ssh","%s"% construct,COMMAND],
                shell=False,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)
        #record some results
        response=ssh.stdout.readline()
        if response == USERNAME:
            STATUS[compIndex]=False
            print(str(labIndex)+"-"+str(compIndex))
        else:
            STATUS[compIndex]=True
        
#put response into mongodb
