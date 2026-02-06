#
# @lc app=leetcode id=3579 lang=java
#
# [3579] Minimum Steps to Convert String with Operations
#

# @lc code=start
class Solution {
    public int minOperations(String word1, String word2) {
        int n = word1.length();
        Integer[][] memo = new Integer[n][n];
        return dp(word1, word2, 0, n - 1, memo);
    }

    private int dp(String w1, String w2, int l, int r, Integer[][] memo) {
        if (l > r) return 0;
        if (memo[l][r] != null) return memo[l][r];
        int minOps = minOpsForPair(w1.substring(l, r + 1), w2.substring(l, r + 1));
        // Try all possible splits
        for (int m = l; m < r; ++m) {
            int left = dp(w1, w2, l, m, memo);
            int right = dp(w1, w2, m + 1, r, memo);
            minOps = Math.min(minOps, left + right);
        }
        memo[l][r] = minOps;
        return minOps;
    }

    // Compute min ops for two substrings of equal length
    private int minOpsForPair(String s1, String s2) {
        if (s1.equals(s2)) return 0;
        int n = s1.length();
        // Reverse check
        String rev = new StringBuilder(s1).reverse().toString();
        if (rev.equals(s2)) return 1;
        // Swap check (if exactly two mismatches and swapping fixes)
        int[] mismatches = new int[2];
        int mi = 0;
        for (int i = 0; i < n; ++i) {
            if (s1.charAt(i) != s2.charAt(i)) {
                if (mi < 2) mismatches[mi++] = i;
                else break;
            }
        }
        if (mi == 2) {
            char[] arr = s1.toCharArray();
            char tmp = arr[mismatches[0]];
            arr[mismatches[0]] = arr[mismatches[1]];
            arr[mismatches[1]] = tmp;
            if (new String(arr).equals(s2)) return 1;
        }
        // Otherwise, count character mismatches (replace)
        int cnt = 0;
        for (int i = 0; i < n; ++i) {
            if (s1.charAt(i) != s2.charAt(i)) cnt++;
        }
        return cnt;
    }
}
# @lc code=end