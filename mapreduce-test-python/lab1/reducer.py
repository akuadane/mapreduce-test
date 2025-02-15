#!/usr/bin/env python
import sys

cur_ip_hour = None
count= 0
ip_hour = None
for line in sys.stdin:
	ip_hour,freq = tuple(line.strip().split('\t'))
	
	try: 
		freq = int(freq)
		if cur_ip_hour==ip_hour:
			count+=freq
		else:
			if cur_ip_hour:             
				print "%s\t%s"%(cur_ip_hour,count)
			cur_ip_hour=ip_hour
			count = freq
	except:
		pass
	
if cur_ip_hour==ip_hour:	
	print "%s\t%s"%(cur_ip_hour,count)
