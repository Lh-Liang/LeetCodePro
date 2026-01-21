#include <bits/stdc++.h>
using namespace std;

/*
 * @lc app=leetcode id=3785 lang=cpp
 *
 * [3785] Minimum Swaps to Avoid Forbidden Values
 */

// @lc code=start
class Solution {
public:
    int minSwaps(vector<int>& nums, vector<int>& forbidden) {
        int n = (int)nums.size();

        unordered_map<long long, int> cntNums, cntForb, badCnt;
        cntNums.reserve(n * 2);
        cntForb.reserve(n * 2);
        badCnt.reserve(n * 2);

        int m = 0;      // number of bad indices
        int mx = 0;     // maximum bad count for any value

        for (int i = 0; i < n; i++) {
            long long a = nums[i];
            long long b = forbidden[i];
            cntNums[a]++;
            cntForb[b]++;
            if (a == b) {
                m++;
                int cur = ++badCnt[a];
                if (cur > mx) mx = cur;
            }
        }

        // Feasibility check: for every value v, occurrences of v must fit into allowed positions.
        for (auto &p : cntNums) {
            long long v = p.first;
            int c = p.second;
            int forb = 0;
            auto it = cntForb.find(v);
            if (it != cntForb.end()) forb = it->second;
            if (c > n - forb) return -1;
        }

        if (m == 0) return 0;
        int ans = max((m + 1) / 2, mx);
        return ans;
    }
};
// @lc code=end
