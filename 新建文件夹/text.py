"""
给出的s列表中正负交替出现，把其中连续的正数与连续的负数分组。
"""
s = [1,2,3,-1,-2,4,3,1,-2,-4,-6]
k = [0,0,0,1,1,0,0,0,1,1,1]
def	fenzu(list):
	key = [0]
	for i in range(len(s)-1):
		if s[i]*s[i+1] < 0:
			key.append(i+1)
	return key	
k = fenzu(s)
print(k)

def fen(list):
	res = []
	key = fenzu(list)
	for k in range(len(key)-1):
		res.append(list[key[k]:key[k+1]])
	res.append(list[key[-1]:])
	return res
print(fen(s))

z = zip(k, s)
for i in z:
	print(i)
