#
# @lc app=leetcode id=3399 lang=java
#
# [3399] Smallest Substring With Identical Characters II
#

# @lc code=start
class Solution {
    public int minLength(String s, int numOps) {
        int n = s.length();
        int maxLen = n;
        for (char target : new char[]{'0', '1'}) {
            int left = 0, right = 0, flipCount = 0;
            while (right < n) {
                if (s.charAt(right) != target) {
                    flipCount++;
                }
                while (flipCount > numOps) {
                    if (s.charAt(left) != target) {
                        flipCount--;
                    }
                    left++;
                }
                maxLen = Math.min(maxLen, right - left + 1);
                right++;
            }
        }
        return maxLen;
    }
}
# @lc code=end