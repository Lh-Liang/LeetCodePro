#
# @lc app=leetcode id=3563 lang=cpp
#
# [3563] Lexicographically Smallest String After Adjacent Removals
#

# @lc code=start
class Solution {
public:
    string lexicographicallySmallestString(string s) {
        stack<char> stk;
        for (char c : s) {
            while (!stk.empty() && ((stk.top() == c + 1) || (stk.top() == c - 1))) {
                stk.pop();
            }
            stk.push(c);
        }
        string result;
        while (!stk.empty()) {
            result += stk.top();
            stk.pop();
        }
        reverse(result.begin(), result.end());
        return result;
    }
};
# @lc code=end