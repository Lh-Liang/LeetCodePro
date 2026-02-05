#
# @lc app=leetcode id=3470 lang=java
#
# [3470] Permutations IV
#

# @lc code=start
import java.util.*;
class Solution {
    public int[] permute(int n, long k) {
        // Use a boolean array to track used numbers for scalability
        boolean[] used = new boolean[n + 1];
        int[] res = new int[n];
        // Memoization cache: (usedKey, lastParity) -> count
        Map<String, Long> dp = new HashMap<>();
        // Helper to create a scalable key for memoization
        String makeKey(boolean[] used, int lastParity) {
            StringBuilder sb = new StringBuilder();
            for (int i = 1; i <= n; ++i) sb.append(used[i] ? '1' : '0');
            sb.append(',').append(lastParity);
            return sb.toString();
        }
        // DP function: count valid completions from current state
        java.util.function.BiFunction<boolean[], Integer, Long> count = new java.util.function.BiFunction<>() {
            public Long apply(boolean[] usedArr, Integer lastParity) {
                String key = makeKey(usedArr, lastParity);
                if (dp.containsKey(key)) return dp.get(key);
                int usedCount = 0;
                for (int i = 1; i <= n; ++i) if (usedArr[i]) ++usedCount;
                if (usedCount == n) return 1L;
                long total = 0L;
                for (int i = 1; i <= n; ++i) {
                    if (!usedArr[i] && (lastParity == -1 || (i % 2 != lastParity))) {
                        usedArr[i] = true;
                        total += apply(usedArr, i % 2);
                        usedArr[i] = false;
                    }
                }
                dp.put(key, total);
                return total;
            }
        };
        int lastParity = -1;
        for (int pos = 0; pos < n; ++pos) {
            boolean found = false;
            for (int v = 1; v <= n; ++v) {
                if (used[v]) continue;
                if (lastParity != -1 && (v % 2 == lastParity)) continue;
                used[v] = true;
                long c = count.apply(used, v % 2);
                used[v] = false;
                if (c < k) {
                    k -= c;
                } else {
                    res[pos] = v;
                    used[v] = true;
                    lastParity = v % 2;
                    found = true;
                    break;
                }
            }
            if (!found) return new int[0];
        }
        return res;
    }
}
# @lc code=end