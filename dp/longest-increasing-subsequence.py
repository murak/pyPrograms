# Problem: Longest Increasing Subsequence
# Link: https://www.geeksforgeeks.org/longest-increasing-subsequence-dp-3/

class LIS:
	def compute(self, s):
		if s == None or len(s) == 0:
			return 0
		n = len(s)
		M = [1 for x in range(n+1)]
		for i in range(1, n+1):
			for j in range(i+1, n+1):
				if s[j-1] >= s[i-1]:
					M[j] = max(M[i] + 1, M[j])
			print M
		
		largest = M[0]
		for i in range(1, n+1):
			largest = max(largest, M[i])
		return largest



def main():
	arr = [10, 22, 9, 3, 21, 10, 1, 0] 
	print "Length of lis is", LIS().compute(arr)

if __name__ == '__main__':
	main()
