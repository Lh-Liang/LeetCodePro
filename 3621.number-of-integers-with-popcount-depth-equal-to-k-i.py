#
# @lc app=leetcode id=3621 lang=python3
#
# [3621] Number of Integers With Popcount-Depth Equal to K I
#

# @lc code=start
import math

class Solution:
    def popcountDepth(self, n: int, k: int) -> int:
        if k == 0:
            return 1 # Only x=1 has depth 0
        
        # Precompute depth for values up to the max possible popcount of n
        # n <= 10^15, so max popcount is < 64.
        # D(1) = 0, D(x) = 1 + D(popcount(x))
        depths = [0] * 65
        depths[1] = 0
        for i in range(2, 65):
            depths[i] = 1 + depths[bin(i).count('1')]
            
        # Find which popcounts 'c' lead to a total depth of k
        # If D(x) = k, then D(popcount(x)) must be k-1
        target_popcounts = [c for c in range(1, 65) if depths[c] == k - 1]
        
        def count_with_popcount(limit: int, target_bits: int) -> int:
            """Counts integers in [1, limit] with exactly target_bits set."""
            if target_bits < 0: return 0
            count = 0
            current_bits = 0
            # Iterate through bits from MSB to LSB
            binary_str = bin(limit)[2:]
            length = len(binary_str)
            
            for i, bit in enumerate(binary_str):
                if bit == '1':
                    # If we set this bit to 0, we can pick remaining bits freely from lower positions
                    remaining_pos = length - 1 - i
                    needed = target_bits - current_bits
                    if 0 <= needed <= remaining_pos:
                        count += math.comb(remaining_pos, needed)
                    current_bits += 1
            
            # Check if the number 'limit' itself matches
            if current_bits == target_bits:
                count += 1
            return count

        total_count = 0
        for c in target_popcounts:
            total_count += count_with_popcount(n, c)
            
        # Edge case: if k=1, target_popcounts includes c=1 (since D(1)=0).
        # count_with_popcount(n, 1) counts x=1, but D(1) is 0, not 1.
        if k == 1:
            total_count -= 1
            
        return total_count
# @lc code=end