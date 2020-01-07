# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if head is None or k == 0:
            return None
        pAhead = head
        pBehind = head
        for i in range(k):
            if pAhead is None:
                return None
            else:
                pAhead = pAhead.next
        if pAhead is None:
            return pBehind
        while pAhead is not None:
            pAhead = pAhead.next
            pBehind = pBehind.next
        return pBehind
