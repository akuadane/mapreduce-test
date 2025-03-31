#!/usr/bin/env python
import subprocess
import os
import json

# first run, sets up the initial points
command = [
    "/usr/local/hadoop/bin/hadoop", "jar", "/usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar",
    "-input", "/P2/input/shot_logs.csv",
    "-output", "/P2/output/",
    "-mapper", "./q2/first_mapper.py",
    "-reducer", "./q2/first_reducer.py",
    "-file", "./q2/first_reducer.py",
    "-file", "./q2/first_reducer.py",
    # "-file", centroids_file  # Pass the current centroids file to the mappers
]
subprocess.check_call(command)


# Load JSON file into a dictionary
with open('boundaries.json', 'r') as json_file:
    players_boundaries = json.load(json_file)

max_epoches = 2
epoch = 0
while epoch<max_epoches:
    command = [
        "/usr/local/hadoop/bin/hadoop", "jar", "/usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar",
        "-input", "/P2/output/*",
        "-output", "/P2/output/",
        "-mapper", "./q1/mapper.py",
        "-reducer", "./q1/reducer.py",
        "-file", "./q1/mapper.py",
        "-file", "./q1/reducer.py",
        # "-file", centroids_file  # Pass the current centroids file to the mappers
    ]

    subprocess.check_call(command)
    
    with open('boundaries.json', 'r') as json_file:
        new_players_boundaries = json.load(json_file)

    if players_boundaries==new_players_boundaries:
        break
    else:
        players_boundaries=new_players_boundaries

command = [
    "/usr/local/hadoop/bin/hadoop", "jar", "/usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar",
    "-input", "/P2/output/*",
    "-output", "/P2/output2/",
    "-mapper", "./q1/mapper2.py",
    "-reducer", "./q1/reducer2.py",
    "-file", "./q1/mapper2.py",
    "-file", "./q1/reducer2.py",
    # "-file", centroids_file  # Pass the current centroids file to the mappers
]