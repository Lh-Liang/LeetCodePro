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
        int left = 0, right = n;
        while (left < right) {
            int mid = (left + right) / 2;
            if (canReduce(nums, maxC, mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
    // Check if it's possible to make all stable subarrays have length <= k after maxC changes
    private boolean canReduce(int[] nums, int maxC, int k) {
        int n = nums.length;
        int changes = 0;
        // For every possible subarray of length k+1, check if it's stable
        // We can optimize by only considering windows with GCD >= 2
        for (int i = 0; i + k < n; ) {
            int g = nums[i];
            int j = i + 1;
            while (j <= i + k && j < n) {
                g = gcd(g, nums[j]);
                j++;
            }
            if (g >= 2) {
                changes++;
                // To break this window, we can skip to the end of the window
                i = j;
            } else {
                i++;
            }
            if (changes > maxC) return false;
        }
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