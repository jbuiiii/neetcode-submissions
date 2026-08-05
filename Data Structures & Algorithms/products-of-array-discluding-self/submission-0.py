class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # want to be doing left and right product arrays
        left = [None]*len(nums)
        right = [None]*len(nums)

        left[0] = nums[0]
        right[len(nums)-1] = nums[len(nums)-1]
        
        for i in range(1, len(nums)):
            left[i] = nums[i] * left[i - 1]
        
        for i in range(len(nums) - 2, -1, -1):
            right[i] = nums[i] * right[i + 1]

        res = [None]*len(nums)
        for i in range(1, len(nums) - 1):
            res[i] = left[i - 1] * right[i + 1]
        
        res[0] = right[1]
        res[len(nums) - 1] = left[len(nums) - 2]
        return res