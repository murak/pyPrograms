# Problem: Longest Increasing Subsequence
# Link: https://www.geeksforgeeks.org/longest-increasing-subsequence-dp-3/

class LIS:
	def compute(self, s):
		if s == None or len(s) == 0:
			return 0
		n = len(s)
		M = [0 for x in range(n+1)]
		for i in range(1, n+1):
			for j in range(1, n+1):
				if j>i and s[j-1] >= s[i-1]:
					M[j] = M[j-1] + 1
		return M[n]

def main():
	arr = [10, 22, 9, 33, 21, 50, 41, 60] 
	print "Length of lis is", LIS().compute(arr)

if __name__ == '__main__':
	main()
