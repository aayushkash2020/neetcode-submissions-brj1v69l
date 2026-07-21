class Solution:
    def myPow(self, x: float, n: int) -> float:
        # if n == 0:
        #     return 1
        if n < 0:
            x = 1/x
            n = -n
        res = x
        mult = 1
        while n > 0:
            if n % 2 == 1:
                mult *= res
            res *= res
            n //= 2
        return mult
        # if n == 0:
        #     return 1
        # if n < 0:
        #     return 1 / self.myPow(x, -n)
        # if n % 2 == 0:
        #     return self.myPow(x * x, n // 2)
        # return x * self.myPow(x * x, n // 2)