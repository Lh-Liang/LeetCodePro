#
# @lc app=leetcode id=3474 lang=java
#
# [3474] Lexicographically Smallest Generated String
#

# @lc code=start
class Solution {
    public String generateString(String str1, String str2) {
        int n = str1.length();
        int m = str2.length();
        int len = n + m - 1;
        char[] res = new char[len];
        // Fill with placeholder
        for (int i = 0; i < len; ++i) res[i] = '?';
        // 1. Enforce all 'T' constraints
        for (int i = 0; i < n; ++i) {
            if (str1.charAt(i) == 'T') {
                for (int j = 0; j < m; ++j) {
                    int idx = i + j;
                    if (res[idx] == '?') {
                        res[idx] = str2.charAt(j);
                    } else if (res[idx] != str2.charAt(j)) {
                        return ""; // Conflict
                    }
                }
            }
        }
        // 2. Enforce all 'F' constraints
        for (int i = 0; i < n; ++i) {
            if (str1.charAt(i) == 'F') {
                boolean same = true;
                for (int j = 0; j < m; ++j) {
                    int idx = i + j;
                    if (res[idx] != '?' && res[idx] != str2.charAt(j)) {
                        same = false;
                        break;
                    }
                }
                if (same) {
                    boolean changed = false;
                    for (int j = m - 1; j >= 0; --j) {
                        int idx = i + j;
                        for (char c = 'a'; c <= 'z'; ++c) {
                            if (c != str2.charAt(j) && (res[idx] == '?' || res[idx] == str2.charAt(j))) {
                                // Check this change does not violate any 'T' constraint
                                boolean conflict = false;
                                for (int k = Math.max(0, idx - m + 1); k <= Math.min(n - 1, idx); ++k) {
                                    if (str1.charAt(k) == 'T') {
                                        int off = idx - k;
                                        if (off >= 0 && off < m && str2.charAt(off) != c) {
                                            conflict = true;
                                            break;
                                        }
                                    }
                                }
                                if (!conflict) {
                                    res[idx] = c;
                                    changed = true;
                                    break;
                                }
                            }
                        }
                        if (changed) break;
                    }
                    if (!changed) return "";
                }
            }
        }
        // 3. Fill remaining positions with 'a' (or minimal valid char)
        for (int i = 0; i < len; ++i) {
            if (res[i] == '?') res[i] = 'a';
        }
        // 4. Final verification of all constraints
        for (int i = 0; i < n; ++i) {
            String sub = new String(res, i, m);
            if (str1.charAt(i) == 'T') {
                if (!sub.equals(str2)) return "";
            } else {
                if (sub.equals(str2)) return "";
            }
        }
        return new String(res);
    }
}
# @lc code=end