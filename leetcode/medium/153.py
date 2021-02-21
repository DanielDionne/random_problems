# 153. Find Minimum in Rotated Sorted Array
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

# 28 ms, faster than 61.57%
# 13.8 MB, less than 9.29%

class Solution(object):

    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                return nums[i+1]
        return nums[0]
    
    
    # For some reason, this is practically slower than linear
    def findMin_binary_search(self, nums):
        left = 0
        right = len(nums)-1
        while left < right:
            m = left + (right-left)/2
            if nums[m] > nums[right]:
                left = m + 1
            else:
                right = m
        return nums[left]
