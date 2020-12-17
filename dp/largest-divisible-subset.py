# problem: Largest Divisible Subset
# Link: https://leetcode.com/problems/largest-divisible-subset/

class LDS:
	def largestDivisibleSubset(self, nums):
		res = []
		if nums == None:
			return res
		n = len(nums)
		if n <= 1:
			return nums

		nums.sort()

		dp = [(1, -1)] * n # (val, previous index)
		maxVal, maxIndex = 1, -1
		for i in range(1, n):
			for j in range(0, i):
				if nums[i]%nums[j] == 0:
					if dp[j][0] + 1 > dp[i][0]:
						dp[i] = (dp[j][0] + 1, j)
			if dp[i][0] > maxVal:
				maxVal, maxIndex = dp[i][0], i

		print('maxval = ', maxVal, ' maxIndex = ', maxIndex)
		print(dp)

		while maxIndex != -1:
			res.insert(0, nums[maxIndex])
			maxIndex = dp[maxIndex][1]

		# If result is empty add any element from the array since every element is divisible by itself
		if len(res) == 0:
			res.append(nums[0])

		return res

def main():
	nums = [1,2,3,4,5,6,7,8,9,13,17,66,16]
	print 'result = ', LDS().largestDivisibleSubset(nums)

if __name__ == '__main__':
	main()
