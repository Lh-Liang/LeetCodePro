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
        prefix = []
        starts = []
        ends = []
        total = 0
        for l, r, c in coins:
            starts.append(l)
            ends.append(r)
            total += (r - l + 1) * c
            prefix.append(total)
        max_coins = 0
        # Try using each possible starting bag, which is any l or r-k+1
        # Use only unique possible windows
        positions = set()
        for l, r, c in coins:
            positions.add(l)
            positions.add(r - k + 2)
        positions = [p for p in positions if p is not None]
        for start in positions:
            left = start
            right = start + k - 1
            if left > right:
                continue
            curr = 0
            for l, r, c in coins:
                inter_l = max(l, left)
                inter_r = min(r, right)
                if inter_l <= inter_r:
                    curr += (inter_r - inter_l + 1) * c
            max_coins = max(max_coins, curr)
        return max_coins
# @lc code=end