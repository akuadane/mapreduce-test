#!/usr/bin/env python
import sys

for line in sys.stdin:
    line = line.strip()
    hour_ip, count = tuple(line.split('\t'))
    try:
        count = int(count)
        hour,ip = tuple(hour_ip.split(']'))
        hour+=']'

        print '%s\t%s'%(hour+"-"+"{:05d}".format(count),ip)
    except: 
        pass
