class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for numero in nums:
            if numero != val:
                nums[k] = numero
                k += 1
        return k
        