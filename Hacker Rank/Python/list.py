if __name__ == '__main__':
    N = int(input())
    lst = []
    while N>0:
    	cmd = input().split()
    	if cmd[0] == "insert":
    		lst.insert(int(cmd[1]),int(cmd[2]))
    	elif cmd[0] == "print":
    		print(lst)
    	elif cmd[0] == "remove":
    		lst.remove(int(cmd[1]))
    	elif cmd[0] == "append":
    		lst.append(int(cmd[1]))
    	elif cmd[0] == "sort":
    		lst = list(map(int, lst))
    		lst.sort()
    	elif cmd[0] == "pop":
    		lst.pop()
    	elif cmd[0] == "reverse":
    		lst.reverse()
    	N -= 1

