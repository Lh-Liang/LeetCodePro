#
# @lc app=leetcode id=3435 lang=python3
#
# [3435] Frequencies of Shortest Supersequences
#

# @lc code=start
class Solution:
    def supersequences(self, words: List[str]) -> List[List[int]]:
        unique_chars = sorted(list(set("".join(words))))
        n = len(unique_chars)
        char_to_idx = {c: i for i, c in enumerate(unique_chars)}
        
        # preds[v] stores bitmask of nodes u such that u -> v is an edge
        preds = [0] * n
        for w in words:
            u, v = char_to_idx[w[0]], char_to_idx[w[1]]
            preds[v] |= (1 << u)
            
        # can_be_dag[mask] is True if the subset of nodes in mask forms a DAG
        can_be_dag = [False] * (1 << n)
        can_be_dag[0] = True
        
        max_mask_size = 0
        
        for mask in range(1, 1 << n):
            m = mask
            while m > 0:
                # Get the index of the lowest set bit
                i = (m & -m).bit_length() - 1
                # If node i has no incoming edges from nodes within the current mask,
                # it can be a source in the topological sort of this mask.
                if not (preds[i] & mask):
                    if can_be_dag[mask ^ (1 << i)]:
                        can_be_dag[mask] = True
                        break
                m &= m - 1
            
            if can_be_dag[mask]:
                size = bin(mask).count('1')
                if size > max_mask_size:
                    max_mask_size = size
        
        results = []
        for mask in range(1 << n):
            if can_be_dag[mask] and bin(mask).count('1') == max_mask_size:
                freq = [0] * 26
                # Characters in mask have frequency 1 in the SCS
                # Characters in unique_chars but not in mask have frequency 2
                for i in range(n):
                    char_idx = ord(unique_chars[i]) - ord('a')
                    if (mask >> i) & 1:
                        freq[char_idx] = 1
                    else:
                        freq[char_idx] = 2
                results.append(freq)
                
        return results
# @lc code=end