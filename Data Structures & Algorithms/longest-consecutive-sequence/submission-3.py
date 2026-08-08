class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # Brute force
        nums = set(nums)
        nums = list(nums)
        nums.sort()
        temp = 1
        maxx = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                temp += 1
            else:
                temp = 1
            maxx = max(temp, maxx)

        return maxx