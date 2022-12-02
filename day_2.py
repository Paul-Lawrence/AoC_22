



def part_1(strats, dict):
	score = 0
	for strat in strats:
		if (dict[strat[0]]==((dict[strat[1]]-1)%3)):
			#print(strat)
			score+=dict[strat[1]]+7
		elif (dict[strat[0]]==dict[strat[1]]):
			score+=dict[strat[1]]+4
		else:
			score+=dict[strat[1]]+1
	return score
	
def part_2(strats,dict):
	score=0
	for strat in strats:
		if (strat[1]=='X'):
			score+=(dict[strat[0]]-1)%3 +1
		elif (strat[1]=='Y'):
			score+=dict[strat[0]]+4
		else:
			score +=(dict[strat[0]]+1)%3 +7			
	return score



def main():
	lines = open('day_2.txt', 'r').readlines()
	strats=[line.strip().split(' ') for line in lines]
	#strats.pop()
	dict = {'A':0, 'B':1, 'C':2, 'X':0, 'Y':1, 'Z':2}
	test=[['A','Y'],['B','X'],['C','Z']]
	print(part_2(strats,dict))
	#print(part_1(strats,dict))

main()