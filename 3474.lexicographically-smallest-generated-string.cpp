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
        int len = n + m - 1;
        
        string word(len, '?');
        vector<bool> locked(len, false);
        
        // Process 'T' constraints
        for (int i = 0; i < n; i++) {
            if (str1[i] == 'T') {
                for (int j = 0; j < m; j++) {
                    if (word[i + j] != '?' && word[i + j] != str2[j]) {
                        return "";
                    }
                    word[i + j] = str2[j];
                    locked[i + j] = true;
                }
            }
        }
        
        // For each 'F' constraint, compute rightmost free position
        vector<int> rightmostFree(n, -2);  // -2: already satisfied or not F
        
        for (int i = 0; i < n; i++) {
            if (str1[i] == 'F') {
                bool satisfied = false;
                for (int j = 0; j < m; j++) {
                    if (locked[i + j] && word[i + j] != str2[j]) {
                        satisfied = true;
                        break;
                    }
                }
                
                if (!satisfied) {
                    rightmostFree[i] = -1;
                    for (int j = m - 1; j >= 0; j--) {
                        if (!locked[i + j]) {
                            rightmostFree[i] = i + j;
                            break;
                        }
                    }
                    if (rightmostFree[i] == -1) return "";
                }
            }
        }
        
        // Build dependency list
        vector<vector<int>> dependents(len);
        for (int i = 0; i < n; i++) {
            if (rightmostFree[i] >= 0) {
                dependents[rightmostFree[i]].push_back(i);
            }
        }
        
        // Track satisfied constraints
        vector<bool> satisfied(n, false);
        for (int i = 0; i < n; i++) {
            if (rightmostFree[i] == -2) satisfied[i] = true;
        }
        
        // Greedy fill
        for (int j = 0; j < len; j++) {
            // Update satisfied for constraints that include position j (for locked positions)
            if (locked[j]) {
                for (int i = max(0, j - m + 1); i <= min(n - 1, j); i++) {
                    if (str1[i] == 'F' && !satisfied[i] && word[j] != str2[j - i]) {
                        satisfied[i] = true;
                    }
                }
                continue;
            }
            
            set<char> forbidden;
            for (int i : dependents[j]) {
                if (!satisfied[i]) {
                    forbidden.insert(str2[j - i]);
                }
            }
            
            word[j] = 'a';
            while (forbidden.count(word[j])) {
                word[j]++;
                if (word[j] > 'z') return "";
            }
            
            // Update satisfied after assignment
            for (int i = max(0, j - m + 1); i <= min(n - 1, j); i++) {
                if (str1[i] == 'F' && !satisfied[i] && word[j] != str2[j - i]) {
                    satisfied[i] = true;
                }
            }
        }
        
        // Final verification
        for (int i = 0; i < n; i++) {
            if (str1[i] == 'F') {
                bool match = true;
                for (int k = 0; k < m; k++) {
                    if (word[i + k] != str2[k]) {
                        match = false;
                        break;
                    }
                }
                if (match) return "";
            }
        }
        
        return word;
    }
};
# @lc code=end