# 1043. Partition Array for Maximum Sum
# https://leetcode.com/problems/partition-array-for-maximum-sum/

# 400 ms, faster than 65.39%
# 13.3 MB, less than 91.35%

class Solution(object):
    def maxSumAfterPartitioning(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """

        '''
        
        1,4,1,5,7,3,6,1,9,9,3
        4 4 7 7 7 9 9 9 9 9 9
          ^     ^       ^
        at every number, I can decide to partition or not
        every partition is just going to take the maximum value contained in it and extend it
                           
        '''
        
        dp = [0]*(len(arr)+1)
        for i in range(1,len(arr)+1):
            result = 0
            m = 0
            for w in range(1,k+1):
                partition_start = i-w
                if partition_start < 0:
                    break
                m = max(m, arr[partition_start])
                sum_with_partition = dp[partition_start] + m*w
                result = max(result, sum_with_partition)
            dp[i] = result
        return dp[-1]