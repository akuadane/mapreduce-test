#!/usr/bin/env python
import sys
import json
import json

# Load JSON file into a dictionary
with open('./q2/boundaries.json', 'r') as json_file:
    players_boundaries = json.load(json_file)

prev_key = None
total = zone = shot_clock = shot_dist = close_def_dist = 0
temp_boundaries = []

for line in sys.stdin:
    line = line.strip()
    
    key, value= line.split("\t")
    name,z,boundary = key.split('-')
    matrix,_ = value.split('-')
    z = int(z)
    sd,cd,sc = eval(matrix)

    print(line)
    if prev_key==None:
        temp_boundaries = players_boundaries[name]
        prev_key = name
        zone = z
    if prev_key==name:
        if zone==z:
            shot_clock += sc
            shot_dist +=sd
            close_def_dist +=cd
            total+=1
        else:
            new_shot_clock = round(shot_clock/total,3)
            new_shot_dist = round(shot_dist/total,3)
            new_close_def_dist = round(close_def_dist/total,3)

            temp_boundaries[zone] = (new_shot_dist,new_close_def_dist,new_shot_clock)

            zone = z
            shot_dist,close_def_dist,shot_clock = sd,cd,sc
            total = 1
    else:
        players_boundaries[prev_key] = temp_boundaries
        temp_boundaries = players_boundaries[name]

        zone = z
        shot_dist,close_def_dist,shot_clock = sd,cd,sc
        total = 1

if prev_key!=None:
    new_shot_clock = round(shot_clock/total,3)
    new_shot_dist = round(shot_dist/total,3)
    new_close_def_dist = round(close_def_dist/total,3)

    temp_boundaries[zone] = (new_shot_dist,new_close_def_dist,new_shot_clock)
    players_boundaries[prev_key] = temp_boundaries

# Save dictionary to a JSON file
with open('./q2/boundaries.json', 'w') as json_file:
    json.dump(players_boundaries, json_file, indent=4)
    
