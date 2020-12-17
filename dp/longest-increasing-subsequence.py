# Problem: Longest Increasing Subsequence
# Link: https://www.geeksforgeeks.org/longest-increasing-subsequence-dp-3/

class LIS:
	def computeN2Solution(self, A):
		if A == None:
			return 0
		n = len(A)
		if (n <= 1):
			return n
		dp = [1] * n
		lis = dp[0]
		for i in range(1, n):
			for j in range(0,i):
				if A[i] >= A[j]:
					dp[i] = max(dp[i], dp[j]+1)
			# print dp
			lis = max(lis, dp[i])
		return lis

	def computeNlogNSolution(self, A):
		if A == None:
			return 0
		n = len(A)
		if n <= 1:
			return n
		tail = [0] * n
		seq = [-1] * n
		size = 0
		for num in A:
			i, j = 0, size
			while i<j:
				m = (i+j)//2
				if tail[m] < num:
					i = m+1
				else:
					j = m
			tail[i] = num
			if i == size or i == size-1:
				seq[i] = num
			size = max(size, i+1)
		print "sequence of lis: ", seq
		return size


def main():
	arr = [10, 1, 9, 3, 21, 10, 2, 20] 
	print "Length of lis using DP in N^2 complexity is: ", LIS().computeN2Solution(arr)
	print "Length of lis using DP & binary search in n(lg n) complexity is: ", LIS().computeNlogNSolution(arr)

if __name__ == '__main__':
	main()
