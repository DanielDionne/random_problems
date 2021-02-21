# 113. Path Sum II
# https://leetcode.com/problems/path-sum-ii/

# 28 ms, faster than 94.70%
# 16.1 MB, less than 63.24%

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSumRec(self, root, targetSum, path, result):
        if not root:
            return
        path.append(root.val)
        if not root.left and not root.right and targetSum == root.val:
            result.append(path[::])
        else:
            self.pathSumRec(root.left, targetSum - root.val, path, result) or self.pathSumRec(root.right, targetSum - root.val, path, result)
        path.pop()
    
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        result = []
        self.pathSumRec(root, targetSum, [], result)
        return result
