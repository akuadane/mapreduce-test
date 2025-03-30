#!/usr/bin/env python
import subprocess
import os
command = [
    "/usr/local/hadoop/bin/hadoop", "jar", "/usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar",
    "-input", "/P2/input/shot_logs.csv",
    "-output", "/P2/output/",
    "-mapper", "../q1/mapper1.py",
    "-reducer", "../q1/reducer1.py",
    "-file", "../q1/mapper1.py",
    "-file", "../q1/reducer1.py",
    # "-file", centroids_file  # Pass the current centroids file to the mappers
]

subprocess.check_call(command)

command = [
    "/usr/local/hadoop/bin/hadoop", "jar", "/usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.1.jar",
    "-input", "/P2/output/*",
    "-output", "/P2/output2/",
    "-mapper", "../q1/mapper2.py",
    "-reducer", "../q1/reducer2.py",
    "-file", "../q1/mapper2.py",
    "-file", "../q1/reducer2.py",
    # "-file", centroids_file  # Pass the current centroids file to the mappers
]

subprocess.check_call(command)