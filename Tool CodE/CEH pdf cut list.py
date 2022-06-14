init = 16
count = 20
next_module_start = 0
prev_module_end = init
while count != 0:
	start = 0
	end   = 0
	next_module_start = int(input("Enter Next Module Start Page: \n")) + init
	start = prev_module_end + 1 
	end   = next_module_start - 1
	print(f"Range: {start} ---->> {end} ")
	prev_module_end = end
	count = count - 1
	


  