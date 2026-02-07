#
# @lc app=leetcode id=3327 lang=cpp
#
# [3327] Check if DFS Strings Are Palindromes
#
# @lc code=start
#include <vector>
#include <string>
#include <functional>
using namespace std;

class Solution {
public:
    vector<bool> findAnswer(vector<int>& parent, string s) {
        int n = s.size();
        vector<vector<int>> children(n);
        for (int i = 1; i < n; ++i) {
            children[parent[i]].push_back(i);
        }

        auto isPalindrome = [](const string& str) {
            int l = 0, r = str.size() - 1;
            while (l < r) {
                if (str[l++] != str[r--]) return false;
            }
            return true;
        };

        vector<bool> answer(n);
        function<void(int)> dfs = [&](int node) {
            string dfsStr;
            function<void(int)> dfsHelper = [&](int x) {
                for (int y : children[x]) dfsHelper(y);
                dfsStr.push_back(s[x]);
            };
            dfsHelper(node);
            answer[node] = isPalindrome(dfsStr);
        };

        for (int i = 0; i < n; ++i) {
            dfs(i);
        }

        return answer;
    }
};
# @lc code=end