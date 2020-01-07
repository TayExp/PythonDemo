# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if root is None:
            return []
        currentSum = 0
        path = []
        ipath = []
        self.toFindPath(root,expectNumber,path,ipath,currentSum)
        return path

    def toFindPath(self,root,expectNumber,path,ipath,currentSum):
        currentSum += root.val
        ipath.append(root.val)
        if (currentSum == expectNumber and
                root.left is None and root.right is None):
            path.append(ipath[:])
        if root.left:
            self.toFindPath(root.left, expectNumber, path, ipath, currentSum)
        if root.right:
            self.toFindPath(root.right, expectNumber, path, ipath, currentSum)
        ipath.pop()