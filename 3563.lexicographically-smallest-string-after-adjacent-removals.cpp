#
# @lc app=leetcode id=3563 lang=cpp
#
# [3563] Lexicographically Smallest String After Adjacent Removals
#

# @lc code=start
class Solution {
public:
    string lexicographicallySmallestString(string s) {
        string stk;
        auto is_consecutive = [](char a, char b) {
            return (abs(a - b) == 1) || (a == 'a' && b == 'z') || (a == 'z' && b == 'a');
        };
        for (char c : s) {
            if (!stk.empty() && is_consecutive(stk.back(), c)) {
                stk.pop_back();
            } else {
                stk.push_back(c);
            }
        }
        return stk;
    }
};
# @lc code=end