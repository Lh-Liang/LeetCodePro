#
# @lc app=leetcode id=3435 lang=python3
#
# [3435] Frequencies of Shortest Supersequences
#

# @lc code=start
from typing import List

class Solution:
    def supersequences(self, words: List[str]) -> List[List[int]]:
        nodes = sorted(list(set("".join(words))))
        n = len(nodes)
        idx = {char: i for i, char in enumerate(nodes)}
        
        adj = [0] * n
        for w in words:
            u, v = idx[w[0]], idx[w[1]]
            if u != v:
                adj[u] |= (1 << v)

        def has_cycle(mask):
            # mask represents nodes allowed to be in the DAG (frequency 1)
            # Nodes not in mask are 'doubled' and effectively break cycles
            in_degree = [0] * n
            for i in range(n):
                if not (mask & (1 << i)): continue
                for j in range(n):
                    if (mask & (1 << j)) and (adj[i] & (1 << j)):
                        in_degree[j] += 1
            
            queue = [i for i in range(n) if (mask & (1 << i)) and in_degree[i] == 0]
            count = 0
            while queue:
                u = queue.pop(0)
                count += 1
                for v in range(n):
                    if (mask & (1 << v)) and (adj[u] & (1 << v)):
                        in_degree[v] -= 1
                        if in_degree[v] == 0:
                            queue.append(v)
            
            return count != bin(mask).count('1')

        min_extra = n + 1
        best_masks = []

        # Iterate through all subsets of nodes. 
        # A bit set to 1 means the character appears ONCE.
        # A bit set to 0 means the character appears TWICE.
        # We want to maximize the number of 1s (minimize 0s) such that 1s form a DAG.
        for mask in range(1 << n):
            extra = n - bin(mask).count('1')
            if extra > min_extra:
                continue
            
            if not has_cycle(mask):
                if extra < min_extra:
                    min_extra = extra
                    best_masks = [mask]
                else:
                    best_masks.append(mask)

        results = []
        for mask in best_masks:
            freq = [0] * 26
            for i in range(n):
                char_idx = ord(nodes[i]) - ord('a')
                freq[char_idx] = 1 if (mask & (1 << i)) else 2
            results.append(freq)
            
        return results
# @lc code=end