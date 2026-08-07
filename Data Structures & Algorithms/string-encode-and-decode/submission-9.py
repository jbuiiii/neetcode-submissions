class Solution:
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        res = ""
        symbol = "#" # delimiter

        for word in strs:
            res += str(len(word))
            res += symbol
            res += word

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        symbol = "#"
        
        while i < len(s):
            j = i
            while s[j] != symbol:
                j += 1
            
            length = int(s[i:j])
            word = s[j + 1 : j + 1 + length]
            res.append(word)
            i = j + 1 + length
            
        return res
