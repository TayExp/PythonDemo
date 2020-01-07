# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here

        p = 0
        pend = len(s)

        if s[p] == "+" or s[p] == "-":
            p += 1
        if p == pend:
            return False

        flag = True
        while p<pend and s[p] >= "0" and s[p] <= "9":
            p += 1

        if p < pend and s[p] == ".":
            p += 1
            while p< pend and s[p] >= "0" and s[p] <= "9":
                p += 1

        if p < pend:
            if s[p] == "e" or s[p] == "E":
                p += 1
                if p < pend and (s[p] == "+" or s[p] == "-"):
                    p += 1
                if p == pend:
                    flag = False
                while p<pend and s[p] >= "0" and s[p] <= "9":
                    p += 1
                if p < pend:
                    flag = False
            else:
                flag = False

        return flag

s = Solution()
print(s.isNumeric("1e+4.3"))