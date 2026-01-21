#
# @lc app=leetcode id=3445 lang=cpp
#
# [3445] Maximum Difference Between Even and Odd Frequency II
#
# @lc code=start
class Solution {
public:
    int maxDifference(string s, int k) {
        int n = s.length();
        int result = INT_MIN;
        
        for (int a = 0; a < 5; a++) {
            for (int b = 0; b < 5; b++) {
                if (a == b) continue;
                
                char charA = '0' + a;
                char charB = '0' + b;
                
                // Compute prefix sums
                vector<int> prefixA(n + 1, 0), prefixB(n + 1, 0);
                for (int i = 0; i < n; i++) {
                    prefixA[i + 1] = prefixA[i] + (s[i] == charA);
                    prefixB[i + 1] = prefixB[i] + (s[i] == charB);
                }
                
                int maxPB = prefixB[n];
                if (maxPB == 0) continue;  // Character b doesn't appear
                
                // BIT for minimum, 4 parity states
                vector<vector<int>> bit(4, vector<int>(maxPB + 2, INT_MAX));
                
                for (int r = k; r <= n; r++) {
                    int l = r - k;
                    int diffL = prefixA[l] - prefixB[l];
                    int stateL = (prefixA[l] % 2) * 2 + (prefixB[l] % 2);
                    
                    // Update BIT at position prefixB[l]
                    for (int i = prefixB[l] + 1; i <= maxPB + 1; i += i & (-i)) {
                        bit[stateL][i] = min(bit[stateL][i], diffL);
                    }
                    
                    // Query: need prefixA[l] with opposite parity, prefixB[l] with same parity and < prefixB[r]
                    int diffR = prefixA[r] - prefixB[r];
                    int targetState = (1 - prefixA[r] % 2) * 2 + (prefixB[r] % 2);
                    
                    if (prefixB[r] > 0) {
                        int minDiffL = INT_MAX;
                        for (int i = prefixB[r]; i > 0; i -= i & (-i)) {
                            minDiffL = min(minDiffL, bit[targetState][i]);
                        }
                        if (minDiffL != INT_MAX) {
                            result = max(result, diffR - minDiffL);
                        }
                    }
                }
            }
        }
        
        return result;
    }
};
# @lc code=end