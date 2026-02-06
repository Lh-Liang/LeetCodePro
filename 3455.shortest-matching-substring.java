#
# @lc app=leetcode id=3455 lang=java
#
# [3455] Shortest Matching Substring
#
# @lc code=start
class Solution {
    public int shortestMatchingSubstring(String s, String p) {
        int n = s.length();
        int m = p.length();
        int firstStar = p.indexOf('*');
        int secondStar = p.indexOf('*', firstStar + 1);
        String prefix = p.substring(0, firstStar);
        String middle = p.substring(firstStar + 1, secondStar);
        String suffix = p.substring(secondStar + 1);
        // Special case: pattern is '**'
        if (prefix.isEmpty() && middle.isEmpty() && suffix.isEmpty()) return 0;
        // Precompute prefix matches
        java.util.List<Integer> prefixMatches = new java.util.ArrayList<>();
        for (int i = 0; i + prefix.length() <= n; ++i) {
            if (s.startsWith(prefix, i)) prefixMatches.add(i);
        }
        // Precompute suffix matches
        java.util.List<Integer> suffixMatches = new java.util.ArrayList<>();
        for (int i = 0; i + suffix.length() <= n; ++i) {
            if (s.startsWith(suffix, i)) suffixMatches.add(i);
        }
        int minLen = Integer.MAX_VALUE;
        // For each prefix match, try to find the smallest matching window with a suffix after it
        for (int start : prefixMatches) {
            int prefixEnd = start + prefix.length();
            // The earliest the suffix can start is prefixEnd + middle.length()
            for (int end : suffixMatches) {
                if (end < prefixEnd) continue;
                int windowEnd = end + suffix.length();
                if (windowEnd > n) continue;
                // The substring between prefixEnd and end must contain middle
                if (prefixEnd <= end) {
                    String between = s.substring(prefixEnd, end);
                    if (between.contains(middle)) {
                        minLen = Math.min(minLen, windowEnd - start);
                        break; // Can't get shorter by trying later suffixes for this prefix
                    }
                }
            }
        }
        return minLen == Integer.MAX_VALUE ? -1 : minLen;
    }
}
# @lc code=end