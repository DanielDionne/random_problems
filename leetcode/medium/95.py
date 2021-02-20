# 95. Unique Binary Search Trees II
# https://leetcode.com/problems/unique-binary-search-trees-ii/

# 36 ms, faster than 100.00%
# 14.6 MB, less than 92.18%

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.generateTreesRec(1, n, {})
    
    def generateTreesRec(self, start, end, cache):
        cached = cache.get((start,end), None)
        if cached:
            return cached
        if end < start:
            return [None]
        if start == end:
            return [TreeNode(start)]
        result = []
        for i in range(start,end+1):
            # left subtrees
            leftTrees = self.generateTreesRec(start, i-1, cache)
            # right subtrees
            rightTrees = self.generateTreesRec(i+1, end, cache)
            # combine all options
            for leftTree in leftTrees:
                for rightTree in rightTrees:
                    result.append(TreeNode(i, leftTree, rightTree))
        cache[(start,end)] = result
        return result
