import os

print(os.name) #Check platform name (UNIX/Linux = posix, Windows = nt):
print(os.getcwd()) #current working directory

#this directory
file_list = os.listdir(".")    # List files in specific directory
for i in file_list:
	print(i)

#parent directory
print("\n")
file_list = os.listdir("../")    # List files in specific directory
for i in file_list:
	print(i)

#os.remove("f.txt") # Remove a file (delete)

print(os.path.isfile("file.txt"))
print(os.path.isdir("file.txt"))

os.system("ping -i 2 127.0.0.1")# Run a shell command

# f = os.popen("ls -l") #Execute a command & return a file object
# for i in f:
# 	print(i)


# os.mkdir("Dir1") # Create a directory named path with
# os.remove("file.txt")

# os.rename(Dir1, DirX)# Rename the file or directory src to dst

