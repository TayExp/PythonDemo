# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        sList = s.split(" ")
        sList.reverse()
        return " ".join(sList)

    def LeftRotateString(self, s, n):
        # write code here
        if s == "":
            return ""
        if n > len(s):
            n = n % len(s)
        sList = list(s)
        s1 = sList[:n]
        s2 = sList[n:]
        s1.reverse()
        s2.reverse()
        sList = s1 + s2
        sList.reverse()
        return "".join(sList)

s = "I am a student."
so = Solution()
print(so.ReverseSentence(s))
s="abcdefg"
print(so.LeftRotateString(s,2))