#made for cleaner script
def readfile(fl):
	"""reads file and returns the data"""
	with open(fl) as f:
		lines = f.readlines()
	
	return lines


def WriteFile(fl, lis):
	"""writes the given data to a given file"""
	with open(fl, 'w') as f:
		for l in lis:
			f.writelines(str(l) + "\n")
