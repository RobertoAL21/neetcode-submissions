class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int: 
        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = len(nums) + 2

        for i in range(len(nums)):
            if abs(nums[i]) <= len(nums):
                indice = abs(nums[i])
                nums[indice -1]= -abs(nums[indice -1])

        for i in range(len(nums)):
            if nums[i]>0:
                return i + 1
        return len(nums) +1
        