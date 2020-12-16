# Problem: KnapSack
# Link: https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/

class Knapsack01:
	def knapsack(self, C, w, v, n):
		M = [[0 for x in range(C+1)] for x in range(n+1)]
		for i in range(1, n+1):
			for j in range(1, C+1):
				if w[i-1] <= j:
					M[i][j] = max(v[i-1] + M[i-1][j-w[i-1]], M[i-1][j])
				else:
					M[i][j] = M[i-1][j]
		return M[n][C]

def main():
	val = [60, 100, 120] 
	wt = [10, 20, 30] 
	C = 50
	k = Knapsack01()
	profit = k.knapsack(C, wt, val, len(val))
	print "profile = ", profit

if __name__ == "__main__":
	main()