#!/usr/bin/env python
import sys
import json

# Load JSON file into a dictionary
with open('boundaries.json', 'r') as json_file:
    players_boundaries = json.load(json_file)

prev_player = None
zone_hit = [0,0,0,0]
hit = total = zone= 0 
filter_players = ['james harden','chris paul', 'stephen curry','lebron james']

for line in sys.stdin:
    line = line.strip()
    
    key,made = line.split('\t')
    name,z = key.split('-')
    made= int(made)
    z = int(z)

    if name not in filter_players:
        continue
    if prev_player==None:
        prev_player = name
        zone = z

    if prev_player==name:
        if zone==z:
            hit+=made
            total+=1
        else:
            zone_hit[zone] = hit/total
            zone = z
            hit = made
            total = 1
    else:
        max_hit = max(zone_hit)
        max_zone = zone_hit.index(max_hit)
        boundary = players_boundaries[prev_player][max_zone]

        print("%s\t%s"%(prev_player,boundary))
        prev_player = name
        zone = z
        hit = made
        total = 1

if prev_player!=None:
    max_hit = max(zone_hit)
    max_zone = zone_hit.index(max_hit)
    boundary = players_boundaries[prev_player][max_zone]

    print("%s\t%s"%(prev_player,boundary))
        