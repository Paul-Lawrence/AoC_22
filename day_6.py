def part_1(string):
	#print(string[0:3])
	for i in range(len(string)-14):
		s=string[i:i+14]
		t=set(s)
		if (len(t)==len(s)):
			return i+14	
	
	
def main():
	data=open('day_6.txt', 'r').readlines()
	string=data[0].strip()
	#print(string[0:4])
	#print(string[len(string)-4:len(string)])
	test1='bvwbjplbgvbhsrlpgdmjqwftvncz'
	test2='nppdvjthqldpwncqszvftbrmjlhg'
	#print(len(string))
	print(part_1(string))
	
		
main()