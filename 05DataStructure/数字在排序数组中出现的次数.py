# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        first = self.GetFirst(data, k, 0, len(data) - 1)
        if first == -1:
            return 0
        last = self.GetLast(data, k, 0, len(data) - 1)
        return last - first + 1

    def GetFirst(self, data, k, start, end):
        if start > end:
            return -1
        middle = (start + end) // 2
        if data[middle] == k:
            while middle >= 0 and data[middle] == k:
                middle -= 1
            return middle + 1
        elif data[middle] < k:
            start = middle + 1
        else:
            end = middle - 1
        return self.GetFirst(data, k, start, end)

    def GetLast(self, data, k, start, end):
        if start > end:
            return -1
        middle = (start + end) // 2
        if data[middle] == k:
            while middle <= end and data[middle] == k:
                middle += 1
            return middle - 1

        elif data[middle] < k:
            start = middle + 1
        else:
            end = middle - 1
        return self.GetLast(data, k, start, end)
s = Solution()
print(s.GetNumberOfK([1,2,3,3,3,3,3,4,5,6,7],3))