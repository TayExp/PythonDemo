# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.__min = []
        self.__stack = []
    def push(self, node):
        # write code here
        self.__stack.append(node)
        if self.__min==[]:
            self.__min.append(node)
            return
        cur_min = self.__min[-1]
        if cur_min < node:
            self.__min.append(cur_min)
        else:
            self.__min.append(node)
    def pop(self):
        # write code here
        self.__min.pop()
        return self.__stack.pop()
    def top(self):
        # write code here
        return self.__stack[-1]
    def min(self):
        # write code here
        return self.__min[-1]

s = Solution()
s.push(3)
s.push(4)
s.push(2)
s.push(1)
s.pop()
s.pop()
s.push(0)
print(s.top())

