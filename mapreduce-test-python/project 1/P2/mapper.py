#!/usr/bin/env python
import sys
for line in sys.stdin:
    line = line.strip()
    
    fields = line.split()
    
    # make the player name and defender the key 
    key = "%s-%s" % (fields[19],fields[14])
    value  = 1 if fields[13]=='made' else 0
    print "%s\t%s" % (key, value)