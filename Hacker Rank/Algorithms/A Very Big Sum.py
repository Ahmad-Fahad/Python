def aVeryBigSum(ar):
	sum = 0
	for i in ar:
		sum += i
	return sum

ar = [int(i) for i in input().split()]
result = aVeryBigSum(ar)
print(result)
