class Solution:
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
            
        res = ""
        symbol = "/"
        for word in strs:
            res += word
            res += symbol
        return res


    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        res = []
        temp = ""
        stack = []
        symbol = "/"
        
        for char in s:
            if stack:
                if char == symbol:
                    temp += symbol
                else:
                    res.append(temp)
                    temp = char
                stack.clear()
            else:
                if char == symbol:
                    stack.append(symbol)
                else:
                    temp += char
        res.append(temp)
        return res
