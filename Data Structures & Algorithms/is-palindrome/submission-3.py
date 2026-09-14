class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_cleaned = ""
        for char in s:
            if char.isalnum():
                s_cleaned += char.lower()
        print(s_cleaned)

        i = 0
        j = len(s_cleaned)-1

        while i < j:
            if s_cleaned[i] != s_cleaned[j]:
                return False
            i += 1
            j -= 1
        return True

        