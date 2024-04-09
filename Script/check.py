
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

