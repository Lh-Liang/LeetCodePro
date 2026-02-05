#
# @lc app=leetcode id=3488 lang=cpp
#
# [3488] Closest Equal Element Queries
#

# @lc code=start
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<int> solveQueries(vector<int>& nums, vector<int>& queries) {
        int n = nums.size();
        unordered_map<int, vector<int>> pos;
        for (int i = 0; i < n; ++i) {
            pos[nums[i]].push_back(i);
        }
        vector<int> res;
        for (int q : queries) {
            int val = nums[q];
            const vector<int>& indices = pos[val];
            if (indices.size() == 1) {
                res.push_back(-1);
                continue;
            }
            // Find the position of q in indices
            auto it = lower_bound(indices.begin(), indices.end(), q);
            int min_dist = n;
            // Check previous index (wrap around if needed)
            if (it != indices.begin()) {
                int prev = *(it - 1);
                min_dist = min(min_dist, min(abs(q - prev), n - abs(q - prev)));
            } else {
                int prev = indices.back();
                min_dist = min(min_dist, min(abs(q - prev), n - abs(q - prev)));
            }
            // Check next index (wrap around if needed)
            if (it != indices.end() && *it != q) {
                int next = *it;
                min_dist = min(min_dist, min(abs(q - next), n - abs(q - next)));
            } else {
                int next = indices[0];
                if (next != q)
                    min_dist = min(min_dist, min(abs(q - next), n - abs(q - next)));
            }
            res.push_back(min_dist);
        }
        return res;
    }
};
# @lc code=end