import ast

def part_1(pairs):
	score=0
	for i in range(len(pairs)):
		L1=pairs[i][0]
		L2=pairs[i][1]
		print(L1)
		if (comp(L1,L2)):
			#print(i)
			#print(L1,L2)
			score+=(i+1)
	return score
	
def comp(A,B):
	Z=complist(A,B)
	if (Z==-1):
		return comp(A[1:],B[1:])
	return Z
	
def typecomp(A,B):
	#print(A,B)
	if ((type(A)==int)&(type(B)==int)):
		return compints(A,B)
	if ((type(A)==int)!=(type(B)==int)):
		return mixcomp(A,B)
	else:
		return complist(A,B)
			
def compints(a,b):
	if (a<b):
		return True
	if (b<a):
		return False
	else:
		return -1
		
def complist(A,B):
	if (len(A)==0):
		if (len(B)==0):
			return -1
		return True
	if (len(B)==0):
		return False
	return typecomp(A[0],B[0])
	
def mixcomp(A,B):
	if (type(A)==int):
		return complist([A],B)
	else:
		return complist(A,[B])

def main():
	data=open('day_13.txt', 'r').readlines()
	lists=[line.strip() for line in data]
	pairs=[]
	for i in range(len(lists)):
		if (i%3==0):
			x=ast.literal_eval(lists[i])
			y=ast.literal_eval(lists[i+1])
			pairs.append([x,y])
	#print(pairs)
	test=[[[1,1,3,1,1],[1,1,5,1,1]],[[[1],[2,3,4]],[[1],4]],[[9],[[8,7,6]]]]
	#print(pairs)
	print(part_1(pairs))

			
	
main()