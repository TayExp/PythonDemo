# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        length = len(tinput)
        if length == 0 or length < k:
            return []
        start = 0
        end = length - 1
        index = self.Partition(tinput, length, start, end)
        while index != k and index != k-1:
            if index > k-1:
                end = index - 1
                index = self.Partition(tinput, length, start, end)
            else:
                start = index + 1
                index = self.Partition(tinput, length, start, end)
        result = sorted(tinput[:k])
        return result

    @staticmethod
    def Partition(numbers,length,start,end):
        i, j = start, end
        while i < j:
            while i<j and numbers[i] <= numbers[start]:
                i += 1
            while i<j and numbers[j] >= numbers[start]:
                j -= 1
            if i < j:
                numbers[i],numbers[j] = numbers[j],numbers[i]
        if  j == 0 or numbers[j] <= numbers[start]:
            numbers[j], numbers[start] = numbers[start], numbers[j]
            return j
        else:
            numbers[j-1], numbers[start] = numbers[start], numbers[j-1]
            return j-1

s = Solution()
a = [1,2,3,2,2,2,5,4,2]
# a=[1]
# a=[]
a =[4,5,1,6,2,7,3,8]
a= [4,5,1,6,2,7,2,8]
print(s.GetLeastNumbers_Solution(a,0))