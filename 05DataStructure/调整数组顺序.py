# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray_(self, array):
        # write code here
        if len(array) <= 1:
            return array
        pBegin, pEnd = 0, len(array) - 1
        while (pBegin < pEnd):
            while (pBegin < pEnd and not self.isEven(array[pBegin])):
                pBegin += 1
            while (pBegin < pEnd and self.isEven(array[pEnd])):
                pEnd -= 1
            if pBegin < pEnd:
                array[pBegin], array[pEnd] = array[pEnd], array[pBegin]
        return array

    def reOrderArray(self, array):
        # write code here
        if len(array) <= 1:
            return array
        k = 0
        for i in range(len(array)):
            if not self.isEven(array[i]):
                # 遇见奇数就往前插,插在所有偶数前面
                for j in range(i,k,-1):
                    if j >= 1:
                        array[j], array[j-1] = array[j-1], array[j]
                k += 1
        return array

    @staticmethod
    def isEven(n):
        return (n & 1 == 0)
s = Solution()
print(s.reOrderArray([2,1,2,3,4,5,6,7,8,9,11,13]))