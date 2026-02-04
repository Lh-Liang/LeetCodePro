#
# @lc app=leetcode id=3458 lang=cpp
#
# [3458] Select K Disjoint Special Substrings
#
# @lc code=start
class Solution {
public:
    bool maxSubstringLength(string s, int k) {
        unordered_map<char, int> frequency;
        for (char c : s) {
            frequency[c]++;
        }
        vector<pair<int, int>> potentialSubstrings;
        int i = 0;
        while (i < s.size()) {
            // Find start of potential substring
            while (i < s.size() && frequency[s[i]] != 1) {
                i++;
            }
            int start = i;
            // Find end of potential substring
            while (i < s.size() && frequency[s[i]] == 1) {
                i++;
            }
            int end = i;
            if (end > start) {
                potentialSubstrings.push_back({start, end});
            }
        }
        // Validate isolation and count valid substrings
        int specialCount = 0;
        for (auto &range : potentialSubstrings) {
            unordered_set<char> seen(s.begin() + range.first, s.begin() + range.second);
            bool valid = true;
            for (char c : seen) {
                if (frequency[c] != 1) { // Shouldn't appear more than once overall
                    valid = false;
                    break;
                }
            }
            if (valid) {
                specialCount++;
                if (specialCount >= k) return true;
            }
        }
        return false;
    }
};
# @lc code=end