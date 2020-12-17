# Problem: Longest Common Subsequence
# Link: https://www.geeksforgeeks.org/longest-common-subsequence-dp-4/

class LCS:
	def compute(self, a, b):
		m = len(a)
		n = len(b)
		M = [0 for x in range(n+1)]
		for i in range(1, m+1):
			for j in range(1, n+1):
				if a[i-1] == b[j-1]:
					M[j] = M[j-1] + 1
				else:
					M[j] = max(M[j], M[j-1])
		return M[n]

def main():
	X = "AGGTAB"
	Y = "GXTXAYB"
	print "Length of LCS is ", LCS().compute(X, Y)

if __name__ == '__main__':
	main()
