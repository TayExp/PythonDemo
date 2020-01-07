# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        if n <= 0:
            return 0
        strNum = str(n)
        length = len(strNum)
        if length == 1:
            return 1
        if strNum[0] > "1":
            numFirstDigit =  pow(10, length - 1)
        else:
            numFirstDigit = n - pow(10, length - 1) + 1
        numOtherDigits = int(strNum[0]) * (length-1) * pow(10,length-2)
        numRecursive = self.NumberOf1Between1AndN_Solution(int(strNum[1:]))
        return numFirstDigit + numOtherDigits + numRecursive

s = Solution()
print(s.NumberOf1Between1AndN_Solution(12))