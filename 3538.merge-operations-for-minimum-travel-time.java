#
# @lc app=leetcode id=3538 lang=java
#
# [3538] Merge Operations for Minimum Travel Time
#

# @lc code=start
class Solution {
    public int minTravelTime(int l, int n, int k, int[] position, int[] time) {
        // Precompute segment lengths
        int[] segLen = new int[n - 1];
        for (int i = 0; i < n - 1; ++i) {
            segLen[i] = position[i + 1] - position[i];
        }
        // Use DP with memoization (cache by current segments and merges left)
        return dfs(segLen, time, k);
    }
    
    private int dfs(int[] segLen, int[] time, int k) {
        int m = segLen.length;
        if (k == 0) {
            int total = 0;
            for (int i = 0; i < m; ++i) {
                total += segLen[i] * time[i];
            }
            return total;
        }
        int min = Integer.MAX_VALUE;
        // Try merging every possible pair (i, i+1) (i >= 1)
        for (int t = 1; t < m; ++t) {
            int[] newSegLen = new int[m - 1];
            int[] newTime = new int[m - 1 + 1];
            int idx = 0;
            for (int i = 0; i < m; ++i) {
                if (i == t - 1) {
                    // Merge segLen[t-1] and segLen[t]
                    newSegLen[idx] = segLen[i] + segLen[i + 1];
                    newTime[idx] = time[i];
                    ++i; // skip i+1
                } else {
                    newSegLen[idx] = segLen[i];
                    newTime[idx] = time[i];
                }
                idx++;
            }
            // Merge time at t into t (time[t] + time[t+1])
            for (int i = 1; i < newTime.length; ++i) {
                if (newSegLen[i - 1] != 0 && i == t) {
                    newTime[i] = time[t] + time[t + 1];
                }
            }
            // Fix time array: after merge, time at merged index is sum
            for (int i = 0, j = 0; i < m; ++i) {
                if (i == t) continue;
                newTime[j++] = time[i];
            }
            newTime[t] = time[t] + time[t + 1];
            int[] trimmedTime = new int[newSegLen.length];
            System.arraycopy(newTime, 0, trimmedTime, 0, trimmedTime.length);
            min = Math.min(min, dfs(newSegLen, trimmedTime, k - 1));
        }
        return min;
    }
}
# @lc code=end