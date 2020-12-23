#Problem: Remove duplicates from sorted array
#Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/submissions/

class Solution:
    def removeDuplicates(self, nums):
        if nums is None:
            return 0
        elif len(nums) <= 1:
            return len(nums)
        
        ref, forward = 0, 1
        for forward in range(1, len(nums)):
            if nums[ref] == nums[forward]:
                forward += 1
            else:
                ref += 1
                nums[ref] = nums[forward]
                forward += 1
        return ref+1

def main():
    nums = [1,2,3,4,4,4,5,5,5,6,6,6,7,7,7,8]
    length = Solution().removeDuplicates(nums)
    print 'final array:', nums[:length]


if __name__ == "__main__":
    main()