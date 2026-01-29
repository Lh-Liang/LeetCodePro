#
# @lc app=leetcode id=3509 lang=python3
#
# [3509] Maximum Product of Subsequences With an Alternating Sum Equal to K
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int], k: int, limit: int) -> int:
        # dp[sum][parity] = set of possible products
        # parity 0: even length, parity 1: odd length
        dp = {}
        
        for x in nums:
            new_updates = []
            
            # Case 1: Start a new subsequence with x (always parity 1)
            if x <= limit:
                new_updates.append((x, 1, x))
            
            # Case 2: Extend existing subsequences
            for (s, p), products in dp.items():
                # If current parity is 1 (odd), next element is at an odd index (subtracted)
                # If current parity is 0 (even), next element is at an even index (added)
                ns = s - x if p == 1 else s + x
                np = 1 - p
                
                for prod in products:
                    nprod = prod * x
                    if nprod <= limit:
                        new_updates.append((ns, np, nprod))
            
            # Apply updates to dp
            for ns, np, nprod in new_updates:
                state = (ns, np)
                if state not in dp:
                    dp[state] = {nprod}
                else:
                    dp[state].add(nprod)
                    
        ans = -1
        # Check both parities for the target alternating sum k
        for p in [0, 1]:
            if (k, p) in dp:
                ans = max(ans, max(dp[(k, p)]))
        
        return ans
# @lc code=end