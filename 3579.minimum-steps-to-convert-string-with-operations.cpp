#
# @lc app=leetcode id=3579 lang=cpp
#
# [3579] Minimum Steps to Convert String with Operations
#

# @lc code=start
class Solution {
public:
    int minOperations(string word1, string word2) {
        int n = word1.size();
        int operations = 0;
        int i = 0;
        while (i < n) {
            if (word1[i] != word2[i]) {
                int j = i;
                while (j < n && word1[j] != word2[j]) j++;
                // Operations needed for substring word1[i:j]
                int len = j - i;
                if (len == 2) { // Special case optimization for length 2
                    operations += 1; // Either swap or reverse is enough
                } else { 
                    // General case: 3 operations (reverse, replace x2) are enough for any len > 2 
                    operations += 3; 
                } 
                i = j; // Move past this segment 
            } else { 
                i++; 
            } 
        } 
        return operations; 
    } 
}; 
# @lc code=end