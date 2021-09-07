import re
import sys

[print(line) for line in ([re.findall(r'0{5}[1-9a-zA-Z][0-9a-zA-Z]{26}', line) for line in sys.stdin])[:int(sys.argv[1])] if line]

