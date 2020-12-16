# Knapsack problem variation
# Problem: https://www.geeksforgeeks.org/subset-sum-problem-dp-25/

class SubsetSumProblem:
	def isSubsetPresent(self, arr, sum):
		n = len(arr)
		M = [[False for x in range(sum+1)] for x in range(n+1)]
		for i in range(n+1):
			for j in range(sum+1):
				if j == 0:
					M[i][j] = True
				elif i == 0:
					M[i][j] = False
				elif arr[i-1] <= j:
					M[i][j] = M[i-1][j-arr[i-1]] or M[i-1][j]
				else:
					M[i][j] = M[i-1][j]
		return M[n][sum]

def main():
	set = [3, 34, 4, 12, 5, 2]
	sum = 26
	problem = SubsetSumProblem()
	print problem.isSubsetPresent(set, sum)

if __name__ == '__main__':
	main()

