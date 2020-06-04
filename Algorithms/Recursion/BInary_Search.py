def Binary_Search(lst, x, l, r):
	if l > r or r < 0:
		return -1
	mid = int((l+r)/2)
	if lst[mid] == x:
		print(mid)
		return mid
	if lst[mid] > x:
		Binary_Search(lst, x, l, mid-1)
	if lst[mid] < x:
		Binary_Search(lst, x, mid+1, r)

lst = [1,2,3,4,5,6,7,8,9,10]
x = 6
l = 0
r = len(lst)-1
Binary_Search(lst, x, l, r)

"""
print(flag)
if flag != -1:
	print("Found ", flag)
else:
	print("Not Found")

"""