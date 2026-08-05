class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            if str(sorted(word)) in anagrams:
                anagrams[str(sorted(word))].append(word)
            else:
                anagrams[str(sorted(word))] = [word]
        
        res = []
        for anagram in anagrams:
            res.append(anagrams[anagram])
        return res