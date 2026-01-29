#
# @lc app=leetcode id=3435 lang=python3
#
# [3435] Frequencies of Shortest Supersequences
#

# @lc code=start
from typing import List

class Solution:
    def supersequences(self, words: List[str]) -> List[List[int]]:
        unique_chars = sorted(list(set(''.join(words))))
        n = len(unique_chars)
        char_to_idx = {c: i for i, c in enumerate(unique_chars)}
        
        # Characters with self-loops (e.g., "aa") must appear at least twice
        # These cannot be part of any induced DAG subset
        has_self_loop = [False] * n
        adj_mask = [0] * n
        
        for w in words:
            u, v = w[0], w[1]
            idx_u, idx_v = char_to_idx[u], char_to_idx[v]
            if idx_u == idx_v:
                has_self_loop[idx_u] = True
            else:
                adj_mask[idx_u] |= (1 << idx_v)
        
        # Candidate nodes for the DAG are those without self-loops
        candidates = [i for i in range(n) if not has_self_loop[i]]
        nc = len(candidates)
        # Map candidate index back to original index
        c_to_orig = {i: candidates[i] for i in range(nc)}
        
        # Build adjacency for candidate nodes only
        c_adj = [0] * nc
        for i in range(nc):
            orig_i = c_to_orig[i]
            for j in range(nc):
                orig_j = c_to_orig[j]
                if (adj_mask[orig_i] >> orig_j) & 1:
                    c_adj[i] |= (1 << j)

        # is_dag[mask] will be true if the subset represented by mask is a DAG
        is_dag = [False] * (1 << nc)
        is_dag[0] = True
        max_dag_size = 0
        
        # Standard DP for Induced DAG: a set S is a DAG if there exists v in S 
        # such that v has no outgoing edges to any other node in S.
        for mask in range(1, 1 << nc):
            for i in range(nc):
                if (mask >> i) & 1:
                    # Check if node i has no outgoing edges to other nodes in the current mask
                    if not (c_adj[i] & mask):
                        if is_dag[mask ^ (1 << i)]:
                            is_dag[mask] = True
                            size = bin(mask).count('1')
                            if size > max_dag_size:
                                max_dag_size = size
                            break
        
        results = []
        for mask in range(1 << nc):
            if is_dag[mask] and bin(mask).count('1') == max_dag_size:
                freq = [0] * 26
                # Convert candidate mask to original character indices
                dag_indices = set()
                for i in range(nc):
                    if (mask >> i) & 1:
                        dag_indices.add(c_to_orig[i])
                
                for i in range(n):
                    char_idx = ord(unique_chars[i]) - ord('a')
                    # Frequency is 1 if in the max DAG, 2 otherwise
                    freq[char_idx] = 1 if i in dag_indices else 2
                results.append(freq)
                
        return results
# @lc code=end