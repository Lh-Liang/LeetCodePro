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
        int res = n;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (canBreakAllRuns(s, numOps, mid, '0') || canBreakAllRuns(s, numOps, mid, '1')) {
                res = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return res;
    }
    // Check if all runs of ch can be broken into pieces of length <= len with <= numOps flips
    private boolean canBreakAllRuns(String s, int numOps, int len, char ch) {
        int flipsNeeded = 0;
        int i = 0, n = s.length();
        while (i < n) {
            if (s.charAt(i) != ch) {
                i++;
                continue;
            }
            int j = i;
            while (j < n && s.charAt(j) == ch) j++;
            int runLen = j - i;
            if (runLen > len) {
                flipsNeeded += (runLen - 1) / len;
            }
            i = j;
        }
        return flipsNeeded <= numOps;
    }
}
# @lc code=end