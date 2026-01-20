#
# @lc app=leetcode id=3538 lang=python3
#
# [3538] Merge Operations for Minimum Travel Time
#

# @lc code=start
class Solution:
    def minTravelTime(self, l: int, n: int, k: int, position: List[int], time: List[int]) -> int:
        # n is up to 50
        # k is up to n-2
        # sum(time) <= 100
        # We need to perform exactly k merges.
        # This means we keep exactly (n - k) signs.
        # Indices 0 and n-1 are always kept.
        # We need to select (n - k - 2) internal signs to keep.
        
        # DP state: dp[merges_done][last_kept_index][current_rate]
        # merges_done: Number of merges performed so far (0 to k)
        # last_kept_index: The index in 'position' of the last kept sign (0 to n-2)
        # current_rate: The effective time/km for the segment starting at last_kept_index.
        #               This rate is determined by the sum of 'time' values of signs merged into last_kept_index.
        #               Specifically, if we keep u and then v, the rate at v will be sum(time[k] for k in u+1...v).
        #               Wait, the rate at u determines the cost of segment u->v.
        #               The rate at v is determined by the transition u->v for the NEXT segment.
        
        # Dimensions:
        # merges_done: k + 1
        # last_kept_index: n
        # current_rate: 101 (since sum(time) <= 100)
        
        # Initialize DP table with infinity
        import math
        inf = math.inf
        dp = [[[inf] * 102 for _ in range(n)] for _ in range(k + 1)]
        
        # Base case:
        # Start at index 0. 0 merges done. Rate is time[0].
        # Cost is 0 initially.
        if time[0] <= 100:
            dp[0][0][time[0]] = 0
        
        # Prefix sums for time to quickly calculate sum(time[u+1...v])
        # P[x] = sum(time[0]...time[x-1])
        P = [0] * (n + 1)
        for i in range(n):
            P[i+1] = P[i] + time[i]
            
        ans = inf
        
        # Iterate through states
        # Topological order: merges m, then index u
        for m in range(k + 1):
            for u in range(n - 1): # u cannot be n-1 because n-1 is the destination, not a start point for a new segment in DP
                for r in range(1, 102):
                    current_cost = dp[m][u][r]
                    if current_cost == inf:
                        continue
                    
                    # Try to transition to next kept index v
                    # v must be > u
                    # The number of merges added is (v - u - 1)
                    # We can iterate v starting from u+1
                    
                    # Optimization: max possible v is limited by remaining allowed merges
                    # remaining merges = k - m
                    # needed = v - u - 1
                    # v - u - 1 <= k - m  =>  v <= k - m + u + 1
                    max_v = min(n - 1, k - m + u + 1)
                    
                    for v in range(u + 1, max_v + 1):
                        needed = v - u - 1
                        next_m = m + needed
                        
                        # Cost for segment u -> v
                        dist = position[v] - position[u]
                        segment_cost = dist * r
                        
                        if v == n - 1:
                            # Reached destination
                            # We must have used exactly k merges
                            if next_m == k:
                                if current_cost + segment_cost < ans:
                                    ans = current_cost + segment_cost
                        else:
                            # Calculate new rate for segment starting at v
                            # New rate is sum(time[u+1...v])
                            # Indices in P: P[v+1] - P[u+1]
                            next_r = P[v+1] - P[u+1]
                            
                            if next_r <= 100:
                                if current_cost + segment_cost < dp[next_m][v][next_r]:
                                    dp[next_m][v][next_r] = current_cost + segment_cost
                                    
        return ans if ans != inf else -1

# @lc code=end