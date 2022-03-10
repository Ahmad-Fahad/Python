day   = 10
month = "____________MARCH____"
with open("In_Queue.txt", 'w') as f_obj:
	for i  in range(16):
		f_obj.write(month)
		day = day+1
		f_obj.write(str(day))
		f_obj.write("\n\n-------------------\n\n")
		f_obj.write("PRIME_WORKs")
		f_obj.write("\n\n-------------------\n\n")
		f_obj.write("1] \n2]\n3] \n4] \n5] \n")
		f_obj.write("\n\n...................\n\n")
		f_obj.write("Tasks TO Do")
		f_obj.write("\n\n-------------------\n\n")
		f_obj.write("1] \n2]\n3] \n4] \n5] \n")
		f_obj.write("\n\n...................\n\n")
		f_obj.write("Regular Activities")
		f_obj.write("\n\n-------------------\n\n")
		f_obj.write("1] News_Paper\n2] Review \n3] Exercise \n4] Easin\n5] T-3\n 6] D-200 \n7] Evil-Eye \n8] Shir 9] \n10] Bath \n11] Oykia")
		f_obj.write("\n\n####################&&####################\n")
		f_obj.write("####################&&####################\n\n")