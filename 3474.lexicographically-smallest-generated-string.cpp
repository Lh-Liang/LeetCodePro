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
        string result(n + m - 1, 'a'); // initialize with smallest character
        
        for (int i = 0; i < n; ++i) {
            if (str1[i] == 'T') {
                for (int j = 0; j < m; ++j) {
                    if (i + j >= result.size()) return ""; // out of bounds
                    result[i + j] = str2[j]; // place str2
                }
            } else { // str1[i] == 'F'
                bool conflict = true;
                for (int j = 0; j < m && i + j < result.size(); ++j) {
                    if (result[i + j] != str2[j]) {
                        conflict = false;
                        break;
                    }
                }
                if (conflict) {
                    // Modify one character minimally to ensure it's not equal
                    if (i + m - 1 < result.size()) {
                        result[i + m - 1] = result[i + m - 1] == 'z' ? 'y' : result[i + m - 1] + 1;
                    } else {
                        return ""; // can't resolve conflict within bounds
                    }
                }
            }
        }
        
        return result;
    }
};
# @lc code=end