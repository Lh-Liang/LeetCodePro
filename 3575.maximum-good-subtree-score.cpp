#
# @lc app=leetcode id=3575 lang=cpp
#
# [3575] Maximum Good Subtree Score
#
# @lc code=start
#include <vector>
#include <string>
#include <unordered_set>
#include <algorithm>
using namespace std;

class Solution {
public:
    int goodSubtreeSum(vector<int>& vals, vector<int>& par) {
        const int MOD = 1e9 + 7;
        int n = vals.size();
        vector<vector<int>> tree(n);
        for (int i = 1; i < n; ++i) {
            tree[par[i]].push_back(i);
        }
        vector<int> maxScore(n, 0);
        function<void(int, unordered_set<int>&)> dfs = [&](int node, unordered_set<int>& usedDigits) {
            string valStr = to_string(vals[node]);
            unordered_set<int> currDigits;
            for (char c : valStr) {
                if (usedDigits.count(c - '0')) return; // digit already used in path, invalid subset here. 
                currDigits.insert(c - '0'); 
            } 
            usedDigits.insert(currDigits.begin(), currDigits.end()); 
            maxScore[node] = vals[node]; 
            for (int child : tree[node]) { 
dfs(child, usedDigits); 
k maxScore[node] = (maxScore[node] + maxScore[child]) % MOD; 
m} 
kusedDigits.erase(currDigits.begin(), currDigits.end()); 
l}; 
dfs(0, unordered_set<int>()); // start dfs from the root node 0 with an empty set of used digits. 
tint totalMaxScore = accumulate(maxScore.begin(), maxScore.end(), 0LL) % MOD; // calculate total sum of maxScores. 
u return totalMaxScore; 
v} }; # @lc code=end