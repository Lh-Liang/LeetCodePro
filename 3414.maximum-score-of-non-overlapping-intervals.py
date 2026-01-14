#
# @lc app=leetcode id=3414 lang=python3
#
# [3414] Maximum Score of Non-overlapping Intervals
#

# @lc code=start
class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        import bisect
        
        n = len(intervals)
        
        # indexed[i] = (end, start, weight, original_index)
        indexed = sorted([(intervals[i][1], intervals[i][0], intervals[i][2], i) for i in range(n)])
        
        ends = [x[0] for x in indexed]
        
        INF = float('inf')
        
        # dp[i][k] = (neg_weight, sorted_indices_tuple)
        # Using negative weight so min() picks higher weights
        # For equal weights, smaller indices tuple is preferred
        dp = [[(0, ())] + [(INF, ())] * 4 for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            end_i, start_i, weight_i, orig_idx_i = indexed[i - 1]
            # Find largest j such that ends[j] < start_i
            prev_j = bisect.bisect_left(ends, start_i) - 1
            
            for k in range(5):
                # Option 1: Don't include interval i-1
                opt1 = dp[i - 1][k]
                
                # Option 2: Include interval i-1
                if k > 0 and dp[prev_j + 1][k - 1][0] != INF:
                    prev_neg_w, prev_idx = dp[prev_j + 1][k - 1]
                    new_neg_w = prev_neg_w - weight_i
                    new_idx = tuple(sorted(prev_idx + (orig_idx_i,)))
                    opt2 = (new_neg_w, new_idx)
                else:
                    opt2 = (INF, ())
                
                dp[i][k] = min(opt1, opt2)
        
        best = (INF, ())
        for k in range(1, 5):
            best = min(best, dp[n][k])
        
        return list(best[1])
# @lc code=end