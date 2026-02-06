#
# @lc app=leetcode id=3399 lang=java
#
# [3399] Smallest Substring With Identical Characters II
#

# @lc code=start
class Solution {
    public int minLength(String s, int numOps) {
        int n = s.length();
        int left = 1, right = n;
        int answer = n;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (canAchieve(s, numOps, mid)) {
                answer = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return answer;
    }
    // Check if we can make all runs of identical chars of length <= len with numOps flips
    private boolean canAchieve(String s, int numOps, int len) {
        // Try both: making all substrings at most len by flipping to '0' or '1'
        return minFlips(s, '0', len) <= numOps || minFlips(s, '1', len) <= numOps;
    }
    // For given char c, compute minimal flips to make all substrings of c of length <= len
    private int minFlips(String s, char c, int len) {
        int n = s.length();
        int flips = 0;
        int i = 0;
        while (i < n) {
            if (s.charAt(i) != c) {
                i++;
                continue;
            }
            int j = i;
            while (j < n && s.charAt(j) == c) j++;
            int runLen = j - i;
            if (runLen > len) {
                // Need to flip at least (runLen-1)/len substrings inside this run
                flips += (runLen - 1) / len;
            }
            i = j;
        }
        return flips;
    }
}
# @lc code=end