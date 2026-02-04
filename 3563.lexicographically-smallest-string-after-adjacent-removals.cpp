#
# @lc app=leetcode id=3563 lang=cpp
#
# [3563] Lexicographically Smallest String After Adjacent Removals
#
# @lc code=start
#include <string>
#include <unordered_map>
using namespace std;

class Solution {
public:
    string lexicographicallySmallestString(string s) {
        unordered_map<string, string> memo;
        return dfs(s, memo);
    }
private:
    // Helper to check if two chars are consecutive (circular)
    bool consecutive(char a, char b) {
        return (abs(a-b) == 1) || (a == 'a' && b == 'z') || (a == 'z' && b == 'a');
    }
    string dfs(const string& s, unordered_map<string, string>& memo) {
        if (memo.count(s)) return memo[s];
        string res = s; // Option to do nothing
        int n = s.size();
        for (int i = 0; i < n-1; ++i) {
            if (consecutive(s[i], s[i+1])) {
                string ns = s.substr(0,i) + s.substr(i+2);
                string candidate = dfs(ns, memo);
                if (candidate < res) res = candidate;
            }
        }
        memo[s] = res;
        return res;
    }
};
# @lc code=end