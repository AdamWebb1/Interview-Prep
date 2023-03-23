from math import floor
import time

n = 1000

solutions = ""

startTime = time.time()
maxPossibleThrees = floor(n/3)
for numThrees in range(0, maxPossibleThrees+1):
	maxPossibleTwos = floor((n-numThrees*3)/2)
	for numTwos in range(0, maxPossibleTwos+1):
		maxPossibleOnes = floor((n-numThrees*3-numTwos*2))
		for numOnes in range(0, maxPossibleOnes+1):
			if (numOnes*1+numTwos*2+numThrees*3) == n:
				solutions += f"3:{numThrees}, 2:{numTwos}, 1:{numOnes},\n"
				
print(solutions)				
solutions = (solutions.count(",")/3)		
print(f"Found {solutions} solutions")
print(f"Algorithm finished in {time.time()-startTime} seconds.")

