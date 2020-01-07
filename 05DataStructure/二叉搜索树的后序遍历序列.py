# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        length = len(sequence)
        if length == 0:
            return False
        root = sequence[-1]
        left = []
        right = []
        for i in range(length-1):
            if sequence[i] > root:
                j = i
                break
            left.append(sequence[i])
        else:
            j = length-1
        for i in range(j,length-1):
            if sequence[i] < root:
                return False
            right.append(sequence[i])
        if len(left) > 0:
            bLeft = self.VerifySquenceOfBST(left)
        else:
            bLeft = True
        if len(right) > 0:
            bRight = self.VerifySquenceOfBST(right)
        else:
            bRight = True
        return bLeft and bRight
s = Solution()
a = [5,7,6,11,9,10,8]
print(s.VerifySquenceOfBST(a))