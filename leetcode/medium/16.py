# 16. 3Sum Closest
# https://leetcode.com/problems/3sum-closest/

# 2260 ms, faster than 5.03%
# 13.4 MB, less than 78.69%

class Solution(object):
    def findClosest(self, nums, target):
        if not nums:
            return None
        # binary search of closest element
        left = 0
        right = len(nums)-1
        while left <= right:
            m = left + (right-left)/2
            if target == nums[m]:
                return nums[m]
            elif target < nums[m]:
                right = m-1
            else:
                left = m+1
        if left >= len(nums) or abs(target-nums[left]) > abs(target-nums[right]):
            return nums[right]
        else:
            return nums[left]

    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        '''
        sort
        for every pair, bin-search for complementary
        
        '''
        
        nums.sort()
        best = None
        s = float('inf')
        for i in range(len(nums)-1):
            a = nums[i]
            for j in range(i+1, len(nums)):
                b = nums[j]
                c = self.findClosest(nums[j+1:], target-(a+b))
                # print('findClosest to {} is {}'.format(-(a+b),c))
                if c is not None:
                    new_s = a+b+c
                    if abs(new_s-target) < abs(s-target):
                        # print(a,b,c)
                        s = new_s
        return s

sol = Solution()
# result = sol.threeSumClosest([1,1,-1,-1,3],-1)
result = sol.threeSumClosest([-1,2,1,-4],1)
print(result)