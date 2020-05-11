import os
import sys
def handshake(n):
	c = n*(n-1)/2
	c = int(c)
	return c
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        n = int(input())
        result = handshake(n)
        fptr.write(str(result) + '\n')
    fptr.close()
