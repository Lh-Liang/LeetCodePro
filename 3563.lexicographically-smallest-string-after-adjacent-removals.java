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
        if (s.length() <= 1) return s;
        if (memo.containsKey(s)) return memo.get(s);
        String minStr = s;
        for (int i = 0; i < s.length() - 1; ++i) {
            char a = s.charAt(i), b = s.charAt(i + 1);
            if (isConsecutive(a, b)) {
                String next = s.substring(0, i) + s.substring(i + 2);
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
        return Math.abs(a - b) == 1 || (a == 'a' && b == 'z') || (a == 'z' && b == 'a');
    }
}
# @lc code=end