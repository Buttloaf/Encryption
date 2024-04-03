vowels = ['a', 'e', 'i', 'o', 'u']

alphabet = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
lis = []

counter = 0

for n in numbers:
	tmp = n
	lis.append(tmp)
	counter += 1
	
for a in alphabet:
	tmp =a
	lis.append(tmp)
	counter +=1

for i in vowels:
	for n in alphabet:
		tmp = n + i
		lis.append(tmp)
		counter += 1


with open('list.txt', 'w') as f:
	for l in lis:
		f.writelines(l + "\n")
	
	
print(lis)
