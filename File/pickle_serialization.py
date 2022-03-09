import pickle

dict_data = {'name':'Fahad', 'country':'Bangladesh'}

with open('data_files/serialize.txt', 'wb') as f_obj:
	pickle.dump(dict_data, f_obj)

with open('data_files/serialize.txt', 'rb') as f_obj:
	dict_data = pickle.load(f_obj)
	print(dict_data)