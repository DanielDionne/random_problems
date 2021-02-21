# 1277. Count Square Submatrices with All Ones
# https://leetcode.com/problems/count-square-submatrices-with-all-ones/

# 528 ms, faster than 74.22%
# 15.9 MB, less than 12.18%

# Slightly faster when using a matrix for dp instead of a hash table

class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        '''
        dp[x,y] = num squares that have x,y as bottom right corner (which coincides with max size)
        dp[x,y] = 
            if matrix[x,y] == 1: min(dp[x-1,y], dp[x,y-1])+1 # don't forget to check opposite corner
            else 0
        '''
        
        width = len(matrix[0])
        height = len(matrix)
        
        result = 0
        dp = [[0]*width for _ in range(height)]
        for y in range(height):
            for x in range(width):
                if x == 0 or y == 0:
                    dp[y][x] = matrix[y][x]
                    result += matrix[y][x]
                elif matrix[y][x] == 1:
                    numSquaresAdj = min(dp[y-1][x], dp[y][x-1], dp[y-1][x-1])+1
                    dp[y][x] = numSquaresAdj
                    result += numSquaresAdj
        return result