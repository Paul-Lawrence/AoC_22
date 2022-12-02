import requests
import numpy as np


def main():
	fname='day_1.txt'
	data = open(fname, 'r')
	lines = data.readlines()
	lines = [line.strip() for line in lines]
	part_2(lines)


def part_1(lines):
	nums=[]
	tot=0
	for line in lines:
		if (line==''):
			nums.append(tot)
			tot=0
		else:
			tot+=int(line)
	print(max(nums))
	
def part_2(lines):
	nums=[]
	tot=0
	for line in lines:
		if (line==''):
			nums.append(tot)
			tot=0
		else:
			tot+=int(line)
	nums=np.sort(nums)
	print(nums[-1]+nums[-2]+nums[-3])
	
main()