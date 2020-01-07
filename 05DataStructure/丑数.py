# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index <= 0:
            return 0
        uglyNumbers = [0] * index
        uglyNumbers[0] = 1
        cur_index = 1
        cur_id2 = 0
        cur_id3 = 0
        cur_id5 = 0
        while cur_index < index:

            uglyNumbers[cur_index] = min(uglyNumbers[cur_id2]*2,uglyNumbers[cur_id3]*3,
                               uglyNumbers[cur_id5] * 5)
            while uglyNumbers[cur_id2]*2<=uglyNumbers[cur_index]:
                cur_id2 += 1
            while uglyNumbers[cur_id3]*3<=uglyNumbers[cur_index]:
                cur_id3 += 1
            while uglyNumbers[cur_id5]*5<=uglyNumbers[cur_index]:
                cur_id5 += 1
            cur_index += 1
        return uglyNumbers[index-1]
s = Solution()
print(s.GetUglyNumber_Solution(1))