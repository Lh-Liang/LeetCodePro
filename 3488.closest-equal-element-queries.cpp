#
# @lc app=leetcode id=3488 lang=cpp
#
# [3488] Closest Equal Element Queries
#

# @lc code=start
#include <vector>
#include <algorithm>
#include <numeric>
#include <cmath>

using namespace std;

class Solution {
public:
    vector<int> solveQueries(vector<int>& nums, vector<int>& queries) {
        int n = nums.size();
        vector<int> p(n);
        iota(p.begin(), p.end(), 0);

        // Sort indices based on the values in nums
        sort(p.begin(), p.end(), [&](int i, int j) {
            if (nums[i] != nums[j]) return nums[i] < nums[j];
            return i < j;
        });

        // Map each original index to its position in the sorted array p
        vector<int> pos(n);
        for (int i = 0; i < n; ++i) {
            pos[p[i]] = i;
        }

        // Precompute the range [L, R] for each value group in sorted array p
        vector<int> start_idx(n), end_idx(n);
        for (int i = 0; i < n; ) {
            int j = i;
            while (j < n && nums[p[j]] == nums[p[i]]) {
                j++;
            }
            for (int k = i; k < j; ++k) {
                start_idx[k] = i;
                end_idx[k] = j - 1;
            }
            i = j;
        }

        // Lambda to calculate circular distance
        auto get_dist = [&](int i, int j) {
            int d = abs(i - j);
            return min(d, n - d);
        };

        vector<int> answer;
        answer.reserve(queries.size());

        for (int q_idx : queries) {
            int k = pos[q_idx];
            int L = start_idx[k];
            int R = end_idx[k];

            if (L == R) {
                // Only one instance of the value exists
                answer.push_back(-1);
            } else {
                // The closest element must be one of the circular neighbors in the sorted group
                int prev_k = (k == L) ? R : k - 1;
                int next_k = (k == R) ? L : k + 1;

                int d1 = get_dist(q_idx, p[prev_k]);
                int d2 = get_dist(q_idx, p[next_k]);
                answer.push_back(min(d1, d2));
            }
        }

        return answer;
    }
};
# @lc code=end