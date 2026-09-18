class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longitud_minima = len(strs[0])
        for palabra in strs:
            if len(palabra) < longitud_minima:
                longitud_minima = len(palabra)

        prefijo = ""
        for i in range(longitud_minima):
            for palabra in strs:
                if palabra[i] != strs[0][i]:
                    return prefijo
            prefijo += strs[0][i]
        return prefijo
        