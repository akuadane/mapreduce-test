#!/usr/bin/env python
import sys

for line in sys.stdin:
    line = line.strip()
    hour_ip, count = tuple(line.split('\t'))
    try:
        count = int(count)
        hour,ip = tuple(hour_ip.split(']'))
        hour+=']'

        # Making the key to be hour+count and also appending zeros to each count so that the sorting is done properly.
        print '%s\t%s'%(hour+"-"+"{:05d}".format(count),ip)
    except: 
        pass
