# 90. Subsets II
# https://leetcode.com/problems/subsets-ii/

# 24 ms, faster than 76.89%
# 13.7 MB, less than 52.04%

class Solution(object):
    def subsets_rec(self, nums, current, result):
        if not nums:
            result.append(current[::])
            return
        current.append(nums[0])
        self.subsets_rec(nums[1:], current, result)
        current.pop()
        self.subsets_rec(nums[1:], current, result)
    
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.subsets_rec(nums, [], result)
        return set(map(tuple,map(sorted,result)))
        
        