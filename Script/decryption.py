import sys

key = sys.argv[1]

file = open(sys.argv[2])

numbered = []

with file as f:
	lines = f.readlines()
	
with open(sys.argv[3]) as li:
	lis = li.readlines()

for l in lines:
	
	numbered.append(int(l) / int(key))


texed = []

for n in numbered:
	texed.append(lis[int(n)])


