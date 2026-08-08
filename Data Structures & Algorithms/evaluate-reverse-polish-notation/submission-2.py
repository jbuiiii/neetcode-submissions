class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        symbols = {'+', '-', '*', '/'}

        for token in tokens:
            if token not in symbols:
                stack.append(int(token))
            else:
                if token == "+":
                    stack[-2] += stack[-1]
                if token == "-":
                    stack[-2] -= stack[-1]
                if token == "*":
                    stack[-2] *= stack[-1]
                if token == "/":
                    stack[-2] = int(stack[-2] / stack[-1])
                stack.pop()
        
        return stack[-1]