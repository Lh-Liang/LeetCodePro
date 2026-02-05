#
# @lc app=leetcode id=3695 lang=cpp
#
# [3695] Maximize Alternating Sum Using Swaps
#
# @lc code=start
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<int> parent;
    int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }
    void unite(int x, int y) {
        parent[find(x)] = find(y);
    }
    long long maxAlternatingSum(vector<int>& nums, vector<vector<int>>& swaps) {
        int n = nums.size();
        parent.resize(n);
        for (int i = 0; i < n; ++i) parent[i] = i;
        for (const auto& s : swaps) {
            unite(s[0], s[1]);
        }
        unordered_map<int, vector<int>> groups;
        for (int i = 0; i < n; ++i) {
            groups[find(i)].push_back(i);
        }
        vector<int> res(nums);
        for (const auto& [p, idxs] : groups) {
            vector<int> vals;
            for (int idx : idxs) vals.push_back(nums[idx]);
            sort(idxs.begin(), idxs.end());
            sort(vals.begin(), vals.end(), greater<int>());
            for (int i = 0; i < idxs.size(); ++i) {
                res[idxs[i]] = vals[i];
            }
        }
        long long ans = 0;
        for (int i = 0; i < n; ++i) {
            if (i % 2 == 0) ans += res[i];
            else ans -= res[i];
        }
        return ans;
    }
};
# @lc code=end