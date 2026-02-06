#
# @lc app=leetcode id=3474 lang=java
#
# [3474] Lexicographically Smallest Generated String
#
# @lc code=start
class Solution {
    public String generateString(String str1, String str2) {
        // Initialize variables
        int n = str1.length();
        int m = str2.length();
        StringBuilder result = new StringBuilder();
        // Iterate over each position in str1
        for (int i = 0; i <= n - m; i++) {
            if (str1.charAt(i) == 'T') {
                // Place str2 at this position if 'T' is found
                result.append(str2);
            } else { // 'F' condition requires ensuring this substring not match str2
                // Add the lexicographically smallest valid character sequence that is not equal to str2 at this position.
                for (int j = 0; j < m; j++) {
                    if (j + i < result.length()) {
                        continue; // Skip already filled parts from previous "T" placements.
                    } else { 
                        char c = 'a'; 
                        while ((c == str2.charAt(j)) && c <= 'z') { 
                            c++; // Ensure different character from corresponding position in str2. 
                        } 
                        result.append(c); 
                    } 
                } 
            } 
        } 
        return result.toString(); 
    } 
}
# @lc code=end