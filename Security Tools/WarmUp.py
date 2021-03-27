if __name__ == '__main__':
	httpPort = 80
	print(httpPort)

	url = "http://www.linuxac.org/"
	print(url)

	logFile = "/var/log/messages"
	print(logFile[0])
	print(logFile[1:4])
	print(logFile[-8])
	print(logFile[-8:])

	splited = logFile.split("/")
	print(splited)
	print(logFile)

	userName   = "binary"
	domainName = "gmail"
	userEmail  = userName + "@" + domainName + ".com"
	print(userEmail) 

	webSite = "http://linuxac.org/"
	param   = "?p=123"
	url     = "".join([webSite, param])  # "" separated string
	print(url)
	print("\n")
	url     = "__XXX__".join([webSite, param,webSite,param])
	print(url)

	portList =  [21,22,80]
	portList.append(443)
	print(portList)
	portList.remove(22)
	print(portList)
	portList.insert(1, 143)
	print(portList)
	if(portList[0] == 22):
	    print("SSH")
	else:
	    print("unknown")

	httpType = type(portList[2])
	print(httpType)
	httpType = str(portList[2])
	print(type(httpType))
	print(httpType)

	l = len(portList)
	print(l) 

	ip  = "192.168.1.1"
	mac = "AA:BB:CC:DD:EE:FF"

	print("IP = "+ ip , "\n" "MAC = "+  mac) 

	x = '\x41'
	print(x)

	h = hex(65)
	print(h)

	h = hex(255)
	print(h)

	# email = input("Enter mail address : ")
	# print(type(email))

	f = open("../Concept/file_1.txt", "r")
	for i in f:
		print(i)
		
	f.close()

	def checkValidPort(port):
		if port>65535 or port<0:
			return False
		else:
			return True

	print(checkValidPort(80))
	print(checkValidPort(-1))
