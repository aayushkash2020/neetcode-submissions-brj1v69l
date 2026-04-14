class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        m, n = len(num1), len(num2)
        res = [0] * (m + n)
        for i in range(m-1, -1, -1):
            d1 = ord(num1[i]) - ord('0')
            for j in range(n-1, -1, -1):
                d2 = ord(num2[j]) - ord('0')
                prod = d1 * d2 + res[i+j+1]
                res[i+j+1] = prod % 10
                res[i+j] += prod // 10

        i = 0
        while i < len(res) and res[i] == 0:
            i += 1
        return ''.join(map(str, res[i:]))