#
# @lc app=leetcode id=3399 lang=java
#
# [3399] Smallest Substring With Identical Characters II
#
# @lc code=start
class Solution {
    public int minLength(String s, int numOps) {
        int n = s.length();
        int[] left = new int[n];
        int[] right = new int[n];
        left[0] = (s.charAt(0) == '1') ? 1 : 0;
        right[n - 1] = (s.charAt(n - 1) == '1') ? 1 : 0;
        for (int i = 1; i < n; i++) {
            left[i] = (s.charAt(i) == '1') ? left[i - 1] + 1 : 0;
        }
        for (int i = n - 2; i >= 0; i--) {
            right[i] = (s.charAt(i) == '1') ? right[i + 1] + 1 : 0;
        }
        int maxOnesBlock = 0;
        for (int i = 0; i < n; i++) {
            maxOnesBlock = Math.max(maxOnesBlock, Math.max(left[i], right[i]));
        }
        return Math.max(maxOnesBlock - numOps, 1); 
    } 
}
# @lc code=end