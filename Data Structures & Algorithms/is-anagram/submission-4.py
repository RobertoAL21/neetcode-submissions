class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        conteo = {}

        for letter in s:
            if letter not in conteo:
                conteo[letter] = 1
            else:
                conteo[letter] += 1

        for letter in t:
            if letter in conteo:
                conteo[letter] -= 1
            else:
                conteo[letter] = 1

        for value in conteo.values():
            if value != 0:
                return False
        return True 

        