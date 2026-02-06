#
# @lc app=leetcode id=3575 lang=java
#
# [3575] Maximum Good Subtree Score
#

# @lc code=start
import java.util.*;

class Solution {
    static final int MOD = 1000000007;
    public int goodSubtreeSum(int[] vals, int[] par) {
        int n = vals.length;
        List<Integer>[] tree = new ArrayList[n];
        for (int i = 0; i < n; ++i) tree[i] = new ArrayList<>();
        for (int i = 1; i < n; ++i) {
            tree[par[i]].add(i);
        }
        int[] maxScore = new int[n];
        dfs(0, vals, tree, maxScore);
        long sum = 0;
        for (int score : maxScore) sum = (sum + score) % MOD;
        return (int)sum;
    }

    // Returns: Map<bitmask, sum> for subtree rooted at u
    private Map<Integer, Integer> dfs(int u, int[] vals, List<Integer>[] tree, int[] maxScore) {
        Map<Integer, Integer> dp = new HashMap<>();
        int mask = digitMask(vals[u]);
        dp.put(mask, vals[u]);
        for (int v : tree[u]) {
            Map<Integer, Integer> childDP = dfs(v, vals, tree, maxScore);
            Map<Integer, Integer> newDP = new HashMap<>(dp);
            for (Map.Entry<Integer, Integer> e1 : dp.entrySet()) {
                int m1 = e1.getKey(), s1 = e1.getValue();
                for (Map.Entry<Integer, Integer> e2 : childDP.entrySet()) {
                    int m2 = e2.getKey(), s2 = e2.getValue();
                    if ((m1 & m2) == 0) {
                        int nm = m1 | m2;
                        int ns = s1 + s2;
                        newDP.put(nm, Math.max(newDP.getOrDefault(nm, 0), ns));
                    }
                }
            }
            // Add all child-only masks (for cases where we don't select current node)
            for (Map.Entry<Integer, Integer> e : childDP.entrySet()) {
                newDP.putIfAbsent(e.getKey(), e.getValue());
            }
            dp = newDP;
        }
        int max = 0;
        for (int v : dp.values()) max = Math.max(max, v);
        maxScore[u] = max;
        return dp;
    }

    // Returns bitmask of digits present in x
    private int digitMask(int x) {
        int mask = 0;
        while (x > 0) {
            mask |= 1 << (x % 10);
            x /= 10;
        }
        return mask;
    }
}
# @lc code=end