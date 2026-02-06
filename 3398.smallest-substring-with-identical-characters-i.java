#
# @lc app=leetcode id=3398 lang=java
#
# [3398] Smallest Substring With Identical Characters I
#

# @lc code=start
class Solution {
    public int minLength(String s, int numOps) {
        int n = s.length();
        int left = 1, right = n;
        while (left < right) {
            int mid = (left + right) / 2;
            if (canAchieve(s, numOps, mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
    private boolean canAchieve(String s, int numOps, int maxLen) {
        int flips = 0;
        int n = s.length();
        int i = 0;
        while (i < n) {
            int j = i;
            while (j < n && s.charAt(j) == s.charAt(i)) j++;
            int len = j - i;
            if (len > maxLen) {
                // Need to break this run into pieces of at most maxLen
                flips += (len - 1) / maxLen;
            }
            i = j;
        }
        return flips <= numOps;
    }
}
# @lc code=end