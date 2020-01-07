# -*- coding:utf-8 -*-
class Solution:
    def Add(self, num1, num2):
        # write code here
        sum = num1^num2
        carry = (num1 & num2) <<1
        while carry:
            tmp = sum
            sum = sum^carry
            carry = (tmp & carry) <<1
        return sum

s = Solution()
print(s.Add(-19,-2))