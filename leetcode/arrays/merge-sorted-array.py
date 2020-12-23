#Problem: Merge two sorted array into given original array
#Link: https://leetcode.com/problems/merge-sorted-array/submissions/

class Solution:
    def merge(self, nums1, m, nums2, n):
        if n == 0:
            return
        i = m+n-1
        x = m-1
        y = n-1
        while x >= 0 and y >= 0:
            if nums1[x] > nums2[y]:
                nums1[i] = nums1[x]
                x -= 1
            else:
                nums1[i] = nums2[y]
                y -= 1
            i -= 1
        
        while x >= 0:
            nums1[i] = nums1[x]
            i -= 1
            x -= 1
        
        while y >= 0:
            nums1[i] = nums2[y]
            i -= 1
            y -= 1
        return nums1

def main():
    nums1 = [1,2,3,0,0,0,0]
    nums2 = [3,4,5,6]
    m = 3
    n = 4
    Solution().merge(nums1, m, nums2, n)
    print 'final merged array = ', nums1

if __name__ == '__main__':
    main()