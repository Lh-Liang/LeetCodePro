#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    int minOperations(string word1, string word2) {
        int n = word1.length();
        vector<int> dp(n + 1, 1e9);
        dp[0] = 0;

        for (int i = 1; i <= n; ++i) {
            for (int j = 0; j < i; ++j) {
                int len = i - j;
                // Option 1: No reverse
                int cost_no_rev = calculateSubstrCost(word1, word2, j, len, false);
                // Option 2: With reverse
                int cost_with_rev = 1 + calculateSubstrCost(word1, word2, j, len, true);
                
                dp[i] = min(dp[i], dp[j] + min(cost_no_rev, cost_with_rev));
            }
        }

        return dp[n];
    }

private:
    int calculateSubstrCost(const string& w1, const string& w2, int start, int len, bool rev) {
        int d = 0;
        int n_counts[26][26] = {0};
        
        for (int k = 0; k < len; ++k) {
            char s_char = rev ? w1[start + len - 1 - k] : w1[start + k];
            char t_char = w2[start + k];
            
            if (s_char != t_char) {
                d++;
                n_counts[s_char - 'a'][t_char - 'a']++;
            }
        }

        int p = 0;
        for (int c1 = 0; c1 < 26; ++c1) {
            for (int c2 = c1 + 1; c2 < 26; ++c2) {
                p += min(n_counts[c1][c2], n_counts[c2][c1]);
            }
        }
        // Under the constraint 'each index used at most once',
        // only mutual pairs (2-cycles) reduce cost relative to replacement.
        return d - p;
    }
};