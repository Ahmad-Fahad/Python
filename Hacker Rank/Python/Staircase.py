#!/bin/python

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
	for i in range(1,n+1):
		for j in range(n-i,0,-1):
			print(" ", end='')
		for j in range(i):
			print("#", end='')
		print()

if __name__ == '__main__':
    n = int(input())
    staircase(n)
