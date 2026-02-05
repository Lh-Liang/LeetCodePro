#
# @lc app=leetcode id=3575 lang=java
#
# [3575] Maximum Good Subtree Score
#

# @lc code=start
import java.util.*;
class Solution {
    private static final int MOD = 1_000_000_007;

    // Helper: extract digit mask from value, ensure correctness for all values
    private int getDigitMask(int val) {
        int mask = 0;
        while (val > 0) {
            int d = val % 10;
            mask |= (1 << d);
            val /= 10;
        }
        return mask;
    }

    public int goodSubtreeSum(int[] vals, int[] par) {
        int n = vals.length;
        List<Integer>[] tree = new ArrayList[n];
        for (int i = 0; i < n; ++i) tree[i] = new ArrayList<>();
        for (int i = 1; i < n; ++i) tree[par[i]].add(i);

        int[] maxScore = new int[n];
        dfs(0, vals, tree, maxScore);
        long total = 0;
        for (int score : maxScore) total = (total + score) % MOD;
        return (int) total;
    }

    // DFS: For each node, maintain map: digitMask -> maxSum
    private Map<Integer, Integer> dfs(int u, int[] vals, List<Integer>[] tree, int[] maxScore) {
        Map<Integer, Integer> dp = new HashMap<>();
        int selfMask = getDigitMask(vals[u]);
        // Handle repeated digits in value: only include node itself if digits are unique
        if (Integer.bitCount(selfMask) == String.valueOf(vals[u]).length()) {
            dp.put(selfMask, vals[u]);
        }
        for (int v : tree[u]) {
            Map<Integer, Integer> childDP = dfs(v, vals, tree, maxScore);
            Map<Integer, Integer> newDP = new HashMap<>(dp);
            // Break down merging for verifiability
            for (Map.Entry<Integer, Integer> e1 : dp.entrySet()) {
                int mask1 = e1.getKey(), sum1 = e1.getValue();
                for (Map.Entry<Integer, Integer> e2 : childDP.entrySet()) {
                    int mask2 = e2.getKey(), sum2 = e2.getValue();
                    // Only merge if masks do not overlap
                    if ((mask1 & mask2) == 0) {
                        int mergedMask = mask1 | mask2;
                        int mergedSum = sum1 + sum2;
                        // Update if merged sum is greater; verify no digit overlap
                        newDP.put(mergedMask, Math.max(newDP.getOrDefault(mergedMask, 0), mergedSum));
                    }
                }
            }
            // Also consider childDP entries alone (in case parent dp is empty)
            for (Map.Entry<Integer, Integer> e : childDP.entrySet()) {
                int mask = e.getKey(), sum = e.getValue();
                newDP.put(mask, Math.max(newDP.getOrDefault(mask, 0), sum));
            }
            dp = newDP;
        }
        // Maximum among all digit masks is the good subset score for this node
        int max = 0;
        for (int v : dp.values()) max = Math.max(max, v);
        // Edge case: if no good subset, ensure at least 0
        maxScore[u] = max;
        return dp;
    }
}
# @lc code=end