def avg(n):
	if not n:
		return none
	return sum(n)/len(n)

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

			},
			{
				'List'     : [],
				'expected' : None,
				'No'       : 'empty'

			}
	]

	for i in table:
		assert i['expected'] == avg(i['list']), i['No']

test_table()