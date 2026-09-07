class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        vistos = set()
        for numero in nums:
            if numero >= 0:
                vistos.add(numero)
        i = 1
        for value in range(len(vistos)+1):
            if i in vistos:
                i += 1
            else:
                return i
        