import re
import sys

arr = ([re.findall(r'0{5}[1-9a-zA-Z][0-9a-zA-Z]{26}', line) for line in sys.stdin])
for line in arr[:int(sys.argv[1])]:
	if line:
		print(*line)
