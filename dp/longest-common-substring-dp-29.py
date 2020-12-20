#Problem: Longest common substring
#Link: https://www.geeksforgeeks.org/longest-common-substring-dp-29/

class Solution:
	def compute(self, A, B):
		m = len(A)
		n = len(B)
		if (m == 0 or n == 0):
			return 0
		M = [[0 for x in range(n+1)] for y in range(2)]
		largest = M[0][0]
		for i in range(1, m+1):
			bi = i&1
			for j in range(1, n+1):
				if A[i-1] == B[j-1]:
					M[bi][j] = 1+M[1-bi][j-1]
					largest = max(largest, M[bi][j])
				else:
					M[bi][j] = 0
		return largest

def main():
	X = 'OldSite:GeeksforGeeks.org'
	Y = 'NewSite:GeeksQuiz.com'
  
	m = len(X) 
	n = len(Y)

	print 'Length of Longest Common Substring is', Solution().compute(X, Y) 

if __name__ == '__main__':
	main()
