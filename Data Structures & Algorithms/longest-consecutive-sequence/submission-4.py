class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setnum = set(nums)
        starts = []
        maxx = 0

        for num in nums:
            if (num - 1) not in setnum:
                starts.append(num)

        for num in starts:
            temp = 1
            curr = num
            while True:
                if (curr + 1) in setnum:
                    curr += 1
                    temp += 1
                else:
                    break
            maxx = max(temp, maxx)
                
        
        return maxx