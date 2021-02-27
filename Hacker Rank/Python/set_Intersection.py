e = int(input())
se = set(int(i) for i in input().split())
f = int(input())
sf = set(int(i) for i in input().split())
s_i = se & sf
print(len(s_i))