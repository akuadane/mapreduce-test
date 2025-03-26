#!/usr/bin/env python
import sys
for line in sys.stdin:
    line = line.strip()
    
    fields = line.split(",")
    
    # make the player name and defender the key 
    
    key = "%s-%s" % (fields[22],fields[17])
    value  = 1 if fields[14]=='made' else 0
    print "%s\t%s" % (key, value)