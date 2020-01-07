# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        # write code here
        if s == "":
            return 0
        minus = 1
        if s[0] == "-" or s[0] == "+":
            if s[0] == "-":
                minus = -1
            return self.StrToIntCore(s[1:])*minus
        else:
            return self.StrToIntCore(s)

    @staticmethod
    def StrToIntCore(s):
        num = 0
        for char in s:
            if char <= "9" and char >= "0":
                num = num * 10 + (int(char))
            else:
                return 0
        else:
            return num

s = Solution()
print(s.StrToInt("-0123"))

