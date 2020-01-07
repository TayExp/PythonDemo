# -*- coding:utf-8 -*-
class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        visited = [[False for i in range(cols)] for j in range(rows)]
        return self.movingCountCore(threshold,rows,cols,0,0,visited)

    def movingCountCore(self,threshold,rows,cols,row,col,visited):
        count = 0
        if self.check(threshold,rows,cols,row,col,visited):
            visited[row][col] = True
            count = 1 + self.movingCountCore(threshold,rows,cols,row,col+1,visited)\
                    +  self.movingCountCore(threshold,rows,cols,row+1,col,visited)\
                    +  self.movingCountCore(threshold,rows,cols,row-1,col,visited)\
                    +  self.movingCountCore(threshold,rows,cols,row,col-1,visited)
        return count

    def check(self, threshold, rows, cols, row, col, visited):
        if row >= 0 and row < rows and col >= 0 and col < cols and \
            self.getDigitSum(row) + self.getDigitSum(col) <= threshold\
            and not visited[row][col]:
            return True
        return False

    @staticmethod
    def getDigitSum(num):
        sum = 0
        while num > 0:
            sum += num % 10
            num = num // 10
        return sum

s = Solution()

print (s.movingCount(0,1,1))