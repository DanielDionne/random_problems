# 78. Subsets
# https://leetcode.com/problems/subsets/

# 24 ms, faster than 49.31%
# 13.7 MB, less than 49.82%

class Solution(object):
    def subsets_rec(self, nums, current, result):
        if not nums:
            result.append(current[::])
            return
        current.append(nums[0])
        self.subsets_rec(nums[1:], current, result)
        current.pop()
        self.subsets_rec(nums[1:], current, result)
            
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.subsets_rec(nums, [], result)
        return result
        