def avg(lst):
	if not lst:
		return none
	return sum(lst)/len(lst)

def test_table():
	table = [
				{
					'List'     : [1,2,3],
					'expected' : 2,
					'No'       : 'Case 1'
				},
				{
					'List'     : [1,2,3,4],
					'expected' : 2,
					'No'       : 'Case 2'
				},
				{
					'List'     : [100],
					'expected' : 100,
					'No'       : 'Case 3'
				}

	]
	
	print(table[2]['expected'])
	print(table[2]['List'])
	print(table[2]['No']) 

	avg(table[0]['List'])

	for i in table:
		assert i['expected'] == avg(i['List']), "Error Occured in "+i['No']

#test_table()




'''
			{
				'List'     : [],
				'expected' : None,
				'No'       : 'empty'
			}



		print(i['No'])
		print(avg(i['List']))
'''