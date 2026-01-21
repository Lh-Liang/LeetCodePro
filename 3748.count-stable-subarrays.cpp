#include <bits/stdc++.h>
using namespace std;

/*
 * @lc app=leetcode id=3748 lang=cpp
 *
 * [3748] Count Stable Subarrays
 */

// @lc code=start
class Solution {
public:
    vector<long long> countStableSubarrays(vector<int>& nums, vector<vector<int>>& queries) {
        int n = (int)nums.size();

        vector<int> blockId(n, -1);
        vector<int> blockStart, blockEnd;
        vector<long long> blockVal; // len*(len+1)/2

        // Build maximal nondecreasing blocks
        int i = 0;
        while (i < n) {
            int j = i;
            while (j + 1 < n && nums[j] <= nums[j + 1]) j++;
            int id = (int)blockStart.size();
            blockStart.push_back(i);
            blockEnd.push_back(j);
            long long len = (long long)(j - i + 1);
            blockVal.push_back(len * (len + 1) / 2);
            for (int k = i; k <= j; k++) blockId[k] = id;
            i = j + 1;
        }

        int m = (int)blockStart.size();
        vector<long long> pref(m + 1, 0); // pref[t] = sum of blockVal[0..t-1]
        for (int b = 0; b < m; b++) pref[b + 1] = pref[b] + blockVal[b];

        auto tri = [&](long long len) -> long long {
            return len * (len + 1) / 2;
        };

        vector<long long> ans;
        ans.reserve(queries.size());

        for (auto &q : queries) {
            int l = q[0], r = q[1];
            int idL = blockId[l], idR = blockId[r];
            long long res = 0;

            if (idL == idR) {
                long long len = (long long)(r - l + 1);
                res = tri(len);
            } else {
                long long leftLen = (long long)(blockEnd[idL] - l + 1);
                long long rightLen = (long long)(r - blockStart[idR] + 1);
                res += tri(leftLen);
                res += tri(rightLen);
                if (idL + 1 <= idR - 1) {
                    // sum blocks (idL+1 .. idR-1)
                    res += pref[idR] - pref[idL + 1];
                }
            }

            ans.push_back(res);
        }

        return ans;
    }
};
// @lc code=end
