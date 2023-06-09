import sys
from collections import deque

table_dna = [['A', 'C', 'A', 'G'],
             ['C', 'G', 'T', 'A'],
             ['A', 'T', 'C', 'G'],
             ['G', 'A', 'G', 'T']]


N = int(sys.stdin.readline())
DNA = deque(sys.stdin.readline().rstrip())

while len(DNA) > 1:
	ele_dna = []
	for _ in range(2):
		if DNA[-1] == 'A':
			ele_dna += '0'
		elif DNA[-1] == 'G':
			ele_dna += '1'
		elif DNA[-1] == 'C':
			ele_dna += '2'
		elif DNA[-1] == 'T':
			ele_dna += '3'
		DNA.pop()

	cnv_dna = table_dna[int(ele_dna[0])][int(ele_dna[1])]
	DNA.append(cnv_dna)

print(DNA[0])
