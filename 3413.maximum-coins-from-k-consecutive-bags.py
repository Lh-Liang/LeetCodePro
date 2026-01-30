#
# @lc app=leetcode id=3413 lang=python3
#
# [3413] Maximum Coins From K Consecutive Bags
#

# @lc code=start
class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        # Step 1: Sort the segments by their start position
        coins.sort()
        intervals = []
        prev_end = 0
        for l, r, c in coins:
            # Step 2: Fill gap (if any) with zero-coin interval
            if l > prev_end + 1:
                intervals.append((prev_end + 1, l - 1, 0))
            intervals.append((l, r, c))
            prev_end = r
        # Step 3: Add a trailing gap with zero coins for possible windows starting after last segment
        intervals.append((prev_end + 1, prev_end + k, 0))
        
        # Step 4: Use sliding window over intervals
        from collections import deque
        window = deque()  # Each element: (start, end, coins per bag)
        curr_sum = 0
        curr_len = 0
        max_coins = 0
        idx = 0
        pos = intervals[0][0]
        # Build initial window of size k
        while curr_len < k and idx < len(intervals):
            s, e, c = intervals[idx]
            if pos < s:
                # Fill gap
                gap = min(k - curr_len, s - pos)
                window.append((pos, pos + gap - 1, 0))
                curr_sum += 0
                curr_len += gap
                pos += gap
                if curr_len == k:
                    break
            take = min(e - max(pos, s) + 1, k - curr_len)
            if take > 0:
                window.append((max(pos, s), max(pos, s) + take - 1, c))
                curr_sum += take * c
                curr_len += take
                pos += take
            if pos > e:
                idx += 1
        max_coins = curr_sum
        # Step 5: Slide the window by one bag at a time
        while True:
            # Remove one bag from left
            if not window:
                break
            ws, we, wc = window[0]
            curr_sum -= wc
            curr_len -= 1
            if ws == we:
                window.popleft()
            else:
                window[0] = (ws + 1, we, wc)
            # Add one bag to right
            if pos >= intervals[-1][1] + 1:
                break
            # Find interval containing position pos
            while idx < len(intervals) and not (intervals[idx][0] <= pos <= intervals[idx][1]):
                idx += 1
            if idx < len(intervals):
                _, _, c = intervals[idx]
            else:
                c = 0
            window.append((pos, pos, c))
            curr_sum += c
            curr_len += 1
            pos += 1
            if curr_len == k:
                max_coins = max(max_coins, curr_sum)
        # Step 6: Verification step - all intervals and edge cases have been considered by filling gaps
        return max_coins
# @lc code=end