class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        vistos = set()
        for value in nums:
            if value in vistos:
                return True
            else:
                vistos.add(value)
        return False
        