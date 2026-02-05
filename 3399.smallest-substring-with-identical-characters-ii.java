//
// @lc app=leetcode id=3399 lang=java
//
// [3399] Smallest Substring With Identical Characters II
//
// @lc code=start
class Solution {
    public int minLength(String s, int numOps) {
        int n = s.length();
        int left = 1, right = n;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (isPossible(s, numOps, mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
    // Check if all runs can be broken into pieces of length <= len with numOps flips
    private boolean isPossible(String s, int numOps, int len) {
        int flips = 0;
        int i = 0, n = s.length();
        while (i < n) {
            char ch = s.charAt(i);
            int j = i;
            while (j < n && s.charAt(j) == ch) j++;
            int runLen = j - i;
            if (runLen > len) {
                flips += (runLen - 1) / len;
            }
            i = j;
        }
        return flips <= numOps;
    }
}
// @lc code=end