#Problem: Maximum sum sub-array
#Link: https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums):
        if nums == None:
            return 0
        prevSum, maxSum = nums[0], nums[0]
        for i in range(1, len(nums)):
            if prevSum < 0:
                prevSum = 0
            prevSum += nums[i]
            maxSum = max(maxSum, prevSum)
        return maxSum

def main():
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print 'maximum sum of sub array = ', Solution().maxSubArray(nums)

if __name__ == '__main__':
    main()
