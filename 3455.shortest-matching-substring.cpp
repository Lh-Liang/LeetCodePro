#
# @lc app=leetcode id=3455 lang=cpp
#
# [3455] Shortest Matching Substring
#
# @lc code=start
class Solution {
public:
    int shortestMatchingSubstring(string s, string p) {
        // Split p by '*'
        size_t star1 = p.find('*');
        size_t star2 = p.find('*', star1 + 1);
        
        string a = p.substr(0, star1);
        string b = p.substr(star1 + 1, star2 - star1 - 1);
        string c = p.substr(star2 + 1);
        
        int n = (int)s.length();
        int lenA = (int)a.length(), lenB = (int)b.length(), lenC = (int)c.length();
        
        // Find all occurrences
        vector<int> posA = findOccurrences(s, a);
        vector<int> posB = findOccurrences(s, b);
        vector<int> posC = findOccurrences(s, c);
        
        if (posA.empty() || posB.empty() || posC.empty()) {
            return -1;
        }
        
        int ans = INT_MAX;
        int maxI = -1;
        int idxI = 0;
        int idxK = 0;
        
        for (int j : posB) {
            // Find the largest posA[i] such that posA[i] + lenA <= j
            while (idxI < (int)posA.size() && posA[idxI] + lenA <= j) {
                maxI = posA[idxI];
                idxI++;
            }
            if (maxI == -1) continue;
            
            // Find the smallest posC[k] such that posC[k] >= j + lenB
            int minCStart = j + lenB;
            while (idxK < (int)posC.size() && posC[idxK] < minCStart) {
                idxK++;
            }
            if (idxK >= (int)posC.size()) break;
            int k = posC[idxK];
            
            int len = k + lenC - maxI;
            ans = min(ans, len);
        }
        
        return ans == INT_MAX ? -1 : ans;
    }
    
private:
    vector<int> findOccurrences(const string& s, const string& pattern) {
        vector<int> result;
        int n = (int)s.length();
        if (pattern.empty()) {
            for (int i = 0; i <= n; i++) {
                result.push_back(i);
            }
        } else {
            // KMP algorithm
            int m = (int)pattern.length();
            vector<int> lps = computeLPS(pattern);
            int i = 0, j = 0;
            while (i < n) {
                if (s[i] == pattern[j]) {
                    i++; j++;
                }
                if (j == m) {
                    result.push_back(i - j);
                    j = lps[j - 1];
                } else if (i < n && s[i] != pattern[j]) {
                    if (j != 0) {
                        j = lps[j - 1];
                    } else {
                        i++;
                    }
                }
            }
        }
        return result;
    }
    
    vector<int> computeLPS(const string& pattern) {
        int m = (int)pattern.length();
        vector<int> lps(m, 0);
        int len = 0, i = 1;
        while (i < m) {
            if (pattern[i] == pattern[len]) {
                len++;
                lps[i] = len;
                i++;
            } else {
                if (len != 0) {
                    len = lps[len - 1];
                } else {
                    lps[i] = 0;
                    i++;
                }
            }
        }
        return lps;
    }
};
# @lc code=end