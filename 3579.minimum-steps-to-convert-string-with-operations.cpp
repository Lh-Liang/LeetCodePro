#
# @lc app=leetcode id=3579 lang=cpp
#
# [3579] Minimum Steps to Convert String with Operations
#

# @lc code=start
#include <vector>
#include <string>
#include <algorithm>
#include <map>

using namespace std;

class Solution {
public:
    int minOperations(string word1, string word2) {
        int n = word1.length();
        vector<int> dp(n + 1, 1e9);
        dp[0] = 0;

        for (int i = 1; i <= n; ++i) {
            for (int j = 0; j < i; ++j) {
                string s = word1.substr(j, i - j);
                string t = word2.substr(j, i - j);
                
                int cost = calculateCost(s, t);
                dp[i] = min(dp[i], dp[j] + cost);
            }
        }

        return dp[n];
    }

private:
    int calculateCost(string s, string t) {
        if (s == t) return 0;
        
        int n = s.length();
        vector<int> countS(26, 0), countT(26, 0);
        for (char c : s) countS[c - 'a']++;
        for (char c : t) countT[c - 'a']++;

        int matches = 0;
        for (int k = 0; k < 26; ++k) {
            matches += min(countS[k], countT[k]);
        }

        int replaces = n - matches;
        
        // After replaces, we have a permutation of T.
        // If the original (with replaced chars) is already T, 0 extra.
        // If it's the reverse of T, 1 extra (Reverse).
        // If it's a permutation of T, 1 extra (Swap).
        // If we need both, 2 extra.
        
        // Special case: if replaces accounts for all differences and result is T
        // But we must consider if we can achieve T using the allowed moves.
        // The constraint "each index involved at most once" for swap/reverse/replace
        // is key. If we replace a char, that index is done for replacements.
        
        string s_rev = s;
        reverse(s_rev.begin(), s_rev.end());

        if (replaces == 0) {
            if (s_rev == t) return 1; // Reverse
            return 1; // Swap (since s != t and same counts)
        }

        // If we replace characters, we can choose which indices to replace.
        // To minimize operations, we replace indices where s[i] != t[i].
        int diff_pos = 0;
        for(int k=0; k<n; ++k) if(s[k] != t[k]) diff_pos++;

        if (diff_pos == replaces) return replaces; 
        
        // Check if Reverse + Replace works
        int diff_pos_rev = 0;
        for(int k=0; k<n; ++k) if(s_rev[k] != t[k]) diff_pos_rev++;
        if (diff_pos_rev <= replaces) return replaces + 1;

        return replaces + 1; // Generally Replace + Swap
    }
};
# @lc code=end