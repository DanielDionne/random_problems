# 18. 4Sum
# https://leetcode.com/problems/4sum/

# 836 ms, faster than 47.34%
# 17.1 MB, less than 9.47%

class Solution(object):
    def twoSum(self, nums, target, cache):
        key = (len(nums),target)
        if key in cache:
            return cache[key]
        # nums is already sorted
        result = []
        i = 0
        j = len(nums)-1
        while i < j:
            s = nums[i] + nums[j]
            if s == target:
                result.append((i,j))
                i+=1
                j-=1
            elif s < target:
                i+=1
            else:
                j-=1
        cache[key] = result
        return result
            
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        '''
        iterate on two pointers, do 2sum to find the other two numbers (could be more than one pair!):
        [_______________]
          ^  ^
          i  j[  2sum  ]
        '''
        nums.sort()
        result = set()
        cache = {}
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                firstTwoSum = nums[i] + nums[j]
                lastTwoIndicesPairs = self.twoSum(nums[j+1:], target-firstTwoSum, cache)
                for lastTwoIndices in lastTwoIndicesPairs:
                    a,b = lastTwoIndices
                    result.add((nums[i],nums[j],nums[a+j+1],nums[b+j+1]))
        return result