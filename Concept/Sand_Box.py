# hash syntax 
_hash = {1:2, 4:5}
print(_hash[4])

#hash assaign from list
target = 9
nums = [2, 7, 11, 15]
print(nums)
hash_map = {}
for i in range(len(nums)):
	hash_map[nums[i]] = i
for i in range(len(nums)):
	complement = target-i
	if complement in hash_map :
		print(hash_map[complement])

print(hash_map)


# two input in one line
R, L = [int(x) for x in input().split()]

x = int(input("X = "))
print(x*10)

for i in range(2,150, 4):
	print("{}-{},  ". format(i, i+1), end='' )

print()

for i in range(4,150, 4):
	print("{}-{},  ". format(i, i+1), end='' )




"""

lst_1 = [1,2,3]
lst_2 = [9,4,5,6]

for i in range(len(lst_2)):
	if lst_2[i]>5:
		lst_2[i]=0
print(lst_2)

lst_3 = [lst_1]+[lst_2]
print(list(zip(*lst_3)))

A = [1,2,3]
B = [6,5,4]
C = [7,8,9]
X = [A] + [B] + [C]

print(list(zip(*X)))


t = 2 
m = []
while t<0:
	t-=1
	z = [float(i) for i in input().split()]
	m += z
print(m)



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
