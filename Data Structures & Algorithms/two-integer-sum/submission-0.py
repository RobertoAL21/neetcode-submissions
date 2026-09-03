class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vistos = {}
        for indice,numeros in enumerate(nums):
            complemento = target - numeros
            if complemento in vistos:
                return [vistos[complemento], indice]
            else:
                vistos[numeros] = indice