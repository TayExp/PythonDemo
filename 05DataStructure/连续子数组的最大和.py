# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if array == []:
            return 0
        sum = 0
        max_sum = array[-1]
        for num in array:
            sum += num
            if sum > max_sum :
                max_sum = sum
            if num > sum:
                sum = num
                if sum > max_sum:
                    max_sum = sum
        return max_sum

a = [1,-2,3,10,-4,7,2,-5]
a=[-2,-8,-1,-5,-9]
s = Solution()
print(s.FindGreatestSumOfSubArray(a))