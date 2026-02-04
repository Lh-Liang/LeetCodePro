#
# @lc app=leetcode id=3435 lang=cpp
#
# [3435] Frequencies of Shortest Supersequences
#

# @lc code=start
class Solution {
public:
    vector<vector<int>> supersequences(vector<string>& words) {
        // There are at most 16 unique letters and all words are length 2
        // For each SCS, any permutation with same letter counts is considered equivalent
        // So, output only one frequency array: sum all letters' frequencies
        vector<int> freq(26, 0);
        for (const auto& word : words) {
            for (char ch : word) {
                freq[ch - 'a']++;
            }
        }
        // Only one equivalence class
        return {freq};
    }
};
# @lc code=end