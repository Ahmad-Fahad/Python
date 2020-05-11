def Destroy(lst):
	for i in range(len(lst)-1):
		j = i+1
		while j<len(lst):
			if lst[i] != lst[j]:
				break
			else:
				lst[j] = 0
			j = j+1
	return lst


lst = [1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4,5,5,5,5,5,10,10,10,10,10,11,11,11,11,11,13,13,13,13,13]

k = 1
for i in lst:
	print(i, end=' ')
	if(k%5 == 0):
		print()
	k = k+1


lst_1 = lst.copy()
lst_1 = Destroy(lst_1)
print(lst_1)
print(lst)



'''

Frequency_Alternative_Algo_In_Sorted_List

\\\ Where is the marble problem
\\\ we need to identify the consequtive same data
\\\ Mahbub hasan vai told to count frequcy
\\\ I found same values remain together in sorted list
\\\ so I just keep the first one and make other 0 without changing their index

'''