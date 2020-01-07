# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        len1 = len(s)
        p1 = 0
        len2 = len(pattern)
        p2 = 0
        return self.matchCore(s,p1,len1,pattern,p2,len2)

    def matchCore(self, s,p1,len1,pattern,p2,len2):
        if p1 == len1 and p2 == len2:
            return True
        if p1 < len1 and p2 == len2:
            return False
        if p2+1 < len2 and pattern[p2+1] == "*":
            if p1 == len1 or (s[p1] != pattern[p2] and pattern[p2] != "."):
                return self.matchCore(s, p1, len1, pattern, p2 + 2, len2)
            else:
                return self.matchCore(s,p1+1,len1,pattern,p2,len2) or \
                       self.matchCore(s,p1+1,len1,pattern,p2+2,len2) or\
                       self.matchCore(s,p1,len1,pattern,p2+2,len2)

        elif p1 < len1:
            if s[p1] == pattern[p2] or pattern[p2] == ".":
                return self.matchCore(s,p1+1,len1,pattern,p2+1,len2)

        return False

s = Solution()
print(s.match("",".*"))
