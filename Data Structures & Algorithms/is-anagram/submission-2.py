class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        vistos_s = {}
        vistos_t = {}
        for letter in s:
            if letter not in vistos_s:
                vistos_s[letter] = 1
            else:
                vistos_s[letter] += 1

        for letter in t:
            if letter not in vistos_t:
                vistos_t[letter] = 1
            else:
                vistos_t[letter] += 1

        if vistos_s == vistos_t:
            return True
        else:
            return False
        