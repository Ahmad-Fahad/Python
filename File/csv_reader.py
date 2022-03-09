import csv

with open("data_files/iphone_price.csv", 'r') as f_obj:
	f_csv = csv.reader(f_obj)

for i, row in enumerate(f_csv):
	print(i, row[0], row[1])
