# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

# 12 ms, faster than 94.56%
# 13.3 MB, less than 66.65%

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n < 2:
            return 1
        
        '''
        Look for a pair where there is a good version followed by a bad version
        '''
        left = 0
        right = n
        while True:
            m = left + (right-left)/2
            bad_m = isBadVersion(m)
            bad_next = m+1 >= n or isBadVersion(m+1)
            if bad_next and not bad_m:
                return m+1
            elif bad_m:
                right = m-1
            else:
                left = m+1
