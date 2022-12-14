import ast
import functools

def part_1(lists):
	pairs=[]
	for i in range(len(lists)):
		if (i%3==0):
			x=ast.literal_eval(lists[i])
			y=ast.literal_eval(lists[i+1])
			pairs.append([x,y])
	score=0
	for i in range(len(pairs)):
		L1=pairs[i][0]
		L2=pairs[i][1]
		#print(L1)
		if (comp(L1,L2)<0):
			#print(i)
			#print(L1,L2)
			score+=(i+1)
	return score
	
def part_2(lists):
	L=[]
	for i in range(len(lists)):
		if (i%3!=2):
			L.append(ast.literal_eval(lists[i]))
	L.append([[2]])
	L.append([[6]])
	L=sorted(L,key=functools.cmp_to_key(comp))
	A=L.index([[2]])+1
	B=L.index([[6]])+1
	print(A,B)
	return A*B
	
def comp(A,B):
	#print(A,B)
	Z=complist(A,B)
	if (Z==0):
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
		return -1
	if (b<a):
		return 1
	else:
		return 0
		
def complist(A,B):
	if (len(A)==0):
		if (len(B)==0):
			return 0
		return -1
	if (len(B)==0):
		return 1
	Z=typecomp(A[0],B[0])
	if (Z==0):
		return complist(A[1:],B[1:])
	else:
		return Z
	
def mixcomp(A,B):
	if (type(A)==int):
		return complist([A],B)
	else:
		return complist(A,[B])

def main():
	data=open('day_13.txt', 'r').readlines()
	lists=[line.strip() for line in data]	
	test=[[[1,1,3,1,1],[1,1,5,1,1]],[[[1],[2,3,4]],[[1],4]],[[9],[[8,7,6]]],[[[4,4],4,4],[[4,4],4,4,4]],[[7,7,7,7],[7,7,7]],[[],[3]],[[[[]]],[[]]],[[1,[2,[3,[4,[5,6,7]]]],8,9],[1,[2,[3,[4,[5,6,0]]]],8,9]]]
	#print(pairs)
	print(part_2(lists))

			
	
main()