# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if pHead is None:
            return None
        pSlow, pFast = pHead, pHead
        while pFast and pFast.next:
            pFast = pFast.next.next
            pSlow = pSlow.next
            if pFast == pSlow:
                pNode1 = pSlow
                pNode2 = pHead
                while pNode1 and pNode1 != pSlow:
                    pNode1 = pNode1.next
                    pNode2 = pNode2.next
                pNode1 = pHead
                while pNode2 != pNode1:
                    pNode1 = pNode1.next
                    pNode2 = pNode2.next
                return pNode1
