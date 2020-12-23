#Problem: Find First and Last Position of Element in Sorted Array
#Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums == None or len(nums) == 0:
            return [-1,-1]
        posLeft = self.getLeftPosition(nums, target)

        if posLeft == -1:
            return [-1, -1]
                
		posRight = self.getRightPosition(nums, target)
        
        return [posLeft, posRight]

    def getLeftPosition(self, nums: List[int], target: int):
    	posLeft, i, j = -1, 0, len(nums)-1
        while i<=j:
            m = (i+j)//2
            if nums[m] == target:
                if m-1 >= i and nums[m-1] == target:
                    j = m-1
                else:
                    posLeft = m
                    break
            elif target > nums[m]:
                i = m+1
            else:
                j = m-1
        return posLeft

    def getRightPosition(self, nums: List[int], target: int):
    	posRight,i,j = -1,0,len(nums)-1
        while i<=j:
            m = (i+j)//2
            if nums[m] == target:
                if m+1 <= j and nums[m+1] == target:
                    i = m+1
                else:
                    posRight = m
                    break
            elif target > nums[m]:
                i = m+1
            else:
                j = m-1
        return posRight




