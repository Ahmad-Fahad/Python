while True:
	current_page   = int(input("Current: "))
	next_page      =  int(input("Next: "))
	start = current_page + 92
	end   = next_page + 92 - 1
	print(f"Range : {start}-{end}")