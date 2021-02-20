# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
'''

Iterate right to left, keep track of max value, compare to current
'''
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        highest = -float('inf')
        result = 0
        for i in reversed(prices):
            if i > highest:
                highest = i
            if highest - i > result:
                result = highest - i
        return result

sol =Solution()
# r = sol.maxProfit([7,1,5,3,6,4])
r = sol.maxProfit([7,6,4,3,1])
print(r)