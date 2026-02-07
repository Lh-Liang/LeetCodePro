#
# @lc app=leetcode id=3563 lang=cpp
#
# [3563] Lexicographically Smallest String After Adjacent Removals
#

# @lc code=start
class Solution {
public:
    string lexicographicallySmallestString(string s) {
        std::stack<char> st;
        for (char c : s) {
            while (!st.empty() && (abs(st.top() - c) == 1 || abs(st.top() - c) == 25)) {
                st.pop(); // Remove if they are consecutive or circularly consecutive (a-z).
            }
            st.push(c); // Add current character to stack.
        }
        std::string result;
        while (!st.empty()) {
            result.push_back(st.top());
            st.pop();
        }
        std::reverse(result.begin(), result.end()); // Reverse to get correct order.
        return result;
    }
};
# @lc code=end