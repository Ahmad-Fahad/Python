#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
	t = ""
	flag = 0
	for i in s:
		if flag == 0:
			if(ord(i)>=97 and ord(i)<=122):
				i = chr(ord(i)-32)
				flag=1 
			if(ord(i)>=65 and ord(i)<=90):
				flag=1
			if(ord(i)>=48 and ord(i)<=57):
    			flag=1
		elif i == ' ':
			flag = 0
		t+=i
	return t
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

"""

s = input()
t = ""
flag = 0
for i in s:
	if flag == 0:
		if i != ' ':
			if(ord(i)>=97 and ord(i)<=122):
				i = chr(ord(i)-32)
			flag=1
		else:
			flag = 0
	t+=i


print(t)


"""