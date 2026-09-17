class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vistos = {}
        for indice,value in enumerate(nums):
            x = target - value
            if x in vistos:
                return [vistos[x],indice]
            else:
                vistos[value] = indice
