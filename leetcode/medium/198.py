# 198. House Robber
# https://leetcode.com/problems/house-robber/

# 20 ms, faster than 62.86%
# 13.3 MB, less than 72.10%

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:    
            a = nums[0]
            b = max(nums[0],nums[1])
            for x in nums[2:]:
                a,b = b,max(b, a + x)
            return b