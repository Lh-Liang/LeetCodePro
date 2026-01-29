#
# @lc app=leetcode id=3435 lang=python3
#
# [3435] Frequencies of Shortest Supersequences
#

# @lc code=start
from typing import List

class Solution:
    def supersequences(self, words: List[str]) -> List[List[int]]:
        # Identify all unique characters and map them to indices
        chars = sorted(list(set("".join(words))))
        n = len(chars)
        char_to_idx = {c: i for i, c in enumerate(chars)}
        
        adj = [0] * n
        rev_adj = [0] * n
        self_loops = 0
        
        # Build adjacency lists using bitmasks for efficient set operations
        for w in words:
            u, v = w[0], w[1]
            u_idx, v_idx = char_to_idx[u], char_to_idx[v]
            if u_idx == v_idx:
                self_loops |= (1 << u_idx)
            else:
                adj[u_idx] |= (1 << v_idx)
                rev_adj[v_idx] |= (1 << u_idx)
        
        # dp[mask] will be True if the subgraph induced by nodes in mask is a DAG
        dp = [False] * (1 << n)
        dp[0] = True
        
        max_dag_size = 0
        best_masks = [0]
        
        # Iterate through all possible subsets of characters
        for mask in range(1, 1 << n):
            # Characters with self-loops can never be part of a DAG search space
            if mask & self_loops:
                continue
            
            temp_mask = mask
            while temp_mask:
                # Extract the lowest set bit (lsb) to try a candidate source node
                lsb = temp_mask & -temp_mask
                i = lsb.bit_length() - 1
                
                # If node i has no incoming edges from other nodes in the current mask,
                # then the mask is a DAG if (mask - {i}) is a DAG.
                if not (rev_adj[i] & mask):
                    if dp[mask ^ lsb]:
                        dp[mask] = True
                        break
                
                # Move to the next bit
                temp_mask ^= lsb
            
            # Track masks that form the largest possible induced DAGs
            if dp[mask]:
                size = bin(mask).count('1')
                if size > max_dag_size:
                    max_dag_size = size
                    best_masks = [mask]
                elif size == max_dag_size:
                    best_masks.append(mask)
        
        # Convert each optimal mask into the required frequency array format
        results = []
        for m_mask in best_masks:
            freq = [0] * 26
            for i in range(n):
                c_idx = ord(chars[i]) - ord('a')
                # Nodes in the DAG appear once; others (FVS nodes or self-loops) appear twice
                freq[c_idx] = 1 if (m_mask & (1 << i)) else 2
            results.append(freq)
            
        return results
# @lc code=end