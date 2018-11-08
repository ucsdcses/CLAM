#!/bin/sh
# gets rid of the first heading
w | awk 'NR>=2' > users.txt;
python3 nameExtractor.py;
# Interval
sleep 1;
./run.sh

# nohup ./run.sh > numberOfUsers.txt &
