#Problem: Buy and sell stocks I
#Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution:
    def maxProfit(self, prices):
        if prices is None:
            return 0
        minimum = prices[0]
        profit = 0
        
        for i in range(1, len(prices)):
            if prices[i] - minimum > profit:
                profit = prices[i] - minimum
            minimum = min(minimum,prices[i])
        return profit

def main():
    prices = [7,1,5,3,6,4]
    profit = Solution().maxProfit(prices)
    print 'profit = ', profit

if __name__ == '__main__':
    main()