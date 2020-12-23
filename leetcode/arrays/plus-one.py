#Problem: Plus one from Leetcode
#Link: https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits):
        n = len(digits)
        for i in range(n):
            if digits[n-1-i]+1 <= 9:
                digits[n-1-i] = digits[n-1-i]+1
                return digits
            digits[n-1-i] = 0
        digits.insert(0, 1)
        return digits

def main():
    digits = [9,9,9]
    print 'answer for ', digits, ' + 1 = ', Solution().plusOne(digits)


if __name__ == '__main__':
    main()