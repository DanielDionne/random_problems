# https://leetcode.com/problems/maximum-subarray/

# 56 ms, faster than 27.15%
# 14.3 MB, less than 53.30%

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = -float('inf')
        m = -float('inf')
        for n in nums:
            c = max(n, c+n)
            m = max(c,m)
        return m

sol = Solution()
print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))