#
# @lc app=leetcode id=3441 lang=java
#
# [3441] Minimum Cost Good Caption
#
# @lc code=start
class Solution {
    public String minCostGoodCaption(String caption) {
        int n = caption.length();
        if (n < 3) return "";
        int INF = 1000000000;
        int[][] dp = new int[n + 1][26];
        int[][][] from = new int[n + 1][26][2];
        for (int i = 0; i <= n; ++i)
            for (int c = 0; c < 26; ++c)
                dp[i][c] = INF;
        for (int len = 3; len <= n; ++len) {
            for (int c = 0; c < 26; ++c) {
                int cost = 0;
                for (int j = 0; j < len; ++j) {
                    if (caption.charAt(j) - 'a' != c) cost++;
                }
                dp[len][c] = cost;
                from[len][c][0] = -1;
                from[len][c][1] = -1;
            }
        }
        for (int i = 3; i < n; ++i) {
            for (int c = 0; c < 26; ++c) {
                if (dp[i][c] == INF) continue;
                for (int len = 3; i + len <= n; ++len) {
                    for (int nc = 0; nc < 26; ++nc) {
                        if (nc == c) continue;
                        int cost = 0;
                        for (int j = 0; j < len; ++j) {
                            if (caption.charAt(i + j) - 'a' != nc) cost++;
                        }
                        int total = dp[i][c] + cost;
                        if (total < dp[i + len][nc]) {
                            dp[i + len][nc] = total;
                            from[i + len][nc][0] = i;
                            from[i + len][nc][1] = c;
                        } else if (total == dp[i + len][nc]) {
                            String prev = reconstruct(from, i + len, nc);
                            String curr = reconstruct(from, i + len, nc, i, c, i + len, nc);
                            if (curr.compareTo(prev) < 0) {
                                from[i + len][nc][0] = i;
                                from[i + len][nc][1] = c;
                            }
                        }
                    }
                }
            }
        }
        int best = INF;
        int endC = -1;
        for (int c = 0; c < 26; ++c) {
            if (dp[n][c] < best) {
                best = dp[n][c];
                endC = c;
            }
        }
        if (best == INF) return "";
        StringBuilder sb = new StringBuilder();
        int pos = n, c = endC;
        while (pos > 0) {
            int prev = from[pos][c][0];
            int pc = from[pos][c][1];
            for (int i = prev + 1; i <= pos; ++i) sb.insert(0, (char)('a' + c));
            pos = prev;
            c = pc;
        }
        // Verification step: check that the output meets the requirement
        if (!isGoodCaption(sb.toString())) return "";
        return sb.toString();
    }
    private boolean isGoodCaption(String s) {
        int n = s.length();
        int i = 0;
        while (i < n) {
            int j = i;
            while (j < n && s.charAt(j) == s.charAt(i)) j++;
            if (j - i < 3) return false;
            i = j;
        }
        return true;
    }
    private String reconstruct(int[][][] from, int pos, int c) {
        StringBuilder sb = new StringBuilder();
        int p = pos, cc = c;
        while (p > 0) {
            int prev = from[p][cc][0];
            for (int i = prev + 1; i <= p; ++i) sb.insert(0, (char)('a' + cc));
            cc = from[p][cc][1];
            p = prev;
        }
        return sb.toString();
    }
    private String reconstruct(int[][][] from, int pos, int c, int prev, int pc, int end, int ec) {
        StringBuilder sb = new StringBuilder();
        int p = pos, cc = c;
        while (p > 0) {
            int pr = from[p][cc][0];
            for (int i = pr + 1; i <= p; ++i) sb.insert(0, (char)('a' + cc));
            cc = from[p][cc][1];
            p = pr;
        }
        return sb.toString();
    }
}
# @lc code=end