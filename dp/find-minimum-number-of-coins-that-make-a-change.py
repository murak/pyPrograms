#Problem: Minimum number of coins
#Link: https://www.geeksforgeeks.org/find-minimum-number-of-coins-that-make-a-change/

import sys

class Solution:
	def minCoins(self, coins, target):
		n = len(coins)
		if target == 0:
			return 0
		M = [sys.maxsize-100 for i in range(target+1)]
		M[0] = 0
		for i in range(1, n+1):
			for j in range(target+1):
				if coins[i-1] <= j:
					M[j] = min(1+M[j-coins[i-1]], M[j])
		return M[target]

def main():
	coins = [9, 6, 5, 1] 
	V = 11
	print 'answer = ', Solution().minCoins(coins, V)

if __name__ == '__main__':
	main()
