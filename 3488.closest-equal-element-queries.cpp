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
        unordered_map<int, vector<int>> value_indices;
        // Step 1: Map values to sorted list of indices
        for (int i = 0; i < n; ++i) {
            value_indices[nums[i]].push_back(i);
        }
        vector<int> answer;
        // Step 2: Process each query
        for (int q : queries) {
            int val = nums[q];
            const vector<int>& idxs = value_indices[val];
            if (idxs.size() == 1) {
                answer.push_back(-1);
                continue;
            }
            // Step 3: Locate position of q in idxs, check neighbors
            auto it = lower_bound(idxs.begin(), idxs.end(), q);
            int min_dist = n;
            // Previous occurrence (wrap-around if needed)
            int prev_idx = (it == idxs.begin()) ? idxs.back() : *(it - 1);
            if (prev_idx != q) {
                int dist = (q - prev_idx + n) % n;
                if (dist > 0) min_dist = min(min_dist, dist);
            }
            // Next occurrence (wrap-around if needed)
            int next_idx = (it == idxs.end() || *it != q) ? *it : (it + 1 == idxs.end() ? idxs.front() : *(it + 1));
            if (next_idx != q) {
                int dist = (next_idx - q + n) % n;
                if (dist > 0) min_dist = min(min_dist, dist);
            }
            answer.push_back(min_dist);
        }
        return answer;
    }
};
# @lc code=end