#
# @lc app=leetcode id=3563 lang=cpp
#
# [3563] Lexicographically Smallest String After Adjacent Removals
#
# @lc code=start
class Solution {
public:
    string lexicographicallySmallestString(string s) {
        std::vector<char> stk; // Using vector as a stack for simplicity.
        for (char c : s) {
            while (!stk.empty() && ((stk.back() == c + 1) || (stk.back() == c - 1) || (stk.back() == 'a' && c == 'z') || (stk.back() == 'z' && c == 'a'))) {
                stk.pop_back(); // Remove consecutive alphabetical pairs considering circular alphabet.
            }
            stk.push_back(c); // Add current character to potential result.
        }
        return std::string(stk.begin(), stk.end()); // Convert vector back to string as result.
    }
};
# @lc code=end