#
# @lc app=leetcode id=3579 lang=java
#
# [3579] Minimum Steps to Convert String with Operations
#
# @lc code=start
class Solution {
    public int minOperations(String word1, String word2) {
        int n = word1.length();
        Integer[][] memo = new Integer[n + 1][n + 1];
        return dp(0, n, word1, word2, memo);
    }
    
    // DP to solve for substring [start, end)
    private int dp(int start, int end, String w1, String w2, Integer[][] memo) {
        if (start == end) return 0;
        if (memo[start][end] != null) return memo[start][end];
        String s1 = w1.substring(start, end);
        String s2 = w2.substring(start, end);
        if (s1.equals(s2)) {
            memo[start][end] = 0;
            return 0;
        }
        int minOps = end - start; // At most all replaces
        // Try all possible partitions
        for (int mid = start + 1; mid < end; ++mid) {
            int left = dp(start, mid, w1, w2, memo);
            int right = dp(mid, end, w1, w2, memo);
            minOps = Math.min(minOps, left + right);
        }
        // Try all operation orders for this substring
        int ops = minForSubstring(s1, s2);
        minOps = Math.min(minOps, ops);
        // Try reverse first, then swap/replace
        String reversed = new StringBuilder(s1).reverse().toString();
        int opsAfterReverse = 1 + minForSubstring(reversed, s2);
        minOps = Math.min(minOps, opsAfterReverse);
        memo[start][end] = minOps;
        return minOps;
    }

    // For a given pair of substrings, enumerate all permutations of swap and replace, and pick minimal
    private int minForSubstring(String s1, String s2) {
        if (s1.equals(s2)) return 0;
        // Try only replaces
        int replaces = 0;
        for (int i = 0; i < s1.length(); ++i) {
            if (s1.charAt(i) != s2.charAt(i)) replaces++;
        }
        // Try only swaps (using cycle decomposition)
        int swaps = minSwapsToMatch(s1, s2);
        // Try swaps + replaces (for positions that can't be matched by swaps)
        int minOps = Math.min(replaces, swaps);
        // Try swap then replace (cycle decomposition leaves mismatches)
        int[] afterSwap = mismatchesAfterSwaps(s1, s2);
        int swapsWithR = afterSwap[0];
        int leftReplace = afterSwap[1];
        minOps = Math.min(minOps, swapsWithR + leftReplace);
        return minOps;
    }

    // Returns minimum swaps required to match s1 to s2, or Integer.MAX_VALUE if not possible
    private int minSwapsToMatch(String s1, String s2) {
        char[] a = s1.toCharArray();
        char[] b = s2.toCharArray();
        int n = a.length;
        boolean[] visited = new boolean[n];
        int swaps = 0;
        for (int i = 0; i < n; i++) {
            if (visited[i] || a[i] == b[i]) continue;
            int j = i, cycle = 0;
            while (!visited[j]) {
                visited[j] = true;
                // Find b[j] in a[]
                int next = -1;
                for (int k = 0; k < n; ++k) {
                    if (!visited[k] && a[k] == b[j] && b[k] != a[k]) {
                        next = k;
                        break;
                    }
                }
                if (next == -1) break;
                j = next;
                cycle++;
            }
            if (cycle > 0) swaps += cycle;
        }
        // Check if after swaps all positions match; if not, return Integer.MAX_VALUE
        for (int i = 0; i < n; ++i) {
            if (a[i] != b[i]) return Integer.MAX_VALUE;
        }
        return swaps;
    }

    // Applies swap cycles, returns [swaps performed, remaining mismatches after swaps]
    private int[] mismatchesAfterSwaps(String s1, String s2) {
        char[] a = s1.toCharArray();
        char[] b = s2.toCharArray();
        int n = a.length;
        boolean[] visited = new boolean[n];
        int swaps = 0, mismatches = 0;
        for (int i = 0; i < n; i++) {
            if (visited[i] || a[i] == b[i]) continue;
            int j = i, cycle = 0;
            while (!visited[j]) {
                visited[j] = true;
                // Find b[j] in a[]
                int next = -1;
                for (int k = 0; k < n; ++k) {
                    if (!visited[k] && a[k] == b[j] && b[k] != a[k]) {
                        next = k;
                        break;
                    }
                }
                if (next == -1) break;
                j = next;
                cycle++;
            }
            if (cycle > 0) swaps += cycle;
        }
        for (int i = 0; i < n; ++i) {
            if (a[i] != b[i]) mismatches++;
        }
        return new int[]{swaps, mismatches};
    }
}
# @lc code=end