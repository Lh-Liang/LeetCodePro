#
# @lc app=leetcode id=3414 lang=python3
#
# [3414] Maximum Score of Non-overlapping Intervals
#

# @lc code=start
class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        # Add original indices and sort by end time
        indexed_intervals = [(intervals[i][0], intervals[i][1], intervals[i][2], i) for i in range(n)]
        indexed_intervals.sort(key=lambda x: x[1])  # Sort by end time
        
        # Extract sorted data
        starts = [interval[0] for interval in indexed_intervals]
        ends = [interval[1] for interval in indexed_intervals]
        weights = [interval[2] for interval in indexed_intervals]
        indices = [interval[3] for interval in indexed_intervals]
        
        # Precompute prev_non_overlap[i] = largest j such that end[j] < start[i]
        import bisect
        prev_non_overlap = [-1] * n
        for i in range(n):
            # Find rightmost j such that ends[j] < starts[i]
            pos = bisect.bisect_left(ends, starts[i])
            if pos > 0:
                prev_non_overlap[i] = pos - 1
        
        # DP[i][k] = maximum weight using at most k intervals from first i intervals
        # parent[i][k] = (choice, prev_i) for backtracking
        DP = [[0] * 5 for _ in range(n + 1)]
        parent = [[(-1, -1)] * 5 for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            curr_idx = i - 1
            prev_idx = prev_non_overlap[curr_idx]
            
            for k in range(5):  # k from 0 to 4
                # Don't take current interval
                DP[i][k] = DP[i-1][k]
                parent[i][k] = (0, i-1)  # 0 means don't take
                
                # Take current interval (if k >= 1)
                if k >= 1:
                    prev_dp_val = DP[prev_idx + 1][k-1] if prev_idx != -1 else (DP[0][k-1] if k-1 == 0 else 0)
                    take_val = prev_dp_val + weights[curr_idx]
                    
                    if take_val > DP[i][k]:
                        DP[i][k] = take_val
                        parent[i][k] = (1, prev_idx + 1)  # 1 means take current
                    elif take_val == DP[i][k]:
                        # For lexicographically smallest, prefer not taking if values are equal
                        # But we need to check which gives lex smaller result
                        pass
        
        # Find best k (0 to 4) and backtrack
        best_k = 0
        for k in range(1, 5):
            if DP[n][k] > DP[n][best_k]:
                best_k = k
        
        # Backtrack to find indices
        result_indices = []
        i = n
        k = best_k
        
        while i > 0 and k > 0:
            choice, prev_i = parent[i][k]
            if choice == 1:  # Take current interval
                curr_idx = i - 1
                result_indices.append(indices[curr_idx])
                prev_idx = prev_non_overlap[curr_idx]
                i = prev_idx + 1 if prev_idx != -1 else 0
                k -= 1
            else:  # Don't take current interval
                i = prev_i
        
        result_indices.sort()
        return result_indices