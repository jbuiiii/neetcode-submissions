class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {'(':')', 
                    '{':'}', 
                    '[':']'}

        for i in range(len(s)):
            if s[i] in brackets:
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


            