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
        // dp[parity][sum] = max product
        Map<Integer, Integer>[] dp = new HashMap[2];
        dp[0] = new HashMap<>();
        dp[1] = new HashMap<>();
        for (int i = 0; i < n; ++i) {
            Map<Integer, Integer>[] newDp = new HashMap[2];
            newDp[0] = new HashMap<>(dp[0]);
            newDp[1] = new HashMap<>(dp[1]);
            // Start a new subsequence with nums[i]
            if (nums[i] <= limit) {
                newDp[0].put(nums[i], Math.max(newDp[0].getOrDefault(nums[i], 0), nums[i]));
            }
            // Extend all existing subsequences
            for (int parity = 0; parity < 2; ++parity) {
                for (Map.Entry<Integer, Integer> entry : dp[parity].entrySet()) {
                    int sum = entry.getKey();
                    int prod = entry.getValue();
                    long newProd = (long)prod * nums[i];
                    if (newProd > limit) continue;
                    int newParity = 1 - parity;
                    int newSum = (parity == 0) ? sum - nums[i] : sum + nums[i];
                    int maxProd = Math.max(newDp[newParity].getOrDefault(newSum, 0), (int)newProd);
                    newDp[newParity].put(newSum, maxProd);
                }
            }
            dp = newDp;
        }
        int ans = -1;
        for (int parity = 0; parity < 2; ++parity) {
            if (dp[parity].containsKey(k)) {
                int prod = dp[parity].get(k);
                if (prod <= limit) ans = Math.max(ans, prod);
            }
        }
        return ans;
    }
}
# @lc code=end