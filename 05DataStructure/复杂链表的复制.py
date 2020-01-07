# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution1:
    # 返回 RandomListNode
    def Clone(self, pHead):
        if not pHead:
            return None

        dummy = pHead

        # first step, N' to N next
        while dummy:
            dummynext = dummy.next
            copynode = RandomListNode(dummy.label)
            copynode.next = dummynext
            dummy.next = copynode
            dummy = dummynext

        dummy = pHead

        # second step, random' to random'
        while dummy:
            dummyrandom = dummy.random
            copynode = dummy.next
            if dummyrandom:
                copynode.random = dummyrandom.next
            dummy = copynode.next

        # third step, split linked list
        dummy = pHead
        copyHead = pHead.next
        while dummy:
            copyNode = dummy.next
            dummynext = copyNode.next
            dummy.next = dummynext
            if dummynext:
                copyNode.next = dummynext.next
            else:
                copyNode.next = None
            dummy = dummynext

        return copyHead
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if pHead:
            self.CloneNodes(pHead)
            self.ConnectSiblingNodes(pHead)
            return self.ReconnectNodes(pHead)
        return None

    def CloneNodes(self,pHead):
        pNode = pHead
        while pNode is not None:
            pCloned = RandomListNode(pNode.label)
            pCloned.next = pNode.next
            pNode.next = pCloned
            pNode = pCloned.next

    def ConnectSiblingNodes(self,pHead):
        pNode = pHead
        while pNode is not None:
            if pNode.random:
                pNode.next.random = pNode.random.next
            pNode = pNode.next.next

    def ReconnectNodes(self,pHead):
        pNode = pHead
        pClonedHead = pHead.next
        pCloned = pClonedHead
        while pCloned.next:
            pNode.next = pCloned.next
            pCloned.next = pCloned.next.next
            pNode = pNode.next
            pCloned = pCloned.next
        pNode.next = None

        return pClonedHead