import random
import os
import sys
import rnw
import check as ch


#Functions
#############################

def FileToNum(string, list_file_dt, dup):
	numbered = []
	counter = 0

	for s in string:		

		counter = 0
		while counter < len(s):
		
			if counter != len(s)-1 and ch.isinlist(dup, s[counter+1]):
			
				numbered.append(ch.checkindex(list_file_dt, s[counter] + s[counter+1] + '\n'))
			
				counter +=1
			
			else:

				numbered.append(ch.checkindex(list_file_dt, s[counter] + '\n'))
			
			counter += 1

		del numbered[-1]
	
	return numbered


def TextToNum(string, list_file_dt, dup):
	numbered = []
	counter = 0

	while counter < len(string):
	
		if counter != len(string)-1 and ch.isinlist(dup, string[counter+1]):
	
			numbered.append(ch.checkindex(list_file_dt, string[counter] + string[counter+1] + '\n')[0])
	
			counter +=1
	
		else:
	
			numbered.append(ch.checkindex(list_file_dt, string[counter] + '\n')[0])
	
		counter += 1
	
	return numbered


def Encrypt(nums):

	key = random.randrange(1000000, 1000000000)
	enced = []
	
	for n in nums:

		if type(n) is list:

			enced.append(int(n[0]) * key)
		
		else:
		
			enced.append(int(n) * key)

	return key, enced


def decrypt(dt, list_file_dt, key):
	index = 0
	textlist = []
	txt = ""

	for n in dt:

		index = int(int(n) / int(key))
		textlist.append(list_file_dt[index])
	
	for t in textlist:
		txt += ''.join(t).replace('\n', '')
	return txt
	
	