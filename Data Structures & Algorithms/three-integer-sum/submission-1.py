class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for index, num in enumerate(nums):
            if num > 0:
                break

            if index > 0 and num == nums[index - 1]:
                continue
        
            L, R = index + 1, len(nums) - 1
            while L < R:
                threeSum = num + nums[L] + nums[R]
                if threeSum > 0:
                    R -= 1
                elif threeSum < 0:
                    L += 1
                else:
                    res.append([num, nums[L], nums[R]])
                    L += 1
                    R -= 1
                    while nums[L] == nums[L - 1] and L < R:
                        L += 1
        
        return res