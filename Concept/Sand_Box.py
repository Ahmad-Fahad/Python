"""

st = {'rr',2,3,4,5}
st.add(8)
print(st)


lst = [5,5,5,5,5,5,5]
ss = set(lst)
print(ss)
n = input()
st = set(int(i) for i in input().split())

print(sum(st))


for i in range(1, int(input())+1):
	print(int((10**i -1)/9)**2)


x = 1
for i in range(int(input())):
	print(x**2)
	x = (x*10)+1



n = int(input())
x = '1'
for i in range(n):
	output = int(x)**2
	print(output)
	x += '1'

"""
