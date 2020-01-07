# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror_(self, root):
        # write code here
        if root is not None:
            if root.left or root.right:
                pTemp = root.left
                root.left = root.right
                root.right = pTemp
            if root.left:
                root.left = self.Mirror(root.left)
            if root.right:
                root.right = self.Mirror(root.right)
        return root
    # 栈实现
    def Mirror_(self,root):
        if root is not None:
            pList = []
            pNode = root
            while len(pList) > 0 or pNode is not None:
                if pNode:
                    pList.append(pNode.right)
                    if pNode.left or pNode.right:
                        pTemp = pNode.left
                        pNode.left = pNode.right
                        pNode.right = pTemp
                    pNode = pNode.right
                else:
                    pNode = pList.pop()
        return root
