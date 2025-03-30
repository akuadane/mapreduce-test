#!/usr/bin/env python
import sys

prev_player = None
defender = None
for line in sys.stdin:
    line = line.strip()
    
    key, defender= line.split("\t")

    player,hit_score = key.split('-')   

    # print the first occurence of the key
    if prev_player!=player:
        prev_player = player
        print("%s\t%s with hit score %s"%(player,defender,hit_score))
    
    
