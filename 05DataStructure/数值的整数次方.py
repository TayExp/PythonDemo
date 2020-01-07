# -*- coding:utf-8 -*-
g_InvalidInput = False
class Solution:
    def Power1(self, base, exponent):
        # write code here
        if abs(base)<1e-9 and exponent<0:
            g_InvalidInput = True
            return 0.0
        absExponent = abs(exponent)
        result = 1
        for i in range(absExponent):
            result *= base
        if exponent < 0:
            result = 1/result
        return result
    def Power(self, base, exponent):
        if abs(base)<1e-9 and exponent<0:
            g_InvalidInput = True
            return 0.0
        absExponent = abs(exponent)
        result = self.PowerWithUnsignedExponent(base, absExponent)
        if exponent < 0:
            result = 1/result
        return result

    def PowerWithUnsignedExponent(self, base,absExponent):
        if absExponent == 0:
            return 1
        if absExponent == 1:
            return base
        semiResult = self.PowerWithUnsignedExponent(base,absExponent>>1)
        result = semiResult * semiResult
        if absExponent & 1 == 1:
            result *= base
        return result

s= Solution()
print(s.Power(3,-4))
