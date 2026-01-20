import collections

class Solution:
    def supersequences(self, words: List[str]) -> List[List[int]]:
        unique_chars = sorted(list(set("".join(words))))
        char_to_idx = {c: i for i, c in enumerate(unique_chars)}
        n = len(unique_chars)
        
        adj = [0] * n
        in_degree_mask = [0] * n
        mandatory_doubled = 0
        
        for w in words:
            u, v = char_to_idx[w[0]], char_to_idx[w[1]]
            if u == v:
                mandatory_doubled |= (1 << u)
            else:
                # Edge u -> v
                if not (adj[u] & (1 << v)):
                    adj[u] |= (1 << v)
                    in_degree_mask[v] |= (1 << u)
        
        # valid_dag[mask] is True if the subgraph induced by the nodes in 'mask' is a DAG
        valid_dag = [False] * (1 << n)
        valid_dag[0] = True
        
        for mask in range(1, 1 << n):
            # Try to find a node 'i' in 'mask' that has 0 in-degree within the induced subgraph
            # i.e., no other node 'j' in 'mask' has an edge j -> i.
            for i in range(n):
                if (mask >> i) & 1:
                    if (in_degree_mask[i] & mask) == 0:
                        # If removing i leaves a valid DAG, then mask is a valid DAG
                        if valid_dag[mask ^ (1 << i)]:
                            valid_dag[mask] = True
                            break
        
        max_single_count = -1
        best_masks = []
        
        # We want to maximize the number of characters that appear once (are in the mask).
        # Characters in the mask have count 1. Characters NOT in the mask have count 2.
        # Condition 1: Mask cannot contain any character that MUST be doubled (mandatory_doubled).
        # Condition 2: The induced subgraph of the mask must be a DAG.
        
        for mask in range(1 << n):
            if (mask & mandatory_doubled) == 0:
                if valid_dag[mask]:
                    cnt = bin(mask).count('1')
                    if cnt > max_single_count:
                        max_single_count = cnt
                        best_masks = [mask]
                    elif cnt == max_single_count:
                        best_masks.append(mask)
        
        results = []
        # It's possible to generate duplicate frequency arrays if multiple masks map to same freqs?
        # No, a mask uniquely determines the counts for the subset of unique_chars.
        # However, we need to map these back to the full 26-char alphabet.
        
        seen_freqs = set()
        
        for mask in best_masks:
            freq = [0] * 26
            # For chars in unique_chars:
            # If in mask -> count 1
            # Else -> count 2
            for i in range(n):
                char_code = ord(unique_chars[i]) - ord('a')
                if (mask >> i) & 1:
                    freq[char_code] = 1
                else:
                    freq[char_code] = 2
            
            # Convert to tuple to store in set
            freq_tuple = tuple(freq)
            if freq_tuple not in seen_freqs:
                seen_freqs.add(freq_tuple)
                results.append(freq)
                
        return results