#Problem: Pascal Triangle II
#Link: https://leetcode.com/problems/pascals-triangle-ii

class Solution:
    def getRow(self, rowIndex):
        n = rowIndex + 1
        M = [[1 for j in range(n)] for i in range(2)]
        for i in range(n):
            bi = i & 1
            for j in range(1, i):
                M[bi][j] = M[1-bi][j] + M[1-bi][j-1]
        return M[bi][0:n]

def main():
    rowIndex = 5
    L = Solution().getRow(rowIndex)
    print 'L = ', L

if __name__ == '__main__':
    main()