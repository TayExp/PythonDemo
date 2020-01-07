# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:

    def Serialize(self, root):
        # write code here
        sList = []
        self.SerializeCore(root,sList)
        return "".join(sList)

    def SerializeCore(self,root,sList):
        if root is None:
            sList.append("#,")
            return
        sList.append(str(root.val)+",")
        self.SerializeCore(root.left,sList)
        self.SerializeCore(root.right,sList)

    def Deserialize(self, s):
        # write code here
        sList = self.ReadStr(s)
        root = self.DeserializeCore(sList)
        return root

    def DeserializeCore(self,sList):
        val = sList.pop(0)
        if val is not None:
            root = TreeNode(val)
            root.left = self.DeserializeCore(sList)
            root.right = self.DeserializeCore(sList)
            return root


    def ReadStr(self, s):
        sList = []
        count = 0
        while count < len(s):
            if s[count] != "#":
                num = s[count]
                count += 1
                while s[count] != ",":
                    num += s[count]
                    count += 1
                num = int(num)
                count += 1
                sList.append(num)
            else:
                count += 2
                sList.append(None)
        return sList

s = Solution()
st = "#,"
print(s.ReadStr(st))
print(s.Deserialize(st))