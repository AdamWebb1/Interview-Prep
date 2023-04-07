

def count_ways_to_climb_stairs(n):
	# You can't climb zero steps
	if n < 0:
		return 0

	# We already know these
	elif n < 3:
		return n

	else:
		# Just some setup with the existing solutions
		solutions = [0] * (n+1)
		solutions[0] = 1
		solutions[1] = 1
		solutions[2] = 2
		for i in range(3, n+1):
			# The child must have come from one of the previous 3 steps,
			# so you each of the three previous steps is a possible solution
			solutions[i] = solutions[i-1] + solutions[i-2] + solutions[i-3]
		return solutions[n]


def main():
	assert count_ways_to_climb_stairs(1) == 1
	assert count_ways_to_climb_stairs(2) == 2
	assert count_ways_to_climb_stairs(3) == 4
	assert count_ways_to_climb_stairs(4) == 7
	assert count_ways_to_climb_stairs(5) == 13
	assert count_ways_to_climb_stairs(6) == 24
	assert count_ways_to_climb_stairs(7) == 44
	assert count_ways_to_climb_stairs(8) == 81
	assert count_ways_to_climb_stairs(9) == 149
	assert count_ways_to_climb_stairs(10) == 274

	assert count_ways_to_climb_stairs(0) == 0

	assert count_ways_to_climb_stairs(-1) == 0

	print('All tests passed!')

if __name__ == '__main__':
	main()