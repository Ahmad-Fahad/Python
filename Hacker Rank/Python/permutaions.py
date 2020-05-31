from itertools import permutations

s, k = input().split()
lst = list(permutations(s, int(k)))
lst.sort()
for i in lst:
	ls = ''.join(i)
	print(ls)
