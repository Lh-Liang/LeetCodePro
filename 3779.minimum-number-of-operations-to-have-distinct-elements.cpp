#
# @lc app=leetcode id=3779 lang=cpp
#
# [3779] Minimum Number of Operations to Have Distinct Elements
#

# @lc code=start
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int minOperations(vector<int>& nums) {
        int n = nums.size();
        vector<int> prev(n, -1);
        vector<int> last_pos(100010, -1);
        for (int i = 0; i < n; ++i) {
            int val = nums[i];
            if (last_pos[val] != -1) {
                prev[i] = last_pos[val];
            }
            last_pos[val] = i;
        }
        vector<int> max_prev(n + 1, -1);
        for (int j = n - 1; j >= 0; --j) {
            max_prev[j] = max(prev[j], max_prev[j + 1]);
        }
        int k = 0;
        while (true) {
            int s = min(3 * k, n);
            if (s == n || max_prev[s] < s) {
                return k;
            }
            ++k;
        }
    }
};
# @lc code=end