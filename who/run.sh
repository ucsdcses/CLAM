#!/bin/sh

who > names.txt;
python3 nameExtractor.py;
# Interval
sleep 1;
./run.sh

# nohup ./run.sh > numberOfUsers.txt &
