#!/usr/bin/env python
import sys
import re

first_boundaries = [(6.0, 6.75, 3.0),(18.0, 20.25, 9.0), (30.0, 33.75, 15.0),(42.0, 47.25, 21.0)]

for line in sys.stdin:
    line = line.strip()
    
    
    fields = re.split(r',(?=(?:[^"]*"[^"]*")*[^"]*$)', line)
    name = fields[19]
    
    shot_dist = float(fields[11] if fields[11]!='' else 0)
    close_def_dist = float(fields[16] if fields[16]!='' else 0)
    shot_clock = float(fields[8] if fields[8]!='' else 0)
    
    shot_result  = 1 if fields[13]=='made' else 0

    boundary = first_boundaries[0]
    dist = float('inf')
    zone = 0

    for i,b in enumerate(first_boundaries):
        temp_dist = ((b[0]-shot_dist)**2 + (b[1]-close_def_dist)**2 + (b[2]-shot_clock)**2)**0.5
        if temp_dist<dist:
            dist = temp_dist
            boundary = b
            zone = i
    print("%s-%s-%s\t%s-%s"%(name,zone,boundary,(shot_dist,close_def_dist,shot_clock),shot_result))