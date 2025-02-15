#!/usr/bin/env python
import sys

# This function print the three lines stored in the array prev
def print_ips(prev):
    for line in prev:
        # skip if the line is empty, in case of hours that have less than three different ip visits
        if line!="":
            print(line)

# stores the current hour 
cur_hour = None
# stores the last three lines we have visited
prev=["","",""]
for line in sys.stdin:
    line = line.strip()
    hour,count_ip  = tuple(line.split('-'))

    # shift the line by one since the incoming will definetly have more count
    if cur_hour==hour:
        prev[0]= prev[1]
        prev[1]= prev[2]
        prev[2]= line
    else:
        # if the line has new hour, print the previous three lines
        if cur_hour:
            print_ips(prev)
        # reset cur_hour and prev
        cur_hour = hour
        prev=["","",""]
        prev[2] = line

print_ips(prev)