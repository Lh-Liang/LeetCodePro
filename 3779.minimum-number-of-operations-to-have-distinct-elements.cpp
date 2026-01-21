#include <bits/stdc++.h>
using namespace std;

/*
 * @lc app=leetcode id=3779 lang=cpp
 *
 * [3779] Minimum Number of Operations to Have Distinct Elements
 */

// @lc code=start
class Solution {
public:
    int minOperations(vector<int>& nums) {
        int n = (int)nums.size();
        // nums[i] <= 1e5 per constraints
        static const int MAXV = 100000;
        vector<char> seen(MAXV + 1, 0);

        int t = 0; // earliest index from which suffix can be all distinct
        for (int i = n - 1; i >= 0; --i) {
            int x = nums[i];
            if (seen[x]) {
                t = max(t, i + 1);
            } else {
                seen[x] = 1;
            }
        }

        return (t + 2) / 3; // ceil(t/3)
    }
};
// @lc code=end
