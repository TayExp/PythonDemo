# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        resultExclusiveOR = 0
        for num in array:
            resultExclusiveOR ^= num
        indexOf1 = self.FindFirstBitIs1(resultExclusiveOR)
        a, b = 0, 0
        for num in array:
            if self.IsBit(num,indexOf1):
                a = a^num
            else:
                b = b^num
        return [a,b]

    @staticmethod
    def FindFirstBitIs1(num):
        indexBit = 0
        while num&1 == 0:
            num = num >> 1
            indexBit += 1
        return indexBit

    @staticmethod
    def IsBit(num,indexBit):
        num = num >> indexBit
        return (num&1)