# Problem: Rod cutting problem
# Link: https://www.geeksforgeeks.org/cutting-a-rod-dp-13/

class Solution:
	def cutRod(self, price, n):
		if n <= 0:
			return 0
		l = [i for i in range(1, n+1)]
		M = [0 for i in range(0, n+1)]

		print('l = ', l)
		print('M = ', M)
		for i in range(n):
			for j in range(1, n+1):
				if j <= l[i]:
					M[j] = max(M[j], price[i] + M[j-l[i]])
			print(M)
		return M[n]

def main():
	arr = [1, 5, 8, 9, 10, 15, 11, 20] 
	size = len(arr) 
	print "Maximum Obtainable Value is", Solution().cutRod(arr, size) 

if __name__ == '__main__':
	main()