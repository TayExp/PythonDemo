# -*- coding:utf-8 -*-
from functools import cmp_to_key
class Solution:
    def PrintMinNumber_(self, numbers):
        # write code here
        length = len(numbers)
        if length == 0:
            return 0
        if length == 1:
            return numbers[0]
        strNumbers = [str(num) for num in numbers]
        strNumbers.sort( cmp = lambda x,y : int(x+y)-int(y+x))
        return int("".join(strNumbers))

    def PrintMinNumber(self, numbers):
        # write code here
        length = len(numbers)
        if length == 0:
            return ""
        if length == 1:
            return numbers[0]
        key = cmp_to_key(lambda x, y: int(x+y)-int(y+x))
        strNumbers = sorted(map(str, numbers),key=key)
        return int("".join(strNumbers))

    # @staticmethod


s = Solution()
print(s.PrintMinNumber([32,321,3]))