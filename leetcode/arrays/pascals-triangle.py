#Problem: Pascal Triangle
#Link: https://leetcode.com/problems/pascals-triangle

class Solution:
    def generate(self, numRows):
        n = numRows
        M = [[1 for j in range(i)] for i in range(1, n+1)]
        for i in range(n):
            for j in range(1, i):
                M[i][j] = M[i-1][j] + M[i-1][j-1]
        return M

def main():
    numRows = 5
    M = Solution().generate(numRows)
    print M

if __name__ == '__main__':
    main()