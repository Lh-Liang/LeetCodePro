//
// @lc app=leetcode id=3598 lang=java
//
// [3598] Longest Common Prefix Between Adjacent Strings After Removals
//
// @lc code=start
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
        int[] res = new int[n];
        if (n < 2) {
            for (int i = 0; i < n; i++) res[i] = 0;
            return res;
        }
        int[] prefix = new int[n - 1];
        for (int i = 0; i < n - 1; ++i) {
            prefix[i] = commonPrefix(words[i], words[i+1]);
        }
        for (int i = 0; i < n; ++i) {
            int maxPref = 0;
            if (n == 2) {
                // Only one pair exists, removing either leaves no pairs
                res[i] = 0;
                continue;
            }
            if (i == 0) {
                // Remove first word, pairs are (words[1], words[2]), ..., (words[n-2], words[n-1])
                for (int j = 1; j < n - 1; ++j) {
                    maxPref = Math.max(maxPref, prefix[j]);
                }
            } else if (i == n - 1) {
                // Remove last word, pairs are (words[0], words[1]), ..., (words[n-3], words[n-2])
                for (int j = 0; j < n - 2; ++j) {
                    maxPref = Math.max(maxPref, prefix[j]);
                }
            } else {
                // Remove word at i, new adjacent pair is (words[i-1], words[i+1])
                int newPrefix = commonPrefix(words[i-1], words[i+1]);
                for (int j = 0; j < i - 1; ++j) {
                    maxPref = Math.max(maxPref, prefix[j]);
                }
                maxPref = Math.max(maxPref, newPrefix);
                for (int j = i + 1; j < n - 1; ++j) {
                    maxPref = Math.max(maxPref, prefix[j]);
                }
            }
            res[i] = maxPref;
        }
        // Final check to guarantee output is correct length and values
        if (res.length != n) throw new AssertionError("Result length mismatch.");
        for (int val : res) {
            if (val < 0) throw new AssertionError("Negative prefix length detected.");
        }
        return res;
    }
}
// @lc code=end