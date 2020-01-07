# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        return self.IsBalanced(pRoot, 0)[0]

    def IsBalanced(self, pRoot, depth):
        if pRoot is None:
            return True, 0
        bLeft, depthLeft = self.IsBalanced(pRoot.left, depth)
        bRight, depthRight = self.IsBalanced(pRoot.right, depth)
        if bLeft and bRight:
            diff = depthLeft - depthRight
            if diff <= 1 and diff >= -1:
                return True, max(depthLeft, depthRight) + 1
        return False, max(depthLeft, depthRight) + 1