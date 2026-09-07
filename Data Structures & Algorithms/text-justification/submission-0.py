class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        i = j = 0

        while i < len(words):
            curr = 0
            left = 0
            while j < len(words):
                curr += len(words[j])
                left += len(words[j])
                if curr == maxWidth:
                    curr -= 1
                    j += 1
                    break
                elif curr > maxWidth:
                    curr -= (len(words[j])+1)
                    left -= len(words[j])
                    break
                curr += 1
                j += 1
            spaces_count = maxWidth - left
            num_pos = j - i - 1
            if j < len(words):
                if num_pos == 0:
                    spaces = [spaces_count]
                else:
                    spaces = [spaces_count // num_pos]*num_pos
                    spaces_count -= (spaces_count // num_pos)*num_pos
                    for k in range(len(spaces)):
                        if spaces_count <= 0:
                            break
                        spaces[k] += 1
                        spaces_count -= 1
                    spaces.append(0)
            else:
                spaces = [1] * num_pos
                spaces.append(maxWidth - left - sum(spaces))

            segment = words[i:j]
            line = []
            for k in range(len(segment)):
                line.append(segment[k])
                line.append(" "* spaces[k])
            ans.append("".join(line))

            i = j

        return ans 
        