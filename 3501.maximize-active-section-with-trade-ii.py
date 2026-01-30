#
# @lc app=leetcode id=3501 lang=python3
#
# [3501] Maximize Active Section with Trade II
#
# @lc code=start
class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        res = []
        for li, ri in queries:
            sub = s[li:ri+1]
            # Augment with '1' on both ends
            t = '1' + sub + '1'
            n = len(t)
            # Find all blocks and their types
            blocks = []
            i = 0
            while i < n:
                j = i
                while j < n and t[j] == t[i]:
                    j += 1
                blocks.append((t[i], i, j-1))
                i = j
            # Count initial '1's (excluding augmentation)
            base_ones = sub.count('1')
            max_ones = base_ones
            # Try all possible trades
            for idx, (char, l, r) in enumerate(blocks):
                if char != '0':
                    continue
                # Surrounded '0's block means previous and next blocks are '1'
                if idx > 0 and idx < len(blocks)-1:
                    if blocks[idx-1][0] == '1' and blocks[idx+1][0] == '1':
                        zero_block_len = r - l + 1
                        # Find any surrounded block of '1's to swap
                        for jdx, (c2, l2, r2) in enumerate(blocks):
                            if c2 != '1':
                                continue
                            if jdx > 0 and jdx < len(blocks)-1:
                                if blocks[jdx-1][0] == '0' and blocks[jdx+1][0] == '0':
                                    one_block_len = r2 - l2 + 1
                                    # After trade: lose one_block_len '1's, gain zero_block_len '1's
                                    new_ones = base_ones - one_block_len + zero_block_len
                                    if new_ones > max_ones:
                                        max_ones = new_ones
                        # If no surrounded '1's, we can only gain
                        if max_ones == base_ones:
                            new_ones = base_ones + zero_block_len
                            if new_ones > max_ones:
                                max_ones = new_ones
            res.append(max_ones)
        return res
# @lc code=end