#
# @lc app=leetcode id=3474 lang=cpp
#
# [3474] Lexicographically Smallest Generated String
#

# @lc code=start
class Solution {
public:
    string generateString(string str1, string str2) {
        int n = str1.length(), m = str2.length();
        string result(n + m - 1, 'a'); // initialize with 'a', which is smallest lexicographically
        for (int i = 0; i <= n - 1; ++i) {
            if (str1[i] == 'T') {
                result.replace(i, m, str2); // place str2 at position i
            } else { // when str1[i] == 'F'
                for (int j = 0; j < m; ++j) {
                    if (result[i + j] == str2[j]) {
                        result[i + j] = (str2[j] == 'z') ? 'y' : 'z'; // change to avoid matching str2
                    }
                }
            }
        }
        return result; // return constructed result
    }
};
# @lc code=end