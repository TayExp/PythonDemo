# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        end = len(ss)
        result = []
        if end > 0:
            self.subPermutation(list(ss),0,end,result)
        return result

    def subPermutation(self,ss,begin,end,result):
        if begin == end:
            result.append("".join(ss))
        else:
            for ch in range(begin,end):
                if ss[begin] == ss[ch] and begin != ch:
                    continue
                ss[begin],ss[ch] = ss[ch],ss[begin]
                self.subPermutation(ss[:],begin+1,end,result)
                # ss[ch], ss[begin] = ss[begin], ss[ch]

s = Solution()
print(s.Permutation("123"))