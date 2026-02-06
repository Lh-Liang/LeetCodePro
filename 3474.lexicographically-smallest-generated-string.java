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
        char[] word = new char[len];
        boolean[] fixed = new boolean[len];
        // Step 1: For 'T' positions, set forced characters
        for (int i = 0; i < n; ++i) {
            if (str1.charAt(i) == 'T') {
                for (int j = 0; j < m; ++j) {
                    int idx = i + j;
                    if (fixed[idx]) {
                        if (word[idx] != str2.charAt(j)) {
                            return "";
                        }
                    } else {
                        word[idx] = str2.charAt(j);
                        fixed[idx] = true;
                    }
                }
            }
        }
        // Step 2: For 'F' positions, ensure substring is not str2
        for (int i = 0; i < n; ++i) {
            if (str1.charAt(i) == 'F') {
                boolean match = true;
                for (int j = 0; j < m; ++j) {
                    int idx = i + j;
                    char c = fixed[idx] ? word[idx] : 'a';
                    if (c != str2.charAt(j)) {
                        match = false;
                        break;
                    }
                }
                if (match) {
                    // Try to change the last character lexicographically
                    int idx = i + m - 1;
                    char orig = fixed[idx] ? word[idx] : 'a';
                    char rep = (orig == 'z') ? 'a' : (char)(orig + 1);
                    if (rep == str2.charAt(m - 1)) {
                        if (rep == 'z') {
                            return "";
                        }
                        rep = (char)(rep + 1);
                        if (rep > 'z') return "";
                    }
                    word[idx] = rep;
                    fixed[idx] = true;
                }
            }
        }
        // Step 3: Fill unset positions with 'a'
        for (int i = 0; i < len; ++i) {
            if (!fixed[i]) {
                word[i] = 'a';
            }
        }
        return new String(word);
    }
}
# @lc code=end