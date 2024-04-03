import random
import os
import sys

os.system("touch " + sys.argv[1])

vowels = ['a', 'e', 'i', 'o', 'u']

numbered = []

for n in sys.argv:
	print(n)

if sys.argv[1] == "-l" or sys.argv[1] == "-L":
	lis = open(sys.argv[2], 'r')
else:
	lis = open("list.txt")

with lis as f:
	lines = f.readlines()
	

def checkindex(l1, val):
	cont = 0
	places = []
	for i in l1:
		if i == val:
			places.append(cont)
		cont += 1
	return places

def isinlist(l1, val):
	for i in l1:
		if val == i:
			return True
	return False
counter = 0

if sys.argv[2] == "-f" or sys.argv[2] == "-F":
	with open(str(sys.argv[3]), 'r') as r:
		string = r.readlines()
	
elif sys.argv[2] == "-t" or sys.argv[2] == "-T":
	string = str(sys.argv[3])

else:
	string = str(sys.argv[2])

if type(string) is list:
	for s in string:		
		while counter < len(s):
			if counter != len(s)-1 and isinlist(vowels, s[counter+1]):
				print(checkindex(lines, s[counter] + s[counter+1] + '\n'))
				numbered.append(checkindex(lines, s[counter] + s[counter+1] + '\n'))
				counter +=1
			else:
				print(checkindex(lines, s[counter] + '\n'))
				numbered.append(checkindex(lines, s[counter] + '\n'))
			counter += 1
	del numbered[-1]
else:
	while counter < len(string):
		if counter != len(string)-1 and isinlist(vowels, string[counter+1]):
			numbered.append(checkindex(lines, string[counter] + string[counter+1] + '\n')[0])
			counter +=1
		else:
			numbered.append(checkindex(lines, string[counter] + '\n')[0])
		counter += 1

hexed = []

randi = random.randrange(1000000, 1000000000) 

for n in numbered:
	if type(n) is list:
		hexed.append(hex(int(n[0]) * randi ))
	else:
		hexed.append(hex(int(n) * randi))

with open(sys.argv[1], 'w') as f:
	for x in hexed:
		f.writelines(x + "\n")

print("your encryption key: ", randi)
