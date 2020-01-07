# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        if pRoot and k > 0:
            return self.KthNodeCore(pRoot,k)[0]
        else:
            return None

    def KthNodeCore(self,pRoot,k):
        target = None
        if pRoot.left:
            target,k = self.KthNodeCore(pRoot.left,k)

        if target is None:
            if k == 1:
                target = pRoot
            k -= 1
        if target is None and pRoot.right:
            target,k = self.KthNodeCore(pRoot.right,k)
        return target,k