# 112. Path Sum
# https://leetcode.com/problems/path-sum/

# 24 ms, faster than 98.49%
# 17 MB, less than 39.84%

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSumRec(self, root, targetSum):
        if not root:
            return False
        if not root.left and not root.right and targetSum == root.val:
            return True
        return self.hasPathSumRec(root.left, targetSum - root.val) or self.hasPathSumRec(root.right, targetSum - root.val)
    
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        return self.hasPathSumRec(root, targetSum)
        