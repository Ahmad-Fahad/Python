stng = input()
lw = []
up = []
ev = []
od = []
for i in stng:
	if i.isdigit():
		n = int(i)
		if n%2 == 0:
			ev.append(n)
		else:
			od.append(n)
	if i.isupper():
		up.append(i)
	if i.islower():
		lw.append(i)

lw.sort()
up.sort()
ev.sort()
od.sort()

out_sorted = lw+up+od+ev
output     = ""
for i in out_sorted:
	output += str(i)

print(output)