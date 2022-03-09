import json

data = {
	'name': 'Bill Gates',
	'age' : 55,
	'country' : 'USA',
	'is_retired' : True
}




json_encoded_str = json.dumps(data)   # dumps()
print(json_encoded_str)

json_decode = json.loads(json_encoded_str) # loads()
print(json_decode)


with open("data_files/json_data.json", 'w') as f_obj:
	json.dump(data, f_obj)    			# dump()

with open("data_files/json_data.json", 'r') as f_obj:
	json_data = json.load(f_obj)       # load()
	print(json_data)

