def part_1(stax, instructions):
	for i in instructions:
		s=i.split(' ')
		a=int(s[1])
		b=int(s[3])
		c=int(s[5])
		for j in range(a):
			x=stax[b-1].pop()
			stax[c-1].append(x)
	print(stax)
	message=[]
	for s in stax:
		message.append(s.pop())
	return message
	
def part_2(stax, instructions):
	for i in instructions:
		s=i.split(' ')
		a=-1*int(s[1])
		b=int(s[3])
		c=int(s[5])
		x=stax[b-1][a:]
		stax[b-1]=stax[b-1][:a]
		for y in x:
			stax[c-1].append(y)
	print(stax)
		
def main():
	box=[line.strip() for line in open('day_5.txt', 'r').readlines()]
	boxes=box[:9]
	instructions=box[10:]
	stacks=boxes[::-1][1:]
	bx=[]
	n=len(boxes[-1].split())
	for j in range(len(stacks)):
		b=[]
		for i in range(n):
			if (4*(i+1)-3>len(stacks[j])):
				b.append(' ')
			else:
				b.append(stacks[j][4*(i+1)-3])
		bx.append(b)
	stax=[]
	for i in range(n):
		s=[]
		for j in range(len(bx)):
			if (bx[j][i]==' '):
				continue
			else:
				s.append(bx[j][i])
		stax.append(s)
	test=[['Z','N'],['M','C','D'],['P']]
	testin=['move 1 from 2 to 1','move 3 from 1 to 3','move 2 from 2 to 1', 'move 1 from 1 to 2']
	part_2(stax, instructions)
	#print(part_2(test))
	#print(part_2(ids))
	
main()