
"""

x = "its global"

def fantastic():
	print("about")
	global x
	x= 230


def lamented():
	print("Sad")

y = input()

if y == "fantastic":
	fantastic()
else:
	lamented()

k = 5j
print(type(k))

"""
"""

lst = [1,2,3,4,5,6,7,8,9, 12,12,23,34,435,6,56,34,23,45,7678,3]

for x in lst:
	print(x)


lst.append(777)
print(lst)



team = {
	"leader" : {
		"name"  : "Fahad",
		"batch" : 13
	},
	"commander" : {
		"name" : "Shakil",
		"batch" : 24,
		55 : "Ok"
	} 
}

print(team['commander'][55])

battalion_1 = {
	"cic"  : "xxxx",
	"rank" : "Lt. Colonel"
}
battalion_2 = {
	"cic"  : "yyy",
	"rank" : "Lt. Colonel"
}
battalion_3 = {
	"cic"  : "zzz",
	"rank" : "Lt. Colonel"
}
battalion_4 = {
	"cic"  : "ggg",
	"rank" : "Lt. Colonel"
}
battalion_5 = {
	"cic"  : "hhh",
	"rank" : "Lt. Colonel"
}

regiment = {
	"battalion_1" : battalion_1,
	"battalion_2" : battalion_2,
	"battalion_3" : battalion_3,
	"battalion_4" : battalion_4,
	"battalion_5" : battalion_5,
}


print(regiment["battalion_3"]["cic"])

a = 33
b = 33

print("A") if a<b else print("AB") if a==b else print("B")

if a == b:
	pass # scontinue in c

while a>0:
	print(a)
	a -= 1



adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]


for x in adj:
	for y in fruits:
		print(x,y)
	print("\n")

def  fruit(*x):
	print(x[1])


fruit("apple", "banana", "cherry")

def  fruiit(**x):
	print(x)


fruiit(a = "apple", b =  "banana", c = "cherry")

def country(name = "Bangladesh"):
	print(name)

country("Germany")
country()



def recurse(n):
	if n<0:
		return

	else:
		recurse(n-1)
		print(n)
		

recurse(10)

x = 1111111
y = 3333333
z = 55555
txt = "ggggggggggg {} ggggggggg {} ggggggggggg {}"
print(txt.format(x, y, z))

txt = "ggggggggggg {1} ggggggggg {2} ggggggggggg {0}"
print(txt.format(x, y, z))

txt = "ggggggggggg {1} ggggggggg {2:.5f} ggggggggggg {0}"
print(txt.format(x, y, z))

m = 10
print(type(m))

t = 187687654564658970978909869576453
print(type(t))

n = 5

r = m % n
q = m / n
print(r)
print(q)

if(m%n == 0):
	print("Ok")




# a = list(map(int, input().split()))

def double(i):
	return 5*i

a=()
a = input()
r = map(double, a)

print(list(r))


def return_int(i):
	return int(i)

a = ()
a = input()
r = map(return_int, a)
t = list(r)
print(t)
print(t[1])


x, y = input().split() 
x = int(x)
y = int(y)
print(x) 
print(y) 

print()

m = list(map(int, input().split())) 
print(m) 

a = list(map(int, input().split()))
print(a) 

while True:
	try:
	    x = input()
	    print(x)
    except EOFError:
        break



while True:
	try:
		print(input())
	except EOFError:
		break

		


x = 90
y = 0
whil
try:
	result = x / y
except ZeroDivisionError:
	print("You can't divide s")

"""

def avg(n):
	if not n:
		return none

	return sum(n)/len(n)


if __name__ == "__main__":

	l = [1,2,3,4,5]
	print(avg(l))