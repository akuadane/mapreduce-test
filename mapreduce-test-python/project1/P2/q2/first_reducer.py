#!/usr/bin/env python
import sys
import json

prev_key = None
players_boundaries = {}
total = zone = shot_clock = shot_dist = close_def_dist = 0
first_boundaries = [(6.0, 6.75, 3.0),(18.0, 20.25, 9.0), (30.0, 33.75, 15.0),(42.0, 47.25, 21.0)]
temp_boundaries = first_boundaries[:]

for line in sys.stdin:
    line = line.strip()
    
    key, value= line.split("\t")
    name,z,boundary = key.split('-')
    matrix,_ = value.split('-')
    z = int(z)
    sd,cd,sc = eval(matrix)

    print(line)
    if prev_key==None:
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
            new_shot_dist = round(shot_dist/total,2)
            new_close_def_dist = round(close_def_dist/total,3)

            temp_boundaries[zone] = (new_shot_dist,new_close_def_dist,new_shot_clock)

            zone = z
            shot_dist,close_def_dist,shot_clock = sd,cd,sc
            total = 1
    else:
        players_boundaries[prev_key] = temp_boundaries
        temp_boundaries = first_boundaries[:]

        zone = z
        shot_dist,close_def_dist,shot_clock = sd,cd,sc
        total = 1

new_shot_clock = round(shot_clock/total,3)
new_shot_dist = round(shot_dist/total,2)
new_close_def_dist = round(close_def_dist/total,3)

temp_boundaries[zone] = (new_shot_dist,new_close_def_dist,new_shot_clock)
players_boundaries[prev_key] = temp_boundaries

# Save dictionary to a JSON file
with open('boundaries.json', 'w') as json_file:
    json.dump(players_boundaries, json_file, indent=4)
    
