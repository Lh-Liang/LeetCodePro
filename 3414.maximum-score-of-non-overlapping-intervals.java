#
# @lc app=leetcode id=3414 lang=java
#
# [3414] Maximum Score of Non-overlapping Intervals
#
# @lc code=start
import java.util.*;
class Solution {
    public int[] maximumWeight(List<List<Integer>> intervals) {
        int n = intervals.size();
        // Pair: [l, r, w, original index]
        int[][] arr = new int[n][4];
        for (int i = 0; i < n; ++i) {
            arr[i][0] = intervals.get(i).get(0);
            arr[i][1] = intervals.get(i).get(1);
            arr[i][2] = intervals.get(i).get(2);
            arr[i][3] = i;
        }
        Arrays.sort(arr, Comparator.comparingInt(a -> a[1]));
        // pred[i]: index of last non-overlapping interval before i, or -1
        int[] pred = new int[n];
        for (int i = 0; i < n; ++i) {
            int l = arr[i][0];
            int lo = 0, hi = i - 1, ans = -1;
            while (lo <= hi) {
                int mid = (lo + hi) / 2;
                if (arr[mid][1] < l) {
                    ans = mid; lo = mid + 1;
                } else {
                    hi = mid - 1;
                }
            }
            pred[i] = ans;
        }
        // DP: dp[i][k] = [score, indices...]
        // We use TreeMap to store at each (i, k) a pair of [score, indices list]
        // But since k <= 4, we can keep a 2D table.
        int maxK = 4;
        long[][] dp = new long[n+1][maxK+1];
        int[][][] idx = new int[n+1][maxK+1][maxK];
        for (int i = 0; i <= n; ++i) for (int k = 0; k <= maxK; ++k) dp[i][k] = Long.MIN_VALUE;
        dp[0][0] = 0; // No interval, score 0
        for (int i = 1; i <= n; ++i) {
            for (int k = 0; k <= maxK; ++k) {
                // skip i-1
                if (dp[i-1][k] > dp[i][k] || (dp[i-1][k] == dp[i][k] && compare(idx[i-1][k], idx[i][k]) < 0)) {
                    dp[i][k] = dp[i-1][k];
                    System.arraycopy(idx[i-1][k], 0, idx[i][k], 0, maxK);
                }
                // take i-1
                if (k > 0) {
                    int pi = pred[i-1]+1;
                    if (dp[pi][k-1] != Long.MIN_VALUE) {
                        long cand = dp[pi][k-1] + arr[i-1][2];
                        int[] candIdx = new int[maxK];
                        System.arraycopy(idx[pi][k-1], 0, candIdx, 0, maxK);
                        candIdx[k-1] = arr[i-1][3];
                        Arrays.sort(candIdx, 0, k);
                        if (cand > dp[i][k] || (cand == dp[i][k] && compare(candIdx, idx[i][k]) < 0)) {
                            dp[i][k] = cand;
                            System.arraycopy(candIdx, 0, idx[i][k], 0, maxK);
                        }
                    }
                }
            }
        }
        long best = Long.MIN_VALUE; int bestK = 0, bestI = n;
        for (int k = 1; k <= maxK; ++k) {
            if (dp[n][k] > best || (dp[n][k] == best && compare(idx[n][k], idx[bestI][bestK]) < 0)) {
                best = dp[n][k]; bestK = k;
            }
        }
        int[] res = Arrays.copyOf(idx[n][bestK], bestK);
        Arrays.sort(res);
        return res;
    }
    // Compare two int arrays lexicographically up to their length
    private int compare(int[] a, int[] b) {
        for (int i = 0; i < a.length; ++i) {
            if (a[i] != b[i]) return Integer.compare(a[i], b[i]);
        }
        return 0;
    }
}
# @lc code=end