# 213. House Robber II
# https://leetcode.com/problems/house-robber-ii/

# 20 ms, faster than 66.39%
# 13.3 MB, less than 72.49%

class Solution(object):
    def rob_1(self, nums):
        a = nums[0]
        b = max(nums[0],nums[1])
        for x in nums[2:]:
            a,b = b,max(b, a + x)
        return b
    
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        '''
        Since we can't pick the first and last, pick only one of them, return the max of both scenarios
        '''
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0],nums[1])
        return max(self.rob_1(nums[1:]), self.rob_1(nums[:len(nums)-1]))
