class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cantidades = {}
        for value in nums:
            if value in cantidades:
                cantidades[value] += 1
            else:
                cantidades [value] = 1
        return max(cantidades, key=cantidades.get)
