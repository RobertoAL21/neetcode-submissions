class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        conteo = {}
        for letra in s:
            if letra in conteo:
                conteo[letra] += 1
            else:
                conteo[letra] = 1

        for letra in t:
            if letra in conteo:
                conteo[letra] -= 1
            else:
                return False
        
        for cantidad in conteo.values():
            if cantidad != 0:
                return False
        return True

        