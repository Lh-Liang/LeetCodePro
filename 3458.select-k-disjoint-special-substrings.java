#
# @lc app=leetcode id=3458 lang=java
#
# [3458] Select K Disjoint Special Substrings
#
# @lc code=start
class Solution {
    public boolean maxSubstringLength(String s, int k) {
        int n = s.length();
        if (k == 0) return true;
        int[] first = new int[26];
        int[] last = new int[26];
        for (int i = 0; i < 26; ++i) {
            first[i] = -1;
            last[i] = -1;
        }
        for (int i = 0; i < n; ++i) {
            int idx = s.charAt(i) - 'a';
            if (first[idx] == -1) first[idx] = i;
            last[idx] = i;
        }
        int count = 0;
        int i = 0;
        while (i < n) {
            int start = i;
            int end = last[s.charAt(i) - 'a'];
            int j = i;
            while (j < end) {
                end = Math.max(end, last[s.charAt(j) - 'a']);
                ++j;
            }
            // Verify all characters in [start, end] are unique to this substring
            boolean valid = true;
            for (int x = start; x <= end; ++x) {
                int idx = s.charAt(x) - 'a';
                if (first[idx] < start || last[idx] > end) {
                    valid = false;
                    break;
                }
            }
            // The substring should not be the whole string and must satisfy uniqueness
            if (valid && (start > 0 || end < n - 1)) {
                count++;
            }
            i = end + 1;
        }
        return count >= k;
    }
}
# @lc code=end