import itertools
import math

def prime_flag(n):
  if n%2 == 0:
    return False
  else:
    limit = math.sqrt(n)+1
    for i in range(3, limit, 2):
      if n%i == 0:
        return False
    return True

def PrimeChecker(num):
  str_n = str(num)
  for i in itertools.permutations(str_n, len(str_n)):
    if prime_flag(int("".join(i))):
      return 1
    else:
      return 0


print(PrimeChecker(input()))