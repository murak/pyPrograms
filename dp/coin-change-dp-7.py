# Problem: Maximum ways we can make change from given set of coins
# Link: https://www.geeksforgeeks.org/coin-change-dp-7/

class Solution:
	def maxWays(self, coins, target):
		if target == 0:
			return 1
		n = len(coins)
		M = [0 for i in range(target+1)]
		M[0] = 1

		for i in range(1,n+1):
			for j in range(coins[i-1], target+1):
					M[j] = M[j-coins[i-1]] + M[j]
		return M[target]

def main():
	arr = [1,2,3] 
	m = len(arr) 
	print(Solution().maxWays(arr, 4))

if __name__ == '__main__':
	main()
