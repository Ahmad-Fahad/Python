lst = [['Name', 'Age', 'Country'], ['Bill Gates', '55', 'USA'], ['Mark J','45', 'USa']]

import csv

with open('data_files/icon.csv', 'w') as f_obj:
	f_csv = csv.writer(f_obj)
	f_csv.writerows(lst)