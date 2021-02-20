# 129. Sum Root to Leaf Numbers
# https://leetcode.com/problems/sum-root-to-leaf-numbers/

# 24 ms, faster than 41.25%
# 13.5 MB, less than 99.83%

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbersRec(self, root, current):
        if not root:
            return 0
        current = current * 10 + root.val
        if not root.left and not root.right:
            return current
        return self.sumNumbersRec(root.left, current) + self.sumNumbersRec(root.right, current)
            
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        return self.sumNumbersRec(root, 0)