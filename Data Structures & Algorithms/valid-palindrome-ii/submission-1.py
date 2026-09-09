class Solution:
    def validPalindrome(self, s: str) -> bool:

        def checkPalindrome(start, end):
            while start < end:
                if s[start] != s[end]:
                    return False

                start += 1
                end -= 1

            return True

        i = 0
        j = len(s) - 1

        while i < j:

            if s[i] == s[j]:
                i += 1
                j -= 1
                continue

            delete_left = checkPalindrome(i + 1, j)
            delete_right = checkPalindrome(i, j - 1)

            if delete_left or delete_right:
                return True

            return False

        return True
        