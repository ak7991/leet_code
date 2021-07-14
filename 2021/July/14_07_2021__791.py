class Solution:
    def customSortString(self, order: str, str: str) -> str:
        ch_order = [-1] * 26
        ch_occ = []
        for i, ch in enumerate(order):
            ch_order[ord(ch)-97] = i
            ch_occ.append([ord(ch)-97, 0])
        unwanted = ""
        for ch in str:
            occ_idx = ch_order[ord(ch)-97]
            if occ_idx == -1:
                unwanted += ch
            else:
                ch_occ[occ_idx][1] += 1
        # print(ch_occ)
        ans = ""
        for ch in ch_occ:
            ans += chr(ch[0]+97) * ch[1]
        ans += unwanted
        return ans