# 16. 3Sum Closest
# https://leetcode.com/problems/3sum-closest/submissions/

# 104 ms, faster than 53.71%
# 13.6 MB, less than 23.41%

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        '''
        Fix one number, do 2sum with the other two
        '''
        nums.sort()
        result = float('inf')
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            while j < k:
                s = nums[i]+nums[j]+nums[k]
                if abs(target - s) < abs(target - result):
                    result = s
                if s == target:
                    return target
                elif s < target:
                    j += 1
                else:
                    k -= 1
        return result

sol = Solution()
# result = sol.threeSumClosest([-1,2,1,-4], 1) # 2
result = sol.threeSumClosest([0,2,1,-3], 1) # 0
print(result)
