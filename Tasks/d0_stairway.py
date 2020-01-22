from typing import Union, Sequence


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
	"""
	Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

	:param stairway: list of ints, where each int is a cost of appropriate step
	:return: minimal cost of getting to the top
	"""

	#straightforward method
	#stairway = [1, 3, 1, 5, 2, 7, 7, 8, 9, 4, 6, 3]
	stairway_sum = [0]*len(stairway)
	stairway_sum[0] = stairway[0]
	stairway_sum[1] = stairway[1]
	print(stairway_sum)
	for i in range(2, len(stairway)):
		stairway_sum[i] = stairway[i] + min(stairway_sum[i-1], stairway_sum[i-2])

	print(stairway_sum)
	return stairway_sum[-1]

'''
# reversed method
#stairway = [1, 3, 1, 5, 2, 7, 7, 8, 9, 4, 6, 3]
stairway_sum = [999] * len(stairway)
stairway_sum[0] = stairway[0]
stairway_sum[1] = stairway[1]

for i in range(len(stairway)):
	if i + 1 < len(stairway) and stairway_sum[i+1] > stairway_sum[i] + stairway[i+1]:
		stairway_sum[i+1] = stairway_sum[i] + stairway[i+1]
	if i + 2 < len(stairway) and stairway_sum[i+2] > stairway_sum[i] + stairway[i+2]:
		stairway_sum[i+2] = stairway_sum[i] + stairway[i+2]
print(stairway_sum)

return stairway_sum[-1]
'''
'''
#lazy method
stairway = [1, 3, 1, 5, 2, 7, 7, 8, 9, 4, 6, 3]
stairway_sum = [0]*len(stairway)

def lazy(n) -> int:
if n - 1 < 0:
	return stairway[n]
if n - 2 < 0:
	return stairway[n]
if stairway_sum[n] == 0:
	stairway_sum[n] = stairway[n] + min(lazy(n-1), lazy(n-2))
return stairway_sum[n]

print(lazy(len(stairway) - 1))
'''


if __name__ == "__main__":
	test_st = [1, 3, 1, 5, 2, 7, 7, 8, 9, 4, 6, 3]
	print(stairway_path(test_st))