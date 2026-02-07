#
# @lc app=leetcode id=3327 lang=cpp
#
# [3327] Check if DFS Strings Are Palindromes
#

# @lc code=start
class Solution {
public:
    vector<bool> findAnswer(vector<int>& parent, string s) {
        int n = parent.size();
        vector<vector<int>> children(n);
        for (int i = 1; i < n; ++i) {
            children[parent[i]].push_back(i);
        }
        
        vector<bool> answer(n);
        
        function<void(int, string&)> dfs = [&](int x, string& dfsStr) {
            for (int y : children[x]) {
                dfs(y, dfsStr);
            }
            dfsStr.push_back(s[x]);
        };
        
        auto isPalindrome = [](const string& str) {
            int l = 0, r = str.size() - 1;
            while (l < r) {
                if (str[l++] != str[r--]) return false;
            }
            return true;
        };
        
        for (int i = 0; i < n; ++i) {
            string dfsStr;
            dfs(i, dfsStr);
            answer[i] = isPalindrome(dfsStr);
        }
        return answer;
    }
};
# @lc code=end