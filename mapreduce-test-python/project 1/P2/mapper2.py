#!/usr/bin/env python
import sys


for line in sys.stdin:
    line = line.strip()
    
    
    key, hit_score= line.split("\t")
    player, defender = key.split('-')

    # make the key player - hitscore
    key = "%s-%s"%(player,hit_score)

    # make the value - defender
    print("%s\t%s"%(key,defender))
