class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for words in strs:
            quantity = len(words)
            encoded_string += str(quantity) + "#" + words
        return encoded_string

    def decode(self, s: str) -> List[str]:
        i = 0
        decoded_strs = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            cantidad = int(s[i:j])

            inicio_p = j + 1
            fin_p = j + 1 + cantidad

            word = s[inicio_p:fin_p]
            decoded_strs.append(word)
            i = fin_p
        return decoded_strs



