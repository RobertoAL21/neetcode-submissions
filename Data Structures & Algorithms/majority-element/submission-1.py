class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        vistos = {}
        for value in nums:
            if value in vistos:
                vistos[value] += 1
            else:
                vistos[value] = 1
        
        major = max(vistos, key=vistos.get)
        return major
