# Problem: Number of Longest Increasing Subsequence
# Link: https://leetcode.com/problems/number-of-longest-increasing-subsequence/

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if nums == None:
            return 0
        n = len(nums)
        if n == 0 or n == 1:
            return n
        
        length = [1 for x in range(n)]
        count = [1 for x in range(n)]
        maxVal = length[0]
        sum = count[0]
        for i in range(1, n):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    if length[j]+1 > length[i]:
                        length[i] = length[j] + 1
                        count[i] = count[j]
                    elif length[j]+1 == length[i]:
                        count[i] += count[j]
            if length[i] > maxVal:
                maxVal = length[i]
                sum = count[i]
            elif length[i] == maxVal:
                sum += count[i]
            #print('length in iteration ', i, 'is ', length, ' and count = ', count)
        #print('maxVal = ', maxVal)
        
        return sum