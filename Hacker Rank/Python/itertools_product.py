from itertools import product

lst_1 = list(int(i) for i in input().split())
lst_2 = list(int(i) for i in input().split())

lst   = list(product(lst_1, lst_2))
for i in lst:
	print(i, end=" ")