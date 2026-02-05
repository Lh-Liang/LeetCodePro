/*
 * @lc app=leetcode id=3455 lang=java
 *
 * [3455] Shortest Matching Substring
 */
// @lc code=start
class Solution {
    public int shortestMatchingSubstring(String s, String p) {
        int n = s.length();
        int firstStar = p.indexOf('*');
        int secondStar = p.indexOf('*', firstStar + 1);
        String prefix = p.substring(0, firstStar);
        String middle = p.substring(firstStar + 1, secondStar);
        String suffix = p.substring(secondStar + 1);
        // Special case: pattern is just '**'
        if (prefix.isEmpty() && middle.isEmpty() && suffix.isEmpty()) {
            return 0;
        }
        int minLen = Integer.MAX_VALUE;
        for (int i = 0; i <= n - prefix.length(); ++i) {
            if (!prefix.isEmpty() && !s.startsWith(prefix, i)) continue;
            int prefixEnd = i + prefix.length();
            // Suffix must be after prefix
            for (int j = prefixEnd; j <= n - suffix.length(); ++j) {
                if (!suffix.isEmpty() && !s.startsWith(suffix, j)) continue;
                int candidateStart = i;
                int candidateEnd = j + suffix.length();
                if (candidateEnd > n) continue;
                // Check middle
                boolean middleMatch = false;
                if (middle.isEmpty()) {
                    middleMatch = true;
                } else {
                    // Search for middle in [prefixEnd, j] (inclusive)
                    int midSearchStart = Math.max(prefixEnd, candidateStart);
                    int midSearchEnd = Math.min(j, n - middle.length());
                    for (int midPos = midSearchStart; midPos <= midSearchEnd; ++midPos) {
                        if (s.startsWith(middle, midPos)) {
                            middleMatch = true;
                            break;
                        }
                    }
                }
                if (middleMatch) {
                    int len = candidateEnd - candidateStart;
                    if (len < minLen) minLen = len;
                }
            }
        }
        return minLen == Integer.MAX_VALUE ? -1 : minLen;
    }
}
// @lc code=end