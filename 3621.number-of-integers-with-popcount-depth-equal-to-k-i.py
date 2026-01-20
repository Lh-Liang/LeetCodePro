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
            # The only number with depth 0 is 1.
            # Since range is [1, n] and n >= 1, the answer is 1.
            return 1

        # Precompute depths for small numbers.
        # Max n is 10^15, which is less than 2^50.
        # The maximum popcount for a number <= 10^15 is roughly 50.
        # We can compute depths up to 60 to be safe.
        
        depth_map = {}
        depth_map[1] = 0
        
        # Function to get depth for small numbers recursively
        def get_depth(val):
            if val in depth_map:
                return depth_map[val]
            # Recursive step: depth(x) = 1 + depth(popcount(x))
            # popcount(val) will be strictly less than val for val > 1
            d = 1 + get_depth(val.bit_count())
            depth_map[val] = d
            return d

        # Fill depth map for possible popcounts (1 to 60)
        for i in range(1, 61):
            get_depth(i)
            
        # We are looking for x in [1, n] such that depth(x) == k.
        # This is equivalent to depth(popcount(x)) == k - 1.
        # Let c = popcount(x). Then we need depth(c) == k - 1.
        # Since x <= n < 2^60, c will be between 1 and 60.
        
        target_popcounts = []
        for c in range(1, 61):
            if depth_map[c] == k - 1:
                target_popcounts.append(c)
        
        if not target_popcounts:
            return 0
            
        # Function to count integers in [1, num] with exactly `cnt` set bits.
        # Using combinatorics logic (Digit DP style without memoization table).
        def count_with_bits(num, cnt):
            if cnt < 0:
                return 0
            if num == 0:
                return 0
            
            s = bin(num)[2:]
            length = len(s)
            res = 0
            current_bits = 0
            
            for i in range(length):
                if s[i] == '1':
                    # If we put '0' at this position:
                    # Remaining positions: length - 1 - i
                    # Bits needed: cnt - current_bits
                    remaining_len = length - 1 - i
                    needed = cnt - current_bits
                    if 0 <= needed <= remaining_len:
                        res += math.comb(remaining_len, needed)
                    
                    # Now assume we put '1' at this position and continue
                    current_bits += 1
            
            # Check the number itself
            if current_bits == cnt:
                res += 1
            
            return res

        total_count = 0
        for c in target_popcounts:
            total_count += count_with_bits(n, c)
            
        return total_count

# @lc code=end