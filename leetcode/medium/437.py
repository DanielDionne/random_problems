# 437. Path Sum III
# https://leetcode.com/problems/path-sum-iii/

# 184 ms, faster than 54.27%
# 14.5 MB, less than 71.36%

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def count(self, path, sum):
        c = 0
        result = 0
        for i in reversed(path):
            c+= i
            result += c == sum
        return result

    def pathSumRec(self, root, sum, path):
        if not root:
            return 0
        path.append(root.val)
        sums = self.count(path, sum)
        result = sums + self.pathSumRec(root.left, sum, path) + self.pathSumRec(root.right, sum, path)
        path.pop()
        return result
        
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        '''
        do a DFS
        keep current path
        every time I add a node, check if I can sum up to target with path
        
        '''
        
        return self.pathSumRec(root, sum, [])