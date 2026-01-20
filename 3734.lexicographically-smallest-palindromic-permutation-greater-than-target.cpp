#
# @lc app=leetcode id=3734 lang=cpp
#
# [3734] Lexicographically Smallest Palindromic Permutation Greater Than Target
#

# @lc code=start
class Solution {
public:
    string lexPalindromicPermutation(string s, string target) {
        int n = s.length();
        vector<int> count(26, 0);
        for (char c : s) count[c - 'a']++;

        int oddCount = 0;
        int oddCharIdx = -1;
        for (int i = 0; i < 26; ++i) {
            if (count[i] % 2 != 0) {
                oddCount++;
                oddCharIdx = i;
            }
        }

        if (oddCount > 1) return "";

        string mid = "";
        if (n % 2 == 1) {
            mid += (char)('a' + oddCharIdx);
            count[oddCharIdx]--;
        }

        // half_counts for the first n/2 characters
        vector<int> half_counts(26);
        for (int i = 0; i < 26; ++i) half_counts[i] = count[i] / 2;

        int m = n / 2;
        
        // Helper to construct palindrome from left half
        auto construct = [&](string left) {
            string right = left;
            reverse(right.begin(), right.end());
            return left + mid + right;
        };

        // 1. Try to match the full left half (prefix length m)
        bool possible = true;
        vector<int> current_counts = half_counts;
        string current_prefix = "";
        for (int i = 0; i < m; ++i) {
            int charIdx = target[i] - 'a';
            if (current_counts[charIdx] > 0) {
                current_counts[charIdx]--;
                current_prefix += target[i];
            } else {
                possible = false;
                break;
            }
        }

        if (possible) {
            string cand = construct(current_prefix);
            if (cand > target) return cand;
        }

        // 2. Iterate backwards to find the latest divergence point
        // We try to match target[0...i-1] and then place c > target[i] at position i
        // Since we want the smallest result, we want the longest matching prefix.
        // So we iterate i from m-1 down to 0.
        
        // We need to maintain the counts available for the prefix 0...i-1.
        // Re-calculating prefix validity every time is O(N^2), which is fine for N=300.
        
        for (int i = m - 1; i >= 0; --i) {
            // Check if prefix 0...i-1 is valid
            vector<int> temp_counts = half_counts;
            string prefix = "";
            bool prefix_valid = true;
            for (int j = 0; j < i; ++j) {
                int c = target[j] - 'a';
                if (temp_counts[c] > 0) {
                    temp_counts[c]--;
                    prefix += target[j];
                } else {
                    prefix_valid = false;
                    break;
                }
            }
            
            if (!prefix_valid) continue;

            // Try to place smallest character c > target[i]
            for (int c = target[i] - 'a' + 1; c < 26; ++c) {
                if (temp_counts[c] > 0) {
                    // Found the divergence point!
                    temp_counts[c]--;
                    prefix += (char)('a' + c);
                    
                    // Fill the rest (i+1 to m-1) with smallest available characters
                    for (int k = 0; k < 26; ++k) {
                        while (temp_counts[k] > 0) {
                            prefix += (char)('a' + k);
                            temp_counts[k]--;
                        }
                    }
                    
                    return construct(prefix);
                }
            }
        }

        return "";
    }
};
# @lc code=end