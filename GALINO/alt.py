def even_rotate(li :list, n: int):
	s = li[n+1:]
	li = li[:n+1]
	li = s+li
	return li

def odd_rotate(li: list, n: int):
	s = li[:n]
	li = li[n:]
	li = li+s
	return li

def checkList(li: list):
	for i in li:
		if type(i) == list:
			return True

def alternate_rotate(li: list, n: int, level = 0):
	if checkList(li) == True:
		if level%2 == 0:
			li = even_rotate(li, n)
		else:
			li = odd_rotate(li, n)
		level += 1
		for i in li:
			if isinstance(i, list):
				li = alternate_rotate(li, n, level)
		return li
	else:
		if level%2 == 0:
			li = even_rotate(li,n)
		else:
			li = odd_rotate(li,n)
		return li

li = ['a', ['b'], ['c', [['d'], 'e', 'f'], 'g']]
print(alternate_rotate(li, 1))
