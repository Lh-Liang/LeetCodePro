#
# @lc app=leetcode id=3563 lang=java
#
# [3563] Lexicographically Smallest String After Adjacent Removals
#
# @lc code=start
import java.util.*;
class Solution {
    public String lexicographicallySmallestString(String s) {
        Map<String, String> memo = new HashMap<>();
        return dfs(s, memo);
    }
    private String dfs(String s, Map<String, String> memo) {
        if (memo.containsKey(s)) return memo.get(s);
        String minStr = s;
        for (int i = 0; i < s.length() - 1; ++i) {
            if (isConsecutive(s.charAt(i), s.charAt(i+1))) {
                String next = s.substring(0, i) + s.substring(i+2);
                String candidate = dfs(next, memo);
                if (candidate.compareTo(minStr) < 0) {
                    minStr = candidate;
                }
            }
        }
        memo.put(s, minStr);
        return minStr;
    }
    private boolean isConsecutive(char a, char b) {
        int d = Math.abs(a - b);
        return d == 1 || d == 25; // Handles 'a' and 'z' as consecutive
    }
}
# @lc code=end