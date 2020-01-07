# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        printList =[]
        if root:
            queue = []
            cur_pNode = root
            while cur_pNode is not None or len(queue) > 0:
                if cur_pNode:
                    printList.append(cur_pNode.val)
                    queue.append(cur_pNode.left)
                    queue.append(cur_pNode.right)
                cur_pNode = queue.pop(0)
        return printList