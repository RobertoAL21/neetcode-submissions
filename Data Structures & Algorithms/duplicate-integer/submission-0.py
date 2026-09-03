class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        vistos = set()
        for values in nums:
            if values in vistos:
                return True
            else:
                vistos.add(values)
        return False
            
        