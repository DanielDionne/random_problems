# https://leetcode.com/problems/move-zeroes/

# 44 ms, faster than 37.92%
# 14.4 MB, less than 74.17%

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        z = 0
        while i < len(nums) and z < len(nums):
            # update indices
            while z < len(nums) and nums[z] != 0:
                z += 1
            i = max(z,i)
            while i < len(nums) and nums[i] == 0:
                i += 1
            # swap
            if i < len(nums) and z < len(nums):
                nums[i],nums[z] = nums[z],nums[i]

sol = Solution()
nums = [0,1,0,3,12]
sol.moveZeroes(nums)
print(nums)