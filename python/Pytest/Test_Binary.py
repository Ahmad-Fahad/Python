def Binary_Search(lst, x):
	left   = 0
	right  = len(lst)-1
	while left<=right:
		mid = (left+right)/2
		mid = int(mid)
		if lst[mid] == x:
			return mid
		elif lst[mid] < x:
			left = mid+1
		elif lst[mid] > x:
			right = mid-1
	return -1

lst    = [1,2,3,4,5,6,7,8,9,10]
k = 3
if k in lst:
	print("Loop in if")

for x in range(20):
	i = Binary_Search(lst, x)
	if i == -1:
		if x in lst:
			print("Error Captured : ", x)
		else:
			print("Correct")
	else:
		print("Correct") 

