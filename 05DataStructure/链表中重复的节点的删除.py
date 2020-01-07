# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if pHead is None:
            return None
        if pHead.next is None:
            return pHead

        flag = 1 if pHead.next.val == pHead.val else 0
        pLast = pHead
        pPreVal = pLast.val
        pNode = pLast.next
        while pNode:
            if pNode.next:
                if pNode.val > pPreVal and pNode.val < pNode.next.val:
                    if flag:
                        pHead = pNode
                        flag = 0
                    pLast.next = pNode
                    pPreVal = pNode.val
                    pLast = pNode
                    pNode = pNode.next

                elif pNode.val == pNode.next.val:
                    pPreVal = pNode.val
                    pNode = pNode.next.next
                else:
                    pNode = pNode.next
            else:
                pLast.next = pNode if pNode.val > pPreVal else None
                if flag:
                    return pNode if pNode.val > pPreVal else None
                else:
                    return pHead
        if flag:
            return None
        else:
            pLast.next = None
            return pHead
