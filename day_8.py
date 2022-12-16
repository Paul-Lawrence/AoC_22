import numpy as np

def part_1(A):
	n=len(A)
	m=len(A[0])
	count=2*(n+m)-4
	for i in range(1,n-1):
		for j in range(1,m-1):
			x=A[i,j]
			if ((check(A[:i,j],x)) or (check(A[i+1:,j],x)) or (check(A[i,:j],x)) or (check(A[i,j+1:],x))):
				count+=1
				print("Visible tree at {},{}".format(i+1,j+1))
	print(len(A),len(A[0]))
	return count
	
def part_2(A):
	n=len(A)
	m=len(A[0])
	max=0
	for i in range(n):
		for j in range(m):
			score=1
			x=A[i,j]
			B=np.flip(A[:i,j])
			score=score*trees(B,x)
			#print(score)
			C=A[i+1:,j]
			score=score*trees(C,x)
			#print(score)
			score=score*trees(A[i,j+1:],x)
			#print(score)
			score=score*trees(np.flip(A[i,:j]),x)
			print(score)
			if (score>max):
				max=score
			
	return max

def trees(B,x):
	score=0
	for c in range(len(B)):
		if (x>B[c]):
			score+=1
		else:
			#print(x,score,B)
			return score+1
	#print(x,score,B)
	return score
	
def check(B,x):
	if (np.max(B)<x):
		return True
	else:
		return False
			
def main():
	data=open('day_8.txt', 'r').readlines()
	lines=[[int(d) for d in line.strip()] for line in data]
	#print(lines)
	A=np.array(lines)
	test=np.array([[3,0,3,7,3],[2,5,5,1,2],[6,5,3,3,2],[3,3,5,4,9],[3,5,3,9,0]])
	print(part_2(A))

		
main()