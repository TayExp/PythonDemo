# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution_(self, numbers):
        # write code here
        length = len(numbers)
        if length == 0:
            return 0

        middle = length >> 1
        start = 0
        end = length - 1
        index = self.Partition(numbers,length,start,end)
        while index != middle:
            if index > middle:
                end = index - 1
                index = self.Partition(numbers,length,start,end)
            else:
                start = index + 1
                index = self.Partition(numbers,length,start,end)
        result = numbers[middle]
        if numbers.count(result) * 2 <= length:
            result = 0
        return result

    @staticmethod
    def Partition(numbers,length,start,end):
        index = start
        i,j = start+1, end
        while i < j:
            while i<j and numbers[i] <= numbers[index]:
                i += 1
            while i<j and numbers[j] >= numbers[index]:
                j -= 1
            if i < j:
                numbers[i],numbers[j] = numbers[j],numbers[i]

        numbers[index], numbers[j] = numbers[j],numbers[index]
        return j

    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        length = len(numbers)
        if length == 0:
            return 0
        result = numbers[0]
        times = 1
        for i in range(1,length):
            if numbers[i] == result:
                times += 1
            else:
                if times > 0:
                    times -= 1
                else:
                    times = 1
                    result = numbers[i]
        if numbers.count(result) * 2 <= length:
            result = 0
        return result
s = Solution()
a = [1,2,3,2,2,2,5,4,2]
a=[1]
a=[]
print(s.MoreThanHalfNum_Solution(a))