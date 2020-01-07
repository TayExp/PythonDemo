# -*- coding:utf-8 -*-
# 一边（归并）合并相邻的子数组，一边统计逆序对的数目
class Solution:
    # def InversePairs(self, data):
    #     # write code here
    #     if data == []:
    #         return 0
    #     copy = [x for x in data]
    #     return self.InversePairsCore(data,copy,0,len(data)-1)
    #
    # def InversePairsCore(self,data,copy,start,end):
    #     if start == end:
    #         copy[start] = data[start]
    #         return 0
    #     middle = (end+start)//2
    #     left = self.InversePairsCore(copy,data,start,middle)
    #     right = self.InversePairsCore(copy,data,middle+1,end)
    #     count = 0
    #     i, j, k = middle, end ,end
    #     while i >= start and j > middle:
    #         if data[i] > data[j]:
    #             count += j-middle
    #             copy[k] = data[i]
    #             i -= 1
    #         else:
    #             copy[k] = data[j]
    #             j -= 1
    #         k -= 1
    #     if i >= start:
    #         while k >= start:
    #             copy[k] = data[i]
    #             k -= 1
    #             i -= 1
    #     elif j > middle:
    #         while k >= start:
    #             copy[k] = data[j]
    #             k -= 1
    #             j -= 1
    #     return left + right + count
    # def InversePairs(self, data):
    #     # write code here
    #     if data == []:
    #         return 0
    #     length = len(data)
    #     copy = data[:]
    #     index = [1]
    #     while index[-1]*2 <= length:
    #         index.append(index[-1]*2)
    #     count = 0
    #     for interval in index:
    #         for k in range(0,length,interval*2):
    #             # start,start+interval,start+interval*2-1
    #             if k + interval-1 >= length:
    #                 continue
    #             middle =k + interval-1
    #             end = min(k+interval*2-1,length-1)
    #             i, j = middle, end
    #             copy_id = end
    #             while i>=k and j > middle and copy_id >= k:
    #                 if data[i] > data[j]:
    #                     count += j - middle
    #                     copy[copy_id] = data[i]
    #                     copy_id -= 1
    #                     i -= 1
    #                 elif data[i] < data[j]:
    #                     copy[copy_id] = data[j]
    #                     j -= 1
    #                     copy_id -= 1
    #             if i < k:
    #                 copy[k:copy_id+1] = data[middle+1:j+1]
    #             elif j == middle:
    #                 copy[k:copy_id+1] = data[k:i+1]
    #         data = copy[:]
    #     return count

    def InversePairs(self, data):
        if data == []:
            return 0
        count = 0
        length = len(data)
        while length > 0:
            for i in range(length-1):
                if data[i] > data[-1]:
                    count += 1
            data.pop()
            length -= 1
        return count

s = Solution()
print(s.InversePairs([7,5,6,4,1]))