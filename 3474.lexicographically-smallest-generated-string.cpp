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
        int L = n + m - 1;
        
        // Initialize word with a placeholder. Using 0 (null char) to signify unset.
        string word(L, '\0');
        // Keep track of which positions are fixed by 'T' constraints
        vector<bool> locked(L, false);

        // Step 1: Apply 'T' constraints
        for (int i = 0; i < n; ++i) {
            if (str1[i] == 'T') {
                for (int j = 0; j < m; ++j) {
                    int idx = i + j;
                    if (word[idx] != '\0' && word[idx] != str2[j]) {
                        // Conflict between two 'T' constraints
                        return "";
                    }
                    word[idx] = str2[j];
                    locked[idx] = true;
                }
            }
        }

        // Step 2: Iterate through the word to fill unset characters and satisfy 'F' constraints
        for (int k = 0; k < L; ++k) {
            if (locked[k]) {
                // The character is fixed. We must check if this completes an 'F' constraint window that creates a violation.
                // An 'F' constraint starting at `start` ends at `k` if `start + m - 1 == k` => `start = k - m + 1`.
                int start = k - m + 1;
                if (start >= 0 && str1[start] == 'F') {
                    bool match = true;
                    for (int j = 0; j < m; ++j) {
                        if (word[start + j] != str2[j]) {
                            match = false;
                            break;
                        }
                    }
                    if (match) {
                        // Violation detected, and we cannot change word[k] because it's locked.
                        return "";
                    }
                }
            } else {
                // The character is free. We greedily try 'a'.
                word[k] = 'a';
                
                // Check if setting it to 'a' violates an 'F' constraint ending at `k`.
                int start = k - m + 1;
                bool violation = false;
                if (start >= 0 && str1[start] == 'F') {
                    bool match = true;
                    for (int j = 0; j < m; ++j) {
                        if (word[start + j] != str2[j]) {
                            match = false;
                            break;
                        }
                    }
                    if (match) {
                        violation = true;
                    }
                }

                if (violation) {
                    // If 'a' causes a violation, we must switch to 'b'.
                    // 'b' is guaranteed not to match str2 at the last position if 'a' did match,
                    // because str2[m-1] cannot be both 'a' and 'b'.
                    word[k] = 'b';
                }
            }
        }

        return word;
    }
};
# @lc code=end