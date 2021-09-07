import sys

mask = '*...***.***.*.*'

def main():
	i = 0
	data = ''
	while (i < 3):
		data +=  sys.stdin.readline().rstrip('\n')
		if (len(data) > (i + 1) * 5):
			print("Error")
			return (-1)
		i += 1
	i = 0
	while (i < 15):
		if (mask[i] == '*' and data[i] != '*') or (mask[i] == '.' and data[i] == '*'):
			print("False")
			return (-1)
		i += 1
	print("True")
	return(0)

if __name__ == "__main__":
	main()


