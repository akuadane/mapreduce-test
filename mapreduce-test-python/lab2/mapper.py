#!/usr/bin/env python
import re
import sys

pat = re.compile('(?P<ip>\d+\.\d+\.\d+\.\d+).*?\d{4}:(?P<hour>\d{2}):\d{2}.*? ')

# get the range passed by the user
r = sys.argv[1]
start, end  = tuple(r.split('-'))

try:
    start = int(start)
    end = int(end)

    for line in sys.stdin:
    match = pat.search(line)
    if match:
        hour = int(match.group('hour'))
        if start<=hour<=end:
            print '%s\t%s' % ('[' + match.group('hour') + ':00' + ']' + match.group('ip'), 1)

except:
    pass




