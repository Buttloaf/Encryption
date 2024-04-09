
def readfile(fl):
	with open(fl) as f:
		lines = f.readlines()
	
	return lines


def WriteFile(fl, lis):
	with open(fl, 'w') as f:
		for l in lis:
			f.writelines(str(l) + "\n")
