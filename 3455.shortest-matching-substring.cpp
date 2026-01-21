//
// @lc app=leetcode id=3455 lang=cpp
//
// [3455] Shortest Matching Substring
//
// @lc code=start
class Solution {
public:
    int shortestMatchingSubstring(string s, string p) {
        size_t first_star = p.find('*');
        size_t second_star = p.find('*', first_star + 1);
        
        string a = p.substr(0, first_star);
        string b = p.substr(first_star + 1, second_star - first_star - 1);
        string c = p.substr(second_star + 1);
        
        int n = s.length();
        int la = a.length(), lb = b.length(), lc = c.length();
        
        if (la + lb + lc > n) return -1;
        
        vector<int> posA = findOccurrences(s, a);
        vector<int> posB = findOccurrences(s, b);
        vector<int> posC = findOccurrences(s, c);
        
        if (la > 0 && posA.empty()) return -1;
        if (lb > 0 && posB.empty()) return -1;
        if (lc > 0 && posC.empty()) return -1;
        
        int min_len = INT_MAX;
        
        if (lb > 0) {
            int idx_a = -1;
            int idx_c = 0;
            
            for (int start_b : posB) {
                if (la > 0) {
                    while (idx_a + 1 < (int)posA.size() && posA[idx_a + 1] + la <= start_b) {
                        idx_a++;
                    }
                    if (idx_a < 0) continue;
                }
                
                if (lc > 0) {
                    while (idx_c < (int)posC.size() && posC[idx_c] < start_b + lb) {
                        idx_c++;
                    }
                    if (idx_c >= (int)posC.size()) break;
                }
                
                int start_a = (la > 0) ? posA[idx_a] : start_b;
                int end_c = (lc > 0) ? posC[idx_c] + lc : start_b + lb;
                
                min_len = min(min_len, end_c - start_a);
            }
        } else {
            if (la > 0 && lc > 0) {
                int idx_a = -1;
                for (int start_c : posC) {
                    while (idx_a + 1 < (int)posA.size() && posA[idx_a + 1] + la <= start_c) {
                        idx_a++;
                    }
                    if (idx_a < 0) continue;
                    
                    int start_a = posA[idx_a];
                    min_len = min(min_len, start_c + lc - start_a);
                }
            } else if (la > 0) {
                min_len = la;
            } else if (lc > 0) {
                min_len = lc;
            } else {
                min_len = 0;
            }
        }
        
        return min_len == INT_MAX ? -1 : min_len;
    }
    
private:
    vector<int> zFunction(const string& s) {
        int n = s.length();
        vector<int> z(n, 0);
        int l = 0, r = 0;
        for (int i = 1; i < n; i++) {
            if (i < r) {
                z[i] = min(r - i, z[i - l]);
            }
            while (i + z[i] < n && s[z[i]] == s[i + z[i]]) {
                z[i]++;
            }
            if (i + z[i] > r) {
                l = i;
                r = i + z[i];
            }
        }
        return z;
    }
    
    vector<int> findOccurrences(const string& text, const string& pattern) {
        vector<int> positions;
        if (pattern.empty()) return positions;
        
        string combined = pattern + "$" + text;
        vector<int> z = zFunction(combined);
        int pLen = pattern.length();
        
        for (int i = pLen + 1; i < (int)combined.length(); i++) {
            if (z[i] >= pLen) {
                positions.push_back(i - pLen - 1);
            }
        }
        
        return positions;
    }
};
// @lc code=end