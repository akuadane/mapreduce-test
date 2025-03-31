#!/usr/bin/env python
import sys
import json

# Load JSON file into a dictionary
with open('boundaries.json', 'r') as json_file:
    players_boundaries = json.load(json_file)


for line in sys.stdin:
    line = line.strip()
    
    
    key, value= line.split("\t")
    name,z,boundary = key.split('-')
    matrix, shot_result = value.split('-')

    sd,cd,sc = eval(matrix)

    boundaries = players_boundaries[name]
    boundary = boundaries[0]
    dist = float('inf')
    zone = 0

    for i,b in enumerate(boundaries):
        temp_dist = ((b[0]-sd)**2 + (b[1]-cd)**2 + (b[2]-sc)**2)**0.5
        if temp_dist<dist:
            dist = temp_dist
            boundary = b
            zone = i
    print("%s-%s-%s\t%s-%s"%(name,zone,boundary,(sd,cd,sc),shot_result))