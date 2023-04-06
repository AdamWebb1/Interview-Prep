
import math

def count_ways_to_climb_stairs(n):
	# You can't climb zero steps
	if n < 0:
		return 0

	# We already know these
	elif n < 3:
		return n

	else:
		# Just some setup with the existing solutions
		memo = [0] * (n+1)
		memo[0] = 1
		memo[1] = 1
		memo[2] = 2
		for i in range(3, n+1):
			# The child must have come from one of the previous 3 steps,
			# so you each of the three previous steps is a possible solution
			memo[i] = memo[i-1] + memo[i-2] + memo[i-3]
		return memo[n]

solutions = "i, solutions, e^i\n"

for i in range(10):
	solution = count_ways_to_climb_stairs(i)
	print(i, solution)
	solutions += (f"{i}, {solution}, {math.e**i}\n")

with open("data.csv", "w") as f:
	f.write(solutions)