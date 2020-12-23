#Problem: Remove element from an array
#Link: https://leetcode.com/problems/remove-element/

class Solution:
    def removeElement(self, nums, val):
        if nums is None:
            return 0
        ref, fwd = -1, 0
        for fwd in range(len(nums)):
            if nums[fwd] == val:
                fwd += 1
            else:
                ref += 1
                nums[ref] = nums[fwd]
                fwd += 1
        return ref+1

def main():
    nums = [1,2,1,3,2,1]
    val = 1
    length = Solution().removeElement(nums, val)
    print 'final array: ', nums[:length]

if __name__ == '__main__':
    main()