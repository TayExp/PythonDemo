# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        i = 0
        j = len(array)-1
        flag = False
        while(i <= j):
            sum = array[i] + array[j]
            if sum == tsum:
                a, b = array[i], array[j]
                flag = True
                i += 1
                j -= 1
            elif sum < tsum:
                i += 1
            else:
                j -= 1
        if flag:
            return a, b
        else:
            return []

    def FindContinuousSequence(self, tsum):
        # write code here
        result = []
        small = 1
        big = 2
        sum = small + big
        if tsum >= sum:
            while(big > small):
                if sum == tsum:
                    result.append([x for x in range(small,big+1)])
                    sum = sum + big- small*2
                    small += 2
                    big += 1
                elif sum > tsum:
                    sum -= small
                    small += 1
                else:
                    big += 1
                    sum += big
        return result

s = Solution()
print(s.FindNumbersWithSum([1,2,4,7,11,15],15))
print(s.FindContinuousSequence(3))