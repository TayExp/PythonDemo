# -*- coding:utf-8 -*-
class Solution:
    # 返回对应char
    def __init__(self):
        self.occurrence = [-1] * 256
        self.s = []
    def FirstAppearingOnce(self):
        # write code here
        for ch in self.s:
            if self.occurrence[ord(ch)] == 1:
                return ch
        return "#"

    def Insert(self, char):
        # write code here
        if self.occurrence[ord(char)] == -1:
            self.occurrence[ord(char)] = 1
        else:
            self.occurrence[ord(char)] = -2
        self.s.append(char)


s = Solution()
print(s.FirstAppearingOnce())
s.Insert("g")
s.Insert("o")
s.Insert("o")
s.Insert("g")
s.Insert("l")
s.Insert("e")
print(s.FirstAppearingOnce())