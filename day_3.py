



def part_1(sacks):
	score=0
	for sack in sacks:
		comp1, comp2=sack[:len(sack)//2], sack[len(sack)//2:]
		comp1, comp2=set(list(comp1)), set(list(comp2))
		c=list(comp1.intersection(comp2))[0]
		if (c.isupper()):
			score+=ord(c)-38
		else:
			score+=ord(c)-96
	return score
	
def part_2(sacks):
	score=0
	for i in range(len(sacks)//3):
		group=sacks[3*i:3*(i+1)]
		sets=[]
		for g in group:
			sets.append(set(list(g)))
		c=list(sets[0].intersection(sets[1],sets[2]))[0]
		if (c.isupper()):
			score+=ord(c)-38
		else:
			score+=ord(c)-96
	return score
		
		
def main():
	lines = open('day_3.txt', 'r').readlines()
	sacks=[line.strip() for line in lines]
	print(part_2(sacks))
	
main()