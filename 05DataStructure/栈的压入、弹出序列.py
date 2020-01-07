# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        bPossible = False
        pEnd = len(pushV)
        if pEnd > 0:
            stackData = []
            pNextPop = pNextPush = 0
            while pNextPop < pEnd:
                while (len(stackData)==0
                       or stackData[-1]!= popV[pNextPop]):
                    if  pNextPush == pEnd:
                        break
                    stackData.append(pushV[pNextPush])
                    pNextPush += 1
                if stackData[-1] != popV[pNextPop]:
                    break
                else:
                    stackData.pop()
                    pNextPop += 1
            if len(stackData)==0 and pNextPop == pEnd:
                bPossible = True
        return bPossible
pushV = [1,2,3,4,5]
popV = [4,5,3,2,1]
# popV = [4,3,5,1,2]
S = Solution()
print(S.IsPopOrder(pushV,popV))
