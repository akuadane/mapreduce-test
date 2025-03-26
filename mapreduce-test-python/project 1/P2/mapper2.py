#!/usr/bin/env python
import sys
for line in sys.stdin:
    line = line.strip()
    
    fields = line.split(",")
    
    # make the player name and defender the key 
    key = "%s-%s" % (fields[22],fields[17])

    # For the value, use 1 if the player made the shot, 0 otherwise.
    value  = 1 if fields[14]=='made' else 0
    print "%s\t%s" % (key, value)