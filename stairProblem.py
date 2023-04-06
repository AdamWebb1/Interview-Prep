
def count_ways_to_climb_stairs(n):
	if n < 0:
		return 0
	elif n < 3:
		return n
	else:
		memo = [0] * (n+1)
		memo[0] = 1
		memo[1] = 1
		memo[2] = 2
		for i in range(3, n+1):
			memo[i] = memo[i-1] + memo[i-2] + memo[i-3]
		return memo[n]


for i in range(10):
	print(i, count_ways_to_climb_stairs(i))