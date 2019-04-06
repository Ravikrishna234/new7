#!/usr/bin/env python
import sys

result = {}
for line in sys.stdin:
	res = line.strip().split()
	if (res[0] in result):
		result[res[0]].append(res[1])
	else:
		result[res[0]] = [res[1]]

for keys in result:
	print keys, len(result[keys])

