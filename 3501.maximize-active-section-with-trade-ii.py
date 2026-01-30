#
# @lc app=leetcode id=3501 lang=python3
#
# [3501] Maximize Active Section with Trade II
#
# @lc code=start
class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        def find_surrounded_blocks(t: str, char: str) -> List[tuple]:
            # Returns list of (start, end) indices of contiguous char-blocks surrounded by opposite char
            n = len(t)
            blocks = []
            i = 0
            while i < n:
                if t[i] == char:
                    j = i
                    while j < n and t[j] == char:
                        j += 1
                    left = i-1 >= 0 and t[i-1] != char
                    right = j < n and t[j] != char
                    if left and right:
                        blocks.append((i, j-1))
                    i = j
                else:
                    i += 1
            return blocks

        def count_sections(t: str) -> int:
            cnt = 0
            i = 0
            n = len(t)
            while i < n:
                if t[i] == '1':
                    cnt += 1
                    while i < n and t[i] == '1':
                        i += 1
                else:
                    i += 1
            return cnt

        res = []
        for li, ri in queries:
            sub = s[li:ri+1]
            t = '1' + sub + '1'
            n = len(t)
            # Step 1: Baseline answer (no trade)
            best = count_sections(t[1:-1])
            # Step 2: Find all '1'-blocks surrounded by '0'
            one_blocks = find_surrounded_blocks(t, '1')
            # Step 3: For each eligible trade, simulate only if it can improve result
            for l, r in one_blocks:
                t2 = list(t)
                for k in range(l, r+1):
                    t2[k] = '0'
                # Step 4: Find all '0'-blocks surrounded by '1' in t2
                zero_blocks = find_surrounded_blocks(''.join(t2), '0')
                for zl, zr in zero_blocks:
                    t3 = t2[:]
                    for k in range(zl, zr+1):
                        t3[k] = '1'
                    # Step 5: Final count, verify boundaries
                    ans = count_sections(''.join(t3[1:-1]))
                    if ans > best:
                        best = ans
            # Step 6: Final verification step (optional assertion)
            res.append(best)
        return res
# @lc code=end