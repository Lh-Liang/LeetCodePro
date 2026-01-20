#include <vector>
#include <algorithm>

using namespace std;

#
# @lc app=leetcode id=3534 lang=cpp
#
# [3534] Path Existence Queries in a Graph II
#

# @lc code=start
class Solution {
public:
    vector<int> pathExistenceQueries(int n, vector<int>& nums, int maxDiff, vector<vector<int>>& queries) {
        // Step 1: Get unique sorted values
        vector<int> S = nums;
        sort(S.begin(), S.end());
        S.erase(unique(S.begin(), S.end()), S.end());
        int k = S.size();

        // Step 2: Connectivity components
        vector<int> comp(k, 0);
        for (int i = 1; i < k; ++i) {
            if (S[i] - S[i - 1] <= maxDiff) {
                comp[i] = comp[i - 1];
            } else {
                comp[i] = comp[i - 1] + 1;
            }
        }

        // Step 3: Binary Lifting for greedy jumps
        int MAX_P = 0;
        while ((1 << MAX_P) <= k) MAX_P++;
        if (MAX_P == 0) MAX_P = 1;

        vector<vector<int>> Next(k, vector<int>(MAX_P));
        for (int i = 0; i < k; ++i) {
            auto it = upper_bound(S.begin(), S.end(), S[i] + maxDiff);
            int j = distance(S.begin(), prev(it));
            Next[i][0] = j;
        }

        for (int p = 1; p < MAX_P; ++p) {
            for (int i = 0; i < k; ++i) {
                Next[i][p] = Next[Next[i][p - 1]][p - 1];
            }
        }

        // Step 4: Process Queries
        vector<int> answer;
        answer.reserve(queries.size());
        for (const auto& query : queries) {
            int u = query[0];
            int v = query[1];

            if (u == v) {
                answer.push_back(0);
                continue;
            }

            int val_u = nums[u];
            int val_v = nums[v];

            if (val_u == val_v) {
                answer.push_back(1);
                continue;
            }

            if (val_u > val_v) swap(val_u, val_v);

            int idx_u = lower_bound(S.begin(), S.end(), val_u) - S.begin();
            int idx_v = lower_bound(S.begin(), S.end(), val_v) - S.begin();

            if (comp[idx_u] != comp[idx_v]) {
                answer.push_back(-1);
            } else {
                int count = 0;
                int curr = idx_u;
                for (int p = MAX_P - 1; p >= 0; --p) {
                    if (Next[curr][p] < idx_v) {
                        curr = Next[curr][p];
                        count += (1 << p);
                    }
                }
                answer.push_back(count + 1);
            }
        }

        return answer;
    }
};
# @lc code=end