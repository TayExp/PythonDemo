# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        if n < 0:
            n =n&0xffffffff
        flag = 1
        while(flag and flag<0xffffffff):
            if(n & flag):
                count += 1
            flag = flag << 1
        return count

    def NumberOf1_(self, n):
        # write code here
        count = 0
        if n < 0:
            n = n & 0xffffffff
        while (n):
            count += 1
            n = (n - 1) & n
        return count
s = Solution()
print(s.NumberOf1_(-1))
# m-->n
# 统计异或后数中1的个数
# m是不是2的整数次方
# m(m-1)==0