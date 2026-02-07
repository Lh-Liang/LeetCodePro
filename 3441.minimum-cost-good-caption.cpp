#
# @lc app=leetcode id=3441 lang=cpp
#
# [3441] Minimum Cost Good Caption
#

# @lc code=start
class Solution {
public:
    string minCostGoodCaption(string caption) {
        int n = caption.size();
        if (n < 3) return ""; // Impossible if less than 3 chars in total.
        
        string result;
        int i = 0;
        
        while (i < n) {
            char currentChar = caption[i];
            int start = i;
            
            // Count consecutive occurrences of current character
            while (i < n && caption[i] == currentChar) {
                i++;
            }
            int count = i - start;
            
            // Process each group based on its count
            if (count >= 3) {
                result.append(count, currentChar);
            } else {
                // Need more characters to make it a valid group
                int needed = 3 - count;
                // Attempt minimal lexicographical adjustments
                if (currentChar > 'a') { // Prefer decreasing first for smaller lexicographical order
                    result.append(3, currentChar - 1);
                } else if (currentChar < 'z') { // Otherwise increase if not possible to decrease
                    result.append(3, currentChar + 1);
                } else {
                    return ""; // If no valid transformation is possible due to boundary constraints.
                }
            }
        }
        return result;
    }
};
# @lc code=end