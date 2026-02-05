#
# @lc app=leetcode id=3474 lang=cpp
#
# [3474] Lexicographically Smallest Generated String
#

# @lc code=start
class Solution {
public:
    string generateString(string str1, string str2) {
        int n = str1.size(), m = str2.size();
        int L = n + m - 1;
        string word(L, '?');
        // Step 1: enforce 'T' positions
        for (int i = 0; i < n; ++i) {
            if (str1[i] == 'T') {
                for (int j = 0; j < m; ++j) {
                    int pos = i + j;
                    if (word[pos] == '?' || word[pos] == str2[j]) {
                        word[pos] = str2[j];
                    } else {
                        return ""; // conflict
                    }
                }
            }
        }
        // Step 2: handle 'F' positions
        for (int i = 0; i < n; ++i) {
            if (str1[i] == 'F') {
                bool found = false;
                string curr;
                // Try to make the lex smallest substring not equal to str2, respecting already set chars
                for (int k = 0; k < m && !found; ++k) {
                    // Try to change character at position k
                    for (char c = 'a'; c <= 'z'; ++c) {
                        if (c != str2[k]) {
                            bool possible = true;
                            string temp;
                            for (int j = 0; j < m; ++j) {
                                int pos = i + j;
                                char want = (j == k) ? c : str2[j];
                                if (word[pos] != '?' && word[pos] != want) {
                                    possible = false;
                                    break;
                                }
                                temp += want;
                            }
                            if (possible) {
                                // Apply this substring
                                for (int j = 0; j < m; ++j) {
                                    word[i + j] = temp[j];
                                }
                                found = true;
                                break;
                            }
                        }
                    }
                }
                if (!found) return "";
            }
        }
        // Step 3: fill unset positions with 'a'
        for (char& ch : word) if (ch == '?') ch = 'a';
        return word;
    }
};
# @lc code=end