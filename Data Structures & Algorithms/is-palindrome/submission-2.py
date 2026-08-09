class Solution:
    def isPalindrome(self, s: str) -> bool:
        L = 0
        R = len(s) - 1
        punct = set("!@#$%^&*()<>?,./:\"'{}[]\\| ")
        s = s.lower()

        while L < R:
            if s[L] == s[R]:
                L += 1
                R -= 1
            elif s[L] in punct:
                L += 1
            elif s[R] in punct:
                R -= 1
            else:
                return False
        return True