class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        symbol = "$"

        for word in strs:
            res += str(len(word))
            res += symbol
            res += word

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        symbol = "$"

        index = 0

        while index < len(s):
            length = ""
            while True:
                if s[index] == symbol:
                    break   
                else:
                    length += s[index]
                index += 1
            index += 1
            length = int(length)
            temp = ""
            for _ in range(length):
                temp += s[index]
                index += 1
            res.append(temp)

        return res  
        