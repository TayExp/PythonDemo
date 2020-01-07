# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        maxInWindows = []

        if len(num) >= size and size >= 1:
            index = []
            for i in range(size):
                while(index != [] and num[i] >= num[index[-1]]):
                    index.pop()
                index.append(i)
            for i in range(size,len(num)):
                maxInWindows.append(num[index[0]])
                while index != [] and num[i]>=num[index[-1]]:
                    index.pop()
                if index != [] and index[0] <= (i-size):
                    index.pop(0)
                index.append(i)

            maxInWindows.append(num[index[0]])

        return maxInWindows

s = Solution()
print(s.maxInWindows([2],1))