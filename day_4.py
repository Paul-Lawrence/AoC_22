def part_1(ids):
	pairs=0
	ids = [(i.split(',')) for i in ids]		
	newids=[]
	for i in range (len(ids)):
		a=ids[i][0].split('-')
		b=ids[i][1].split('-')
		for c in b:
			a.append(c)
		newids.append([int(c) for c in a])
	for id in newids:
		if ((id[0]<=id[2])&(id[1]>=id[3])):
			pairs+=1
		elif ((id[2]<=id[0])&(id[3]>=id[1])):
			pairs +=1
	return pairs
		
def part_2(ids):
	pairs=0
	ids = [(i.split(',')) for i in ids]		
	newids=[]
	for i in range (len(ids)):
		a=ids[i][0].split('-')
		b=ids[i][1].split('-')
		for c in b:
			a.append(c)
		newids.append([int(c) for c in a])
	for id in newids:
		if ((id[1]>=id[2])&(id[1]<=id[3])):
			pairs+=1
		elif ((id[3]>=id[0])&(id[3]<=id[1])):
			pairs+=1
	return pairs
		
		
		
		
		
def main():
	ids=[line.strip() for line in open('day_4.txt', 'r').readlines()]
	test=['2-8,3-7','2-6,7-8']
	#print(part_2(test))
	print(part_2(ids))
	
main()