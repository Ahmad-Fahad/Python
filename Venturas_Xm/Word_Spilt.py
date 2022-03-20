def WordSplit(strArr):
	word = strArr[0]
	dictionary = strArr[1].split(',')
	print(dictionary.count(dictionary[0]))
	
	return word

lst = ["baseball", "a,all,b,ball,bas,base,cat,code,d,e,quit,z"]
print(WordSplit(lst))