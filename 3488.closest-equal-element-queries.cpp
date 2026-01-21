#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Solution {
public:
    vector<int> solveQueries(vector<int>& nums, vector<int>& queries) {
        int n = (int)nums.size();
        unordered_map<int, vector<int>> pos;
        pos.reserve(n * 2);

        for (int i = 0; i < n; ++i) {
            pos[nums[i]].push_back(i);
        }

        vector<int> best(n, -1);
        for (auto &kv : pos) {
            vector<int> &v = kv.second;
            int m = (int)v.size();
            if (m <= 1) continue;

            for (int i = 0; i < m; ++i) {
                int p = v[i];
                int prev = v[(i - 1 + m) % m];
                int nxt  = v[(i + 1) % m];

                int d1 = abs(p - prev);
                d1 = min(d1, n - d1);
                int d2 = abs(p - nxt);
                d2 = min(d2, n - d2);

                best[p] = min(d1, d2);
            }
        }

        vector<int> ans;
        ans.reserve(queries.size());
        for (int q : queries) ans.push_back(best[q]);
        return ans;
    }
};
// @lc code=end
