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
        string result(n + m - 1, ' ');
        
        if (backtrack(0, n, m, str1, str2, result)) {
            return result;
        }
        return "";
    }
    
private:
    bool backtrack(int pos, int n, int m, const string& str1, const string& str2, string& result) {
        if (pos == n + m - 1) {
            return true;
        }
        
        for (char c = 'a'; c <= 'z'; c++) {
            result[pos] = c;
            
            if (isValid(pos, n, m, str1, str2, result)) {
                if (backtrack(pos + 1, n, m, str1, str2, result)) {
                    return true;
                }
            }
        }
        
        return false;
    }
    
    bool isValid(int pos, int n, int m, const string& str1, const string& str2, const string& result) {
        for (int i = max(0, pos - m + 1); i <= min(pos, n - 1); i++) {
            int windowEnd = i + m - 1;
            
            if (windowEnd == pos) {
                bool match = true;
                for (int j = 0; j < m; j++) {
                    if (result[i + j] != str2[j]) {
                        match = false;
                        break;
                    }
                }
                
                if (str1[i] == 'T' && !match) return false;
                if (str1[i] == 'F' && match) return false;
            } else {
                int offset = pos - i;
                
                if (str1[i] == 'T') {
                    if (result[pos] != str2[offset]) return false;
                } else {
                    bool allPrevMatch = true;
                    for (int j = i; j < pos; j++) {
                        if (result[j] != str2[j - i]) {
                            allPrevMatch = false;
                            break;
                        }
                    }
                    
                    if (allPrevMatch && offset == m - 1) {
                        if (result[pos] == str2[offset]) return false;
                    }
                }
            }
        }
        
        return true;
    }
};
# @lc code=end