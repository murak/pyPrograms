#Problem: Search and return insert position in sorted array
#Link: https://leetcode.com/problems/search-insert-position/submissions/

class Solution:

    def efficientSearchInsert(self, nums, target):
        if nums is None:
            return 0
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if target == nums[m]:
                return m
            elif target > nums[m]:
                i = m+1 
            else:
                j = m-1
        return i

    def searchInsert(self, nums, target):
        if nums is None:
            return 0
        i, j = 0, len(nums) - 1
        m = 0
        while i <= j:
            m = (i + j) // 2
            if target == nums[m]:
                return m
            elif target > nums[m]:
                if m+1 >= len(nums):
                    return m+1
                elif target < nums[m+1]:
                    return m+1
                else:
                    i = m+1
            else:
                if m-1 < 0:
                    return 0
                elif target > nums[m-1]:
                    return m
                else:
                    j = m-1
        return m

def main():
    nums = [2,4,6,8,10]
    s = Solution()

    for target in range(12):
        print 'for ', nums, 'insert ', target, ' at position = ', s.searchInsert(nums, target)

    print '\n#### Efficient Algorithm'

    for target in range(12):
        print 'for ', nums, 'insert ', target, ' at position = ', s.efficientSearchInsert(nums, target)


if __name__ == '__main__':
    main()