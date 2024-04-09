vowels = ['a', 'e', 'i', 'o', 'u']

alphabet = "abcdefghijklmnopqrstuvwxyz"

lis = []

counter = 0

for n in range(256):
	tmp = chr(n)
	lis.append(tmp)
	counter += 1

for i in vowels:
	for n in alphabet:
		tmp = n + i
		lis.append(tmp)
		counter += 1


with open('list.txt', 'w') as f:
	for l in lis:
		f.writelines(l + "\n")
	
	
print(lis)
