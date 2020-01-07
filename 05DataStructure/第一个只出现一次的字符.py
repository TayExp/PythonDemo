# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if s == "":
            return -1
        hashTable = [0] * 256
        for ch in s:
            hashTable[ord(ch)] += 1
        for i in range(len(s)):
            if hashTable[ord(s[i])] == 1:
                return i
        else:
            return -1

    def DeleteS2fromS1(self,s1,s2):
        # write code here
        if s2 == "":
            return s1
        hashTable = [0] * 256
        for ch in s2:
            hashTable[ord(ch)] += 1
        for i in range(len(s1)):
            if hashTable[ord(s1[i])] == 1:
                s1 = s1[:i] + s1[i+1:]
        return s1

    def DeleteRepetition(self,s):
        if s == "":
            return s
        sLs = list(s)
        hashTable = [False] * 256
        i = 0
        while i < len(sLs):
            if hashTable[ord(sLs[i])] == True:
                sLs.pop(i)
            else:
                hashTable[ord(sLs[i])] = True
                i += 1
        return "".join(sLs)

s = Solution()
print(s.FirstNotRepeatingChar("abaccdeff"))
print(s.DeleteRepetition("google"))