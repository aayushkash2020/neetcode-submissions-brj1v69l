class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            while i < j and not self.alphaNum(s[i]):
                i += 1
            while j > i and not self.alphaNum(s[j]):
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True

    def alphaNum(self, a):
        return ord('A') <= ord(a) <= ord('Z') or \
               ord('a') <= ord(a) <= ord('z') or \
               ord('0') <= ord(a) <= ord('9')
            
        # a = "".join(c.lower() for c in s if c.isalnum())
        # i, j = 0, len(a)-1
        # while i < j:
        #     if a[i] != a[j]:
        #         return False
        #     i += 1
        #     j -= 1
        # return True