class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        built = f"{s[0]}"
        c_map = {s[0]: 0}
        left_tether = 0
        max_len = 1
        for i, c in enumerate(s[1:]):
            i = i + 1
            # print(">>", c_map)
            if c not in c_map:
                c_map[c] = i
                built += c
            else:
                discard = s[left_tether:c_map[c] + 1]
                retain = s[c_map[c] + 1:i+1]
                built = retain
                # print("debugging cmap", c_map, discard)
                for _c in discard:
                    c_map.pop(_c)
                c_map[c] = i
                left_tether = c_map[built[0]]
                # print(discard, " + ", built, c_map[c] + 1)
            max_len = max(max_len, len(built))
            # print("built", built)
        return max_len

if __name__ == "__main__":
    sol = Solution()

    print(sol.lengthOfLongestSubstring("abcabcbb"))
    
    print(sol.lengthOfLongestSubstring("bbbbb"))

    print(sol.lengthOfLongestSubstring("pwwkew"))

    print(sol.lengthOfLongestSubstring(" "))