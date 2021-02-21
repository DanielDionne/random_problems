# 1277. Count Square Submatrices with All Ones
# https://leetcode.com/problems/count-square-submatrices-with-all-ones/

# 600 ms, faster than 33.71%
# 22.1 MB, less than 5.10% 

class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        '''
        dp[x,y] = num squares that have x,y as bottom right corner (which coincides with max size)
        dp[x,y] = 
            if matrix[x,y] == 1: min(dp[x-1,y], dp[x,y-1], dp[x-1,y-1]) + 1
            else 0
        '''
        
        width = len(matrix[0])
        height = len(matrix)
        
        result = 0
        dp = {}
        for y in range(height):
            for x in range(width):
                if matrix[y][x] == 1:
                    numSquares = min(dp.get((x,y-1),0), dp.get((x-1,y),0), dp.get((x-1,y-1),0)) + 1
                    dp[(x,y)] = numSquares
                    result += numSquares
        return result
