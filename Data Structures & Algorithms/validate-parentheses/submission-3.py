class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {'(':')', 
                    '{':'}', 
                    '[':']'}
        left = set(brackets.keys())

        for i in range(len(s)):
            if s[i] in brackets.keys():
                stack.append(s[i])
            else:
                if not stack:
                    return False

                temp = stack.pop()
                if brackets[temp] != s[i]:
                    return False
        
        if stack:
            return False
        return True 


            