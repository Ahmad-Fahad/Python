def SumMultiplier(arr):
	flag = "false"
	l = len(arr)
	if l >= 2:
		sum = 0
		for i in arr:
			sum += i
		n = sum*2
		arr.sort()
		max_1 = arr[l-1]
		max_2 = arr[l-2]
		mult = max_1*max_2
		if mult > n:
			flag = "true"
	return flag


print(SumMultiplier([int(x) for x in input().split(',')]))

