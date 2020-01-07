# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        printList = []
        rows = len(matrix)
        if rows > 0:
            columus = len(matrix[0])
            start = 0
            while(columus > 2*start and rows > 2*start):
                printList.extend(self.printMatrixInCircle(matrix,start,rows,columus))
                start += 1
        return printList

    def printMatrixInCircle(self,matrix,start,rows,columus):
        oneCircleList = []
        endX = columus - 1 - start
        endY = rows - 1- start
        for i in range(start,endX+1):
            oneCircleList.append(matrix[start][i])
        if endY > start:
            for i in range(start+1,endY+1):
                oneCircleList.append(matrix[i][endX])
            if endX > start:
                for i in range(endX-1,start-1,-1):
                 oneCircleList.append(matrix[endY][i])
                if endY-1 > start:
                        for i in range(endY-1,start,-1):
                            oneCircleList.append(matrix[i][start])
        return oneCircleList

a=[1,2,3,4,5]
b=[6,7,8,9,10]
c=[11,12,13,14,15]
d=[16,17,18,19,20]
e=[21,22,23,24,25]
f=[26,27,28,29,30]
s = Solution()
h=[]
for i in h:
    print(i)
print(s.printMatrix(h))