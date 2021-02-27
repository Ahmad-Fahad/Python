from itertools import combinations

S,k = input().split()
lst = sorted(S)
for j in range(1,int(k)+1):
    for i in combinations(lst,j):
        print("".join(i))
