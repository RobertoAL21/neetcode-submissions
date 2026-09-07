class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        buckets = [[] for _ in range (n+1)]

        cantidad = {}
        for value in nums:
            if value in cantidad:
                cantidad[value] += 1
            else:
                cantidad[value] = 1

        for numero, frecuencia in cantidad.items():
            buckets[frecuencia].append(numero)

        result = []

        for i in range(n, 0, -1):
            for numero in buckets[i]:
                result.append(numero)
                if len(result) == k:
                    return result        
        
        