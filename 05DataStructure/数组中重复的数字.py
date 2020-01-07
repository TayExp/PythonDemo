# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        length = len(numbers)
        duplication[0] = -1
        if length == 0:
            return  False

        for i in range(length):
            while numbers[i] != i:
                if numbers[i] == numbers[numbers[i]] and i!= numbers[i]:
                    duplication[0] = numbers[i]
                    return True
                tmp = numbers[i]
                numbers[i] = numbers[tmp]
                numbers[tmp] = tmp
        return False

