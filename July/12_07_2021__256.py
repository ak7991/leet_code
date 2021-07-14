class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping_s_t = [-1] * 128
        mapping_t_s = [-1] * 128
        i = 0
        len_s = len(s)
        len_t = len(t)
        if len_s != len_t:
            return False
        while i < len(s):
            s_ord = ord(s[i])
            t_ord = ord(t[i])
            if mapping_s_t[s_ord] == -1 and mapping_t_s[t_ord] == -1:
                mapping_s_t[s_ord] = t_ord
                mapping_t_s[t_ord] = s_ord
            elif mapping_s_t[s_ord] != t_ord or mapping_t_s[t_ord] != s_ord:
                return False            
            i += 1
        return True