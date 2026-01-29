#
# @lc app=leetcode id=3509 lang=python3
#
# [3509] Maximum Product of Subsequences With an Alternating Sum Equal to K
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int], k: int, limit: int) -> int:
        # dp: (alternating_sum, length_parity) -> bitmask of achievable products
        # length_parity 1: odd number of elements (next index is odd: 1, 3...)
        # length_parity 0: even number of elements (next index is even: 0, 2...)
        dp = {}
        
        for x in nums:
            # Use a copy to ensure each element is used at most once per subsequence
            new_dp = dp.copy()
            
            # 1. Start a new subsequence (index 0 is even)
            if x <= limit:
                new_dp[(x, 1)] = new_dp.get((x, 1), 0) | (1 << x)
            
            # 2. Extend existing subsequences
            for (s, p), mask in dp.items():
                if p == 1: # Current element is at an odd index (subtract from sum)
                    ns, np = s - x, 0
                else:      # Current element is at an even index (add to sum)
                    ns, np = s + x, 1
                
                if x == 0:
                    new_mask = 1 # Product becomes 0 (set bit 0)
                elif x == 1:
                    new_mask = mask # Product remains the same
                else:
                    # For x >= 2, the product increases; calculate only products <= limit
                    new_mask = 0
                    curr = mask
                    while curr:
                        lsb = curr & -curr
                        p_val = lsb.bit_length() - 1
                        if p_val * x <= limit:
                            new_mask |= (1 << (p_val * x))
                        curr ^= lsb
                
                if new_mask:
                    new_dp[(ns, np)] = new_dp.get((ns, np), 0) | new_mask
            
            dp = new_dp
            
        # Combine masks for both parities at the target sum k
        combined_mask = dp.get((k, 0), 0) | dp.get((k, 1), 0)
        
        # bit_length() - 1 gives the index of the highest set bit (the max product)
        return combined_mask.bit_length() - 1 if combined_mask > 0 else -1
# @lc code=end