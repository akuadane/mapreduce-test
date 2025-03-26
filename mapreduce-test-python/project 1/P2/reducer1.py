#!/usr/bin/env python
import sys

prev_key = None
made=total=0
for line in sys.stdin:
    line = line.strip()
    
    key, value= line.split("\t")

    # convert the shot value to int
    value = int(value)
    if prev_key == key:
        made+=value
        total+=1
    else:
        if prev_key!=None:
            print '%s' % (made/total)
            hit_score = str(made/total)
            print "%s\t%s"%(prev_key,total)
        
        prev_key = key
        made  = value
        total = 1

hit_score = str(round(made/total,2))
print "%s\t%s"%(prev_key,hit_score)
    
    