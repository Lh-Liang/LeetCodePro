#
# @lc app=leetcode id=3441 lang=python3
#
# [3441] Minimum Cost Good Caption
#

# @lc code=start
class Solution:
    def minCostGoodCaption(self, caption: str) -> str:
        n = len(caption)
        if n < 3:
            return ""
        
        # dp[i] stores the minimum cost to make the suffix caption[i:] valid
        dp = [float('inf')] * (n + 1)
        dp[n] = 0
        
        # path[i] stores (char_code, length) for the optimal choice at index i
        path = [None] * (n + 1)
        
        # Precompute ordinals for faster access
        ords = [ord(c) for c in caption]
        
        # We iterate backwards from the last possible start index
        for i in range(n - 3, -1, -1):
            best_cost = float('inf')
            best_char_code = -1
            best_k = -1
            
            for char_code in range(97, 123): # 'a' through 'z'
                # Calculate cost for the first group of 3 characters
                if i + 3 > n:
                    break
                
                current_cost = 0
                # Base cost for length 3
                current_cost += abs(ords[i] - char_code)
                current_cost += abs(ords[i+1] - char_code)
                current_cost += abs(ords[i+2] - char_code)
                
                # Try group lengths 3, 4, 5
                # We check valid transitions. A transition is valid if dp[i+k] is not infinity.
                
                # Length 3
                if dp[i+3] != float('inf'):
                    total = current_cost + dp[i+3]
                    if total < best_cost:
                        best_cost = total
                        best_char_code = char_code
                        best_k = 3
                    elif total == best_cost:
                        # Tie-breaking logic handled implicitly by loop order for char_code
                        # If char_code > best_char_code, we don't switch (we want lexicographically smallest)
                        # If char_code == best_char_code (unlikely in this loop structure as char_code is unique per iteration)
                        # Wait, we are inside char_code loop. So char_code is currently expanding.
                        # We only need to compare with previously stored best for THIS i.
                        # Since char_code increases, if total == best_cost, we prefer the smaller char_code (already stored).
                        # So strictly < is correct to maintain smallest char_code.
                        pass

                # Length 4
                if i + 4 <= n:
                    current_cost += abs(ords[i+3] - char_code)
                    if dp[i+4] != float('inf'):
                        total = current_cost + dp[i+4]
                        if total < best_cost:
                            best_cost = total
                            best_char_code = char_code
                            best_k = 4
                        elif total == best_cost:
                            # Tie-breaking for same cost
                            # Since we are in the same char_code iteration, this means char_code == best_char_code
                            # We need to decide between best_k (previous) and k=4 (current)
                            # Rule: compare next char of suffix
                            
                            # Retrieve the starting char of the suffix for the stored best_k
                            # path[i+best_k] is (next_char_code, next_len)
                            # Note: i+best_k is a valid start index, so path[i+best_k] is populated.
                            
                            # If i+best_k == n, then suffix is empty. But if k=4 is valid, then i+4 <= n.
                            # If i+best_k == n, then k=4 implies i+4 > n (since 4 > 3 usually, or 5 > 4).
                            # So if best_k reaches end, we can't extend further, so this block won't be entered for larger k.
                            # Thus path[i+best_k] is safe.
                            
                            next_char = path[i+best_k][0]
                            if next_char > char_code:
                                # The suffix starts with a larger char than current.
                                # Extending current char (smaller) is better.
                                best_k = 4
                
                # Length 5
                if i + 5 <= n:
                    current_cost += abs(ords[i+4] - char_code)
                    if dp[i+5] != float('inf'):
                        total = current_cost + dp[i+5]
                        if total < best_cost:
                            best_cost = total
                            best_char_code = char_code
                            best_k = 5
                        elif total == best_cost:
                            # Same logic as k=4
                            next_char = path[i+best_k][0]
                            if next_char > char_code:
                                best_k = 5
            
            dp[i] = best_cost
            path[i] = (best_char_code, best_k)
            
        if dp[0] == float('inf'):
            return ""
            
        # Reconstruct the string
        res = []
        curr = 0
        while curr < n:
            code, k = path[curr]
            res.append(chr(code) * k)
            curr += k
            
        return "".join(res)
# @lc code=end