# 96. Unique Binary Search Trees
# https://leetcode.com/problems/unique-binary-search-trees/

# 16 ms, faster than 77.02%
# 13.4 MB, less than 38.77%

class Solution(object):
    def numTreesRec(self, n, cache):
        if n in cache:
            return cache[n]
        if n <= 1:
            return 1
        result = 0
        for i in range(1,n+1):
            result += self.numTreesRec(i-1,cache) * self.numTreesRec(n-i,cache)
        cache[n] = result
        return result
    
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.numTreesRec(n,{})
