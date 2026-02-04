#
# @lc app=leetcode id=3458 lang=cpp
#
# [3458] Select K Disjoint Special Substrings
#

# @lc code=start
class Solution {
public:
    bool maxSubstringLength(string s, int k) {
        unordered_map<char, int> freq;
        for (char c : s) {
            freq[c]++;
        }
        int unique_count = 0;
        for (const auto &entry : freq) {
            if (entry.second == 1) {
                unique_count++;
            }
        }
        return unique_count >= k;
    }
};
# @lc code=end