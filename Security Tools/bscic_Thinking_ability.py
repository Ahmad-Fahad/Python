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
