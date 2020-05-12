n = input().split()
data   = input().split()
weight = input().split()
s = 0 
t = 0
for i in range(len(data)):
	s += int(data[i])*int(weight[i])
for i in weight:
	t += int(i)
W_mean = s/t
print("{:.1f}".format(W_mean))
