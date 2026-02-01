#
# @lc app=leetcode id=3420 lang=cpp
#
# [3420] Count Non-Decreasing Subarrays After K Operations
#

# @lc code=start
#include <vector>
#include <deque>

using namespace std;

class Solution {
public:
    long long countNonDecreasingSubarrays(vector<int>& nums, int k) {
        int n = nums.size();
        long long ans = 0;
        long long sum_b = 0;
        long long sum_nums = 0;
        int R = n - 1;
        // Deque stores pairs of (value, count) for the non-decreasing sequence b.
        // We iterate L from right to left to easily manage prefix maximum updates.
        deque<pair<long long, int>> dq;

        for (int L = n - 1; L >= 0; --L) {
            long long cur_val = nums[L];
            long long count_to_add = 1;
            sum_nums += cur_val;
            
            // When adding nums[L] to the front, any existing b[i] < nums[L] 
            // will be updated to nums[L] until we hit a value > nums[L].
            while (!dq.empty() && dq.front().first <= cur_val) {
                sum_b -= dq.front().first * (long long)dq.front().second;
                count_to_add += dq.front().second;
                dq.pop_front();
            }
            dq.push_front({cur_val, (int)count_to_add});
            sum_b += cur_val * count_to_add;
            
            // If the cost (sum_b - sum_nums) exceeds k, shrink the window from the right.
            while (sum_b - sum_nums > (long long)k) {
                long long last_val = dq.back().first;
                sum_b -= last_val;
                sum_nums -= nums[R];
                dq.back().second--;
                if (dq.back().second == 0) {
                    dq.pop_back();
                }
                R--;
            }
            // All subarrays [L, i] where L <= i <= R are valid.
            ans += (long long)(R - L + 1);
        }
        
        return ans;
    }
};
# @lc code=end