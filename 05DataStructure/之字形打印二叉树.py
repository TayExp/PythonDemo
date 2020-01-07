# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        if pRoot is None:
            return []
        current, nextlevel = 0, 1
        result,currentResult = [],[]
        stack = [[pRoot],[]]
        while stack[0]!=[] or stack[1]!=[]:
            node = stack[current].pop()
            currentResult.append(node.val)
            if current == 1:
                if node.left:
                    stack[0].append(node.left)
                if node.right:
                    stack[0].append(node.right)
            else:
                if node.right:
                    stack[1].append(node.right)
                if node.left:
                    stack[1].append(node.left)
            if stack[current] == []:
                current,nextlevel = nextlevel,current
                result.append(currentResult)
                currentResult = []
        return result