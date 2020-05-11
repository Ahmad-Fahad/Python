n = int(input())
lst = []
lst = list(map(int, input().split(' ')))
lst.sort()
sum = 0
for i in lst:
	sum = sum + i
mean = sum/n
mid  = n/2
mid  = int(mid)
if n%2 == 0:
	median = (lst[mid]+lst[mid-1])/2
else:
	median = lst[mid]/2
frequency = {}
for i in lst:
	frequency[i] = lst.count(i)
max = 0
for key,value in frequency.items():
	if max<value:
		max   = value
		index = key
flag = 0
for i in frequency:
	if frequency[i]>1:
		flag = 1
		break
print(mean)
print(median)
if flag == 1:
	print(index)
else:
	print(lst[0])

	