#
# @lc app=leetcode id=3695 lang=cpp
#
# [3695] Maximize Alternating Sum Using Swaps
#
# @lc code=start
class Solution {
public:
    long long maxAlternatingSum(vector<int>& nums, vector<vector<int>>& swaps) {
        int n = nums.size();
        vector<int> parent(n);
        iota(parent.begin(), parent.end(), 0);
        function<int(int)> find = [&](int x) {
            if (parent[x] != x) parent[x] = find(parent[x]);
            return parent[x];
        };
        for (auto& s : swaps) {
            int a = find(s[0]), b = find(s[1]);
            if (a != b) parent[a] = b;
        }
        unordered_map<int, vector<int>> groups;
        for (int i = 0; i < n; ++i) {
            groups[find(i)].push_back(i);
        }
        vector<int> res(n);
        for (auto& [_, idxs] : groups) {
            vector<int> vals;
            for (int i : idxs) vals.push_back(nums[i]);
            sort(idxs.begin(), idxs.end());
            sort(vals.rbegin(), vals.rend()); // descending
            // Assign largest values to smallest indices (even positions)
            for (int j = 0; j < idxs.size(); ++j) {
                res[idxs[j]] = vals[j];
            }
            // Verification step: For small components, check both possible assignments (start even or odd)
            if (idxs.size() <= 10) {
                vector<int> perm = vals;
                long long best = LLONG_MIN;
                sort(perm.begin(), perm.end());
                do {
                    long long cur = 0;
                    for (int j = 0; j < idxs.size(); ++j) {
                        if (idxs[j] % 2 == 0) cur += perm[j];
                        else cur -= perm[j];
                    }
                    if (cur > best) {
                        for (int j = 0; j < idxs.size(); ++j) res[idxs[j]] = perm[j];
                        best = cur;
                    }
                } while (next_permutation(perm.begin(), perm.end()));
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