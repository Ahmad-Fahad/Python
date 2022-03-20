strg = input()
l = len(strg)
print(l)

rev_str=""
for i in range(l-1, -1, -1):
	rev_str = rev_str + strg[i]
print(rev_str)


