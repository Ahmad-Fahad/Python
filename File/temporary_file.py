from tempfile import TemporaryFile

with TemporaryFile('w+') as f_obj:  # same time a file read and write -> 'w+'
	f_obj.write("Life is cool.\n")
	f_obj.seek(4) # seeek to the begining
	data = f_obj.read()
	print(data)