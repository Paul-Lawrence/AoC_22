import ast 
import re

def part_1(nums):
	return -1
	
def main():
	grid=[list(d.replace('\n','')) for d in open('day_22.txt','r').readlines()]
	print(grid)
	d={" ":0,'.':1,'#':-1}
	path = ''.join(map(str, grid.pop()))
	grid.pop()
	grid=[[d[x] for x in y] for y in grid]
	print(grid)
	#print(path)
	nums=[int(n) for n in map(int, re.findall(r'\d+', path))]
	print(nums)
	print(next((i for i, v in enumerate(grid[0]) if v != 0), -1))
	print(grid[0])
	print(len(grid[0])-1-next((i for i, v in enumerate(reversed(grid[0])) if v != 0), -1))
	#nums=[int(line.strip()) for line in open('day_20.txt', 'r').readlines()]
	#print([n.value for n in nums])
	#test=[1,2,-3,3,-2,0,4]
	#for i in range(len(test)):
	#	test[i]=coord(test[i],i)
	#print(part_2(test))
	#cheat=[int(x.strip()) for x in open('day_20.txt','r').readlines()]
	#ch(nums)
	
	
main()