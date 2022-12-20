class coord:
	def __init__(self,num, c):
		self.value=num
		self.loc=c

def part_1(nums):
	Nums=[n for n in nums]
	zloc=0
	#print([n.value for n in Nums])
	#print([n.loc for n in Nums])
	for i in range(len(nums)):
		j=nums[i].loc
		n=Nums.pop(j)
		c=(j+n.value)%len(Nums)
		n.loc=c
		#if (c==0):
		#	c=len(Nums)-1
		#	Nums.append(n)
		#else:
		Nums.insert(c,n)
		if (c>j):
			for k in range(j,c):
				Nums[k].loc=Nums[k].loc-1
		elif (c<j):
			for k in range(c+1,j+1):
				Nums[k].loc+=1
		#print([n.value for n in Nums])
		#print([n.loc for n in Nums])
	for n in Nums:
		if (n.value==0):
			zloc=n.loc
			#print(zloc)
	a=len(Nums)
	#print([n.value for n in Nums])
	#print([n.loc for n in Nums])
	#print((zloc+1000)%len(Nums))
	#print(zloc)
	tot=(Nums[(zloc+1000)%a].value+Nums[(zloc+2000)%a].value+Nums[(zloc+3000)%a].value)
	#print(Nums[(zloc+1000)%a].value)
	return tot
	
def part_2(nums):
	Nums=[coord(n.value*811589153,n.loc) for n in nums]
	print([n.value for n in Nums])
	zloc=0
	for m in range(1):
		for i in range(len(nums)):
			j=nums[i].loc
			n=Nums.pop(j)
			c=(j+n.value)%len(Nums)
			n.loc=c
			Nums.insert(c,n)
			if (c>j):
				for k in range(j,c):
					Nums[k].loc=Nums[k].loc-1
			elif (c<j):
				for k in range(c+1,j+1):
					Nums[k].loc+=1
			print([n.value for n in Nums])
			print([n.loc for n in Nums])
	for n in Nums:
		if (n.value==0):
			zloc=n.loc
	a=len(Nums)
	#print([n.value for n in Nums])
	#print([n.loc for n in Nums])
	tot=(Nums[(zloc+1000)%a].value+Nums[(zloc+2000)%a].value+Nums[(zloc+3000)%a].value)
	return tot
	
def ch(nums):
	x=[n*81589153 for n in nums]
	j = list(range(len(x)))
	
	for _ in range(10):
		for i in range(len(x)):
			c=j.index(i)
			j.pop(c)
			j.insert((c+x[i])%len(j),i)
		#print(x)
		#print(j)
	z=j.index(x.index(0))
	print(sum(x[j[(z+i)%len(j)]]for i in [1000,2000,3000]))
	
	
	#while(i<len(nums)):
	#	if (nums[i].moved==True):
	#		i+=1
	#	else:
	#		n=nums.pop(i)
	#		nums.insert((i+n.value)%len(nums),n)
	#		n.moved=True
	#	print([n.value for n in nums])
	#return nums
	
	
	
def main():
	#nums=[coord(int(line.strip())) for line in open('day_20.txt', 'r').readlines()]
	nums=[int(line.strip()) for line in open('day_20.txt', 'r').readlines()]
	for i in range(len(nums)):
		nums[i]=coord(nums[i],i)
	#print([n.value for n in nums])
	test=[1,2,-3,3,-2,0,4]
	#for i in range(len(test)):
	#	test[i]=coord(test[i],i)
	#print(part_2(test))
	cheat=[int(x.strip()) for x in open('day_20.txt','r').readlines()]
	ch(test)
	
	
main()