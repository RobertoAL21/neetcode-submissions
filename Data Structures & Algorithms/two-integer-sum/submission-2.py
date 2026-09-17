class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vistos = {}
        for indice,value in enumerate(nums):
            meta = target - value
            if meta in vistos:
                return [vistos[meta], indice]
            else:
                vistos[value] = indice
