#!/usr/bin/env python
import sys
import re

for line in sys.stdin:
    line = line.strip()
    
    fields = re.split(r',(?=(?:[^"]*"[^"]*")*[^"]*$)', line)
    
    # make the player name and defender the key 
    key = "%s*%s" % (fields[19],fields[14])

    # For the value, use 1 if the player made the shot, 0 otherwise.
    value  = 1 if fields[13]=='made' else 0
    print("%s\t%s" % (key, value))