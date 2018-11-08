#!/bin/sh

who am i > users.txt;
python3 nameExtractor.py;
# Interval
sleep 1;
./run.sh

# nohup ./run.sh > numberOfUsers.txt &
