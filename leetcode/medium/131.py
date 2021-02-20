# 131. Palindrome Partitioning
# https://leetcode.com/problems/palindrome-partitioning/

# 580 ms, faster than 94.59%
# 27.3 MB, less than 85.88%

'''
In general, all possible partitions up to letter i =
  - all possible partitions up to letter i - j, plus word[j...i] if it's a palindrome

abbababa + b
abbaba + bab
abba + babab
ab + bababab

Keep a cache of arrays that represents all possible partitions up to a letter i
'''

class Solution(object):
    def palindrome(self, s):
        if len(s) == 1:
            return True
        left = 0
        right = len(s)-1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        dp = [[[s[0]]]] # base case, just the first letter
        for i in range(1,len(s)):
            result = []
            for j in range(0,i+1):
                rightmostWord = s[j:i+1]
                if self.palindrome(rightmostWord):
                    if j >= 1:
                        for partition in dp[j-1]:
                            result.append(partition + [rightmostWord])
                    else:
                        result.append([rightmostWord])
            dp.append(result)
        return dp[-1]
        
sol = Solution()
result = sol.partition('abbababab')
# result = sol.partition('abba')
print(result)