#
# @lc app=leetcode id=3509 lang=java
#
# [3509] Maximum Product of Subsequences With an Alternating Sum Equal to K
#
# @lc code=start
import java.util.*;
class Solution {
    public int maxProduct(int[] nums, int k, int limit) {
        int n = nums.length;
        // dp[i][altSum][parity] = max product (at index i, altSum, parity)
        Map<Integer, Map<Integer, Integer>>[] dp = new HashMap[n+1];
        for (int i = 0; i <= n; i++) {
            dp[i] = new HashMap<>();
        }
        // Base: before any elements, altSum = 0, parity = 0 (even, next is even)
        dp[0].computeIfAbsent(0, x -> new HashMap<>()).put(0, 1); // product 1, but must select at least one later
        int res = -1;
        for (int i = 0; i < n; i++) {
            for (Map.Entry<Integer, Map<Integer, Integer>> entry : dp[i].entrySet()) {
                int altSum = entry.getKey();
                for (Map.Entry<Integer, Integer> sub : entry.getValue().entrySet()) {
                    int parity = sub.getKey();
                    int prod = sub.getValue();
                    // Option 1: skip nums[i]
                    dp[i+1].computeIfAbsent(altSum, x -> new HashMap<>()).merge(parity, prod, Math::max);
                    // Option 2: take nums[i]
                    int newSum = altSum + (parity == 0 ? nums[i] : -nums[i]);
                    int newProd = prod * nums[i];
                    if (nums[i] == 0 && prod != 0) newProd = 0; // handle 0 multiplication
                    if (newProd > limit) continue;
                    dp[i+1].computeIfAbsent(newSum, x -> new HashMap<>()).merge(1 - parity, newProd, Math::max);
                }
            }
        }
        // At the end, scan all dp[n][k][*] for product > 1 (subsequence must be non-empty)
        for (int p = 0; p <= 1; p++) {
            if (dp[n].containsKey(k) && dp[n].get(k).containsKey(p)) {
                int val = dp[n].get(k).get(p);
                if (val > 1 && val <= limit) {
                    res = Math.max(res, val);
                }
                // Special: single element case, product==0 is allowed
                if (val == 0 && limit >= 0 && k == 0) {
                    res = Math.max(res, 0);
                }
            }
        }
        // Also check for single element subsequence
        for (int i = 0; i < n; i++) {
            int alt = nums[i];
            int prod = nums[i];
            if (prod <= limit && alt == k) {
                res = Math.max(res, prod);
            }
        }
        return res;
    }
}
# @lc code=end