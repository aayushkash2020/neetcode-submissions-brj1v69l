class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = "".join(c.lower() for c in s if c.isalnum())
        i, j = 0, len(a)-1
        while i < j:
            if a[i] != a[j]:
                return False
            i += 1
            j -= 1
        return True