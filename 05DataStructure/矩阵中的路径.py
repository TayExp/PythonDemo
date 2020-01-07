# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        if len(matrix) == 0 or len(path) == 0 or rows < 1 or cols < 1:
            return False
        board = [[matrix[i*cols+j] for j in range(cols)] for i in range(rows)]
        for row in range(rows):
            for col in range(cols):
                pathLength = [0]
                visited = [[False for j in range(cols)] for i in range(rows)]
                if self.hasPathCore(board, rows, cols, row, col, path, pathLength, visited):
                    return True

        return False

    def hasPathCore(self, board, rows, cols, row, col, path, pathLength, visited):
        if pathLength[0] == len(path):
            return True
        hasPath = False
        if (row >= 0 and row < rows and col >= 0 and col < cols and
                board[row][col] == path[pathLength[0]] and not visited[row][col]):
            pathLength[0] += 1
            visited[row][col] = True
            hasPath = self.hasPathCore(board, rows, cols, row, col + 1, path, pathLength, visited) or\
                      self.hasPathCore(board, rows, cols, row + 1, col, path, pathLength, visited) or\
                      self.hasPathCore(board, rows, cols, row, col - 1, path, pathLength, visited) or\
                      self.hasPathCore(board, rows, cols, row - 1, col, path, pathLength, visited)
            if not hasPath:
                pathLength[0] -= 1
                visited[row][col] = False

        return hasPath

s = Solution()
ma = "abcesfcsasee"
pa ="bccee"
print (s.hasPath(ma,3,4,pa))