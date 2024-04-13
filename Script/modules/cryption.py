import random
import os
import sys
import rnw

def checkindex(l1, v1):
	count = 0
	for l in l1:
		if v1 == l:
			return count
		count += 1

#Functions
#############################

def FileToNum(string, list_file_dt, dup):
	"""converts the given file's data to decimal"""
	numbered = []
	counter = 0

	#going through each element of string and converting it to decimal with duplicates
	for s in string:		

		counter = 0
		while counter < len(s):
		
			if counter != len(s)-1 and s[counter+1] in dup :
			
				numbered.append(checkindex(list_file_dt, (s[counter] + s[counter+1] + '\n')))
			
				counter +=1
			
			else:
				
				tmp = s[counter] + '\n'
				numbered.append(checkindex(list_file_dt, s[counter]+'\n'))
			
			counter += 1

		del numbered[-1]
	return numbered


def TextToNum(string, list_file_dt, dup):
	"""converting given text to decimals"""
	numbered = []
	counter = 0

	#going through each element of given string and converting it to decimal with duplicates
	while counter < len(string):
		
		if counter != len(string)-1 and string[counter+1] in dup:
	
			numbered.append(checkindex(list_file_dt, string[counter] + string[counter+1] + '\n')[0])
	
			counter +=1
	
		else:
	
			numbered.append(checkindex(list_file_dt, string[counter] + '\n')[0])
	
		counter += 1
	
	return numbered


def Encrypt(nums):
	"""encrypts the decimal data by using a key with the length of 7 to 10"""
	#generating a random key
	key = random.randrange(1000000, 1000000000)
	enced = []
	
	#going through nums elements to convert them do unconvertable decimals
	for n in nums:
		if type(n) is list and len(n) != 0:
			enced.append(int(n[0]) * key)
		else:
		
			enced.append(n * key)

	return key, enced


def decrypt(dt, list_file_dt, key):
	"""decrypts given data by using the encryptiong key"""
	index = 0
	textlist = []
	txt = ""

	#goes through the data and reverses the encryption
	for n in dt:

		index = int(int(n) / int(key))
		textlist.append(list_file_dt[index])
	
	for t in textlist:
		txt += ''.join(t).replace('\n', '')
	return txt
	
	