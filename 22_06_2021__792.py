from typing import List

class Solution:
    def append_to_dict(self, words_dict, word, count=1):
        if word == "":
            return words_dict
        # print("first letter ", word, "not in ", words_dict)
        if word[0] not in words_dict:
            words_dict[word[0]] = {word: count}
        else:
            if word not in words_dict[word[0]]:
                words_dict[word[0]][word] = count
            else:
                words_dict[word[0]][word] += count
        # print("updated ", words_dict)
        return words_dict
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        ans = 0
        words_dict = {}
        for word in words:
            words_dict = self.append_to_dict(words_dict, word)
            # print("gotten: ", words_dict)
        print(">>",words_dict)
        for c in s:
            # print("next letter: ", c, words_dict)
            if c in words_dict:
                words_to_pop = words_dict.pop(c)
                for w, count in words_to_pop.items():
                    if w[1:] == "":
                        print("just add to count", count, w, words_to_pop)
                        ans += count
                    else:
                        # print("changing ", w, " to ", w[1:])
                        words_dict = self.append_to_dict(words_dict, w[1:], count)
        return ans

if __name__ == "__main__":
    sol = Solution()
    s = "abcde"
    words = ["a","bb","acd","ace"]
    print(sol.numMatchingSubseq(s, words))