#
# @lc app=leetcode id=3598 lang=java
#
# [3598] Longest Common Prefix Between Adjacent Strings After Removals
#

# @lc code=start
class Solution {
    private int commonPrefix(String a, String b) {
        int minLen = Math.min(a.length(), b.length());
        int i = 0;
        while (i < minLen && a.charAt(i) == b.charAt(i)) {
            i++;
        }
        return i;
    }

    public int[] longestCommonPrefix(String[] words) {
        int n = words.length;
        if (n == 1) return new int[]{0};
        int[] prefix = new int[n - 1];
        for (int i = 0; i < n - 1; i++) {
            prefix[i] = commonPrefix(words[i], words[i+1]);
        }
        int max = 0;
        for (int p : prefix) max = Math.max(max, p);
        int[] res = new int[n];
        for (int i = 0; i < n; i++) {
            int curMax;
            if (n == 2) {
                // Only one pair, removing either leaves no pairs
                res[i] = 0;
                continue;
            }
            if (i == 0) {
                // Remove first; pairs from 1 to n-2
                curMax = 0;
                for (int j = 1; j < n - 1; j++) curMax = Math.max(curMax, prefix[j]);
            } else if (i == n - 1) {
                // Remove last; pairs from 0 to n-3
                curMax = 0;
                for (int j = 0; j < n - 2; j++) curMax = Math.max(curMax, prefix[j]);
            } else {
                // Remove in the middle
                int combined = commonPrefix(words[i-1], words[i+1]);
                curMax = 0;
                for (int j = 0; j < n-1; j++) {
                    if (j == i-1) {
                        // This pair is replaced
                        curMax = Math.max(curMax, combined);
                    } else if (j == i) {
                        // This pair is removed
                        continue;
                    } else {
                        curMax = Math.max(curMax, prefix[j]);
                    }
                }
            }
            res[i] = curMax;
        }
        return res;
    }
}
# @lc code=end