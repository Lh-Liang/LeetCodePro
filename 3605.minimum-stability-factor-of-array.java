#
# @lc app=leetcode id=3605 lang=java
#
# [3605] Minimum Stability Factor of Array
#

# @lc code=start
import java.util.*;
class Solution {
    public int minStable(int[] nums, int maxC) {
        int n = nums.length;
        if (n == 0) return 0;
        if (maxC >= n) return 0;
        int left = 1, right = n, answer = n;
        while (left <= right) {
            int mid = (left + right) / 2;
            if (canDisruptAllStable(nums, maxC, mid)) {
                answer = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return answer;
    }
    // Checks if all stable subarrays of length >= k can be disrupted with at most maxC modifications
    private boolean canDisruptAllStable(int[] nums, int maxC, int k) {
        int n = nums.length;
        // For each subarray of length k, compute its HCF
        // Count how many stable subarrays each index appears in
        int[] coverage = new int[n];
        List<int[]> stableSubarrays = new ArrayList<>();
        for (int i = 0; i <= n - k; i++) {
            int hcf = nums[i];
            for (int j = i + 1; j < i + k; j++) {
                hcf = gcd(hcf, nums[j]);
                if (hcf == 1) break;
            }
            if (hcf >= 2) {
                stableSubarrays.add(new int[]{i, i + k - 1});
                for (int j = i; j < i + k; j++) coverage[j]++;
            }
        }
        if (stableSubarrays.isEmpty()) return true;
        boolean[] disrupted = new boolean[stableSubarrays.size()];
        int mods = 0;
        // Greedily pick the index that disrupts most remaining stable subarrays
        while (true) {
            int maxCover = 0, idx = -1;
            for (int i = 0; i < n; i++) {
                if (coverage[i] > maxCover) {
                    maxCover = coverage[i];
                    idx = i;
                }
            }
            if (maxCover == 0) break; // all disrupted
            mods++;
            if (mods > maxC) return false;
            // Remove all stable subarrays this index disrupts
            for (int si = 0; si < stableSubarrays.size(); si++) {
                if (!disrupted[si]) {
                    int[] rng = stableSubarrays.get(si);
                    if (rng[0] <= idx && idx <= rng[1]) {
                        disrupted[si] = true;
                        for (int j = rng[0]; j <= rng[1]; j++) coverage[j]--;
                    }
                }
            }
        }
        // Verify all stable subarrays are disrupted
        for (boolean b : disrupted) if (!b) return false;
        return true;
    }
    private int gcd(int a, int b) {
        while (b != 0) {
            int t = b;
            b = a % b;
            a = t;
        }
        return a;
    }
}
# @lc code=end