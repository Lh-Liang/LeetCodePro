#
# @lc app=leetcode id=3474 lang=cpp
#
# [3474] Lexicographically Smallest Generated String
#

# @lc code=start
class Solution {
public:
    string generateString(string str1, string str2) {
        int n = str1.length();
        int m = str2.length();
        int len = n + m - 1;
        
        string word(len, '?');
        
        // Process 'T' constraints
        for (int i = 0; i < n; i++) {
            if (str1[i] == 'T') {
                for (int j = 0; j < m; j++) {
                    if (word[i + j] == '?') {
                        word[i + j] = str2[j];
                    } else if (word[i + j] != str2[j]) {
                        return "";  // Conflict
                    }
                }
            }
        }
        
        // Check 'F' constraints and identify "at risk" ones
        vector<int> atRisk;
        for (int i = 0; i < n; i++) {
            if (str1[i] == 'F') {
                bool allFixed = true;
                bool allMatch = true;
                for (int j = 0; j < m; j++) {
                    if (word[i + j] == '?') {
                        allFixed = false;
                        if (str2[j] != 'a') {
                            allMatch = false;
                        }
                    } else if (word[i + j] != str2[j]) {
                        allMatch = false;
                    }
                }
                if (allMatch) {
                    if (allFixed) {
                        return "";  // Impossible
                    }
                    atRisk.push_back(i);
                }
            }
        }
        
        // Greedy: cover at-risk constraints
        vector<bool> mustChange(len, false);
        int lastChange = -1;
        for (int i : atRisk) {
            if (lastChange >= i && lastChange < i + m) {
                // Already covered by a previous change
                continue;
            }
            // Find rightmost unfixed position in [i, i+m-1]
            for (int j = m - 1; j >= 0; j--) {
                if (word[i + j] == '?') {
                    mustChange[i + j] = true;
                    lastChange = i + j;
                    break;
                }
            }
        }
        
        // Fill in the word
        for (int k = 0; k < len; k++) {
            if (word[k] == '?') {
                word[k] = mustChange[k] ? 'b' : 'a';
            }
        }
        
        return word;
    }
};
# @lc code=end