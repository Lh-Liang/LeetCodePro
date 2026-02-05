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
        char[] word = new char[n + m - 1];
        Arrays.fill(word, 'a'); // Start with smallest possible letters
        
        for (int i = 0; i < n; i++) {
            if (str1.charAt(i) == 'T') {
                // Ensure substring matches str2
                if (i + m > word.length) return ""; // Bounds check
                for (int j = 0; j < m; j++) {
                    word[i + j] = str2.charAt(j);
                }
            } else {
                // Ensure substring does not match str2 by checking possible conflicts
                boolean adjusted = false;
                for (int j = 0; j < m && i + j < word.length; j++) {
                    if (word[i + j] == str2.charAt(j)) {
                        // Adjust character minimally to avoid match without disrupting lexicographical order
                        for (char c = 'a'; c <= 'z'; c++) {
                            if (c != str2.charAt(j)) { // Find a non-matching character
                                word[i + j] = c;
                                adjusted = true;
                                break;
                            }
                        }
                    }
                }
                if (!adjusted && i + m <= word.length) {
                    for (char c = 'a'; c <= 'z'; c++) { // Adjust first position minimally if no adjustment made yet
                        if (c != word[i]) {
                            word[i] = c;
                            break;
                        }
                    }
                }
            }
        }
        return new String(word);
    }
}
# @lc code=end