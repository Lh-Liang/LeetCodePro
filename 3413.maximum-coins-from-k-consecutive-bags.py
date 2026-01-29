#
# @lc app=leetcode id=3413 lang=python3
#
# [3413] Maximum Coins From K Consecutive Bags
#

# @lc code=start
class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        coins.sort()
        n = len(coins)
        
        def get_max(segments, k):
            m = len(segments)
            ans = 0
            current_sum = 0
            right = 0
            
            # Prefix sums of (r - l + 1) * c for full segments
            prefix_coins = [0] * (m + 1)
            for i in range(m):
                l, r, c = segments[i]
                prefix_coins[i+1] = prefix_coins[i] + (r - l + 1) * c
            
            for left in range(m):
                l_start, r_start, c_start = segments[left]
                window_end = l_start + k - 1
                
                # Move right pointer to the last segment that starts within the window
                while right < m and segments[right][0] <= window_end:
                    right += 1
                
                # Full segments are from index 'left' to 'right - 2'
                # The segment at 'right - 1' might be partially covered
                full_segments_sum = prefix_coins[right-1] - prefix_coins[left]
                
                # Partial segment at right-1
                last_idx = right - 1
                l_last, r_last, c_last = segments[last_idx]
                partial_sum = (min(r_last, window_end) - l_last + 1) * c_last
                
                ans = max(ans, full_segments_sum + partial_sum)
            return ans

        # Case 1: Window starts at the beginning of a segment
        res1 = get_max(coins, k)
        
        # Case 2: Window ends at the end of a segment
        # Transform: [l, r, c] -> [-r, -l, c] and sort to reuse the 'start' logic
        reversed_coins = sorted([[-r, -l, c] for l, r, c in coins])
        res2 = get_max(reversed_coins, k)
        
        return max(res1, res2)
# @lc code=end