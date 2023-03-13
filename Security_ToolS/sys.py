
import sys

# Check Python path, and count them
print(sys.path)
for i in sys.path:
	print(i)
# Print all imported modules
print(sys.modules.keys())

# Print the platform type (linux, win32, mac, etc)

print(sys.platform)

# Check application name, and list number of passed arguments

print(sys.argv[0])
print(sys.argv)

if len(sys.argv) > 1:
	print("You passed", len(sys.argv)-1, "arguments. They are:")
for arg in sys.argv[1:]:
	print(arg)
else:
	print("No arguments passed!")

print(sys.version)

	