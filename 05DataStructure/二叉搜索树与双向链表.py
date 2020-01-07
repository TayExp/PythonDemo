# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def Convert(self, pRootOfTree):
        # write code here
        pLastNodeInList = [None]
        self.ConvertNode(pRootOfTree,pLastNodeInList)
        pHeadOfList = pLastNodeInList[0]
        while pHeadOfList is not None and pHeadOfList.left is not None:
            pHeadOfList = pHeadOfList.left
        return pHeadOfList

    def ConvertNode(self,pNode,pLastNodeInList):
        if pNode is None:
            return
        pCurrent = pNode
        if pCurrent.left:
            self.ConvertNode(pCurrent.left,pLastNodeInList)
        pCurrent.left = pLastNodeInList[0]
        if pLastNodeInList[0]:
            pLastNodeInList[0].right = pCurrent
        pLastNodeInList[0] = pCurrent
        if pCurrent.right:
            self.ConvertNode(pCurrent.right,pLastNodeInList)
