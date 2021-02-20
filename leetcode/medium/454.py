# 454. 4Sum II
# https://leetcode.com/problems/4sum-ii/

# 424 ms, faster than 26.40%
# 39.8 MB, less than 38.95%

from collections import Counter
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        '''
        Calculate and store all possible combinations of A and B
        Then for every pair of C and D, check if the complementary exists in the stored table
        '''
        result = 0
        
        ab = Counter()
        for a in A:
            for b in B:
                ab[a+b] += 1
        
        for c in C:
            for d in D:
                result += ab[-(c+d)]

        return result