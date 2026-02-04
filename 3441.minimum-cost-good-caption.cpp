#
# @lc app=leetcode id=3441 lang=cpp
#
# [3441] Minimum Cost Good Caption
#
# @lc code=start
class Solution {
public:
    string minCostGoodCaption(string caption) {
        int n = caption.length();
        if (n < 3) return ""; // Impossible to have good caption if length < 3.
        vector<pair<int, int>> groups; // Stores start index and length of each group.
        for (int i = 0; i < n;) {
            int j = i;
            while (j < n && caption[j] == caption[i]) ++j;
            int len = j - i;
            groups.push_back({i, len});
            i = j;
        }
        for (auto& [start, len] : groups) {
            if (len >= 3) continue; // Already a valid group.
            // Attempt to expand this group using adjacent characters.
            char targetChar = caption[start];
            if (start > 0 && start + len < n) { // Between two different chars
                char prevChar = caption[start - 1];
                char nextChar = caption[start + len];
                char changeChar = min(prevChar, nextChar); // Choose smaller lexicographical option if possible.
                for (int k = start; k < start + len; ++k) {
                    caption[k] = changeChar;
                }
            } else if (start > 0) { // At end of string or only one side available
                char prevChar = caption[start - 1];
                for (int k = start; k < start + len; ++k) {
                    caption[k] = prevChar;
                }
            } else if (start + len < n) { // At start of string
                char nextChar = caption[start + len];
                for (int k = start; k < start + len; ++k) {
                    caption[k] = nextChar;
                }
            } else {
                return ""; // No valid transformation possible at boundaries without adjacent options.
            }
        }
        // Verify final result forms valid groups after all transformations.
        for (int i = 0; i < n;) {
            int j = i;
            while (j < n && caption[j] == caption[i]) ++j;
            int len = j - i;
            if (len < 3) return "";
            i = j;
        }
        return caption;
    }
};
integrate_vertical_transformation_strategy();
integrate_global_lexicographical_order_maintenance();