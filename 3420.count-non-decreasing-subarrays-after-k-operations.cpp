#
# @lc app=leetcode id=3420 lang=cpp
#
# [3420] Count Non-Decreasing Subarrays After K Operations
#

# @lc code=start
#include <vector>
#include <deque>
#include <algorithm>

using namespace std;

class Solution {
public:
    long long countNonDecreasingSubarrays(vector<int>& nums, int k) {
        int n = nums.size();
        long long ans = 0;
        long long current_cost = 0;
        int r = n - 1;
        deque<int> dq; // Stores indices of elements in the window in decreasing order of nums[i]

        // Process from right to left to make cost calculation easier
        // As we expand 'l' to the left, nums[l] potentially increases elements to its right.
        for (int l = n - 1; l >= 0; --l) {
            // When adding nums[l] at the left, it becomes the new maximum for elements to its right
            // that are smaller than it, until it hits an element >= nums[l].
            while (!dq.empty() && nums[l] > nums[dq.back()]) {
                int idx = dq.back();
                dq.pop_back();
                // The range affected by nums[idx] being replaced by nums[l]
                int range_end = dq.empty() ? r : dq.back() - 1;
                current_cost += (long long)(nums[l] - nums[idx]) * (range_end - idx + 1);
            }
            dq.push_back(l);

            // If cost exceeds k, shrink window from the right
            while (current_cost > k) {
                // nums[dq.front()] is the current max for the rightmost part of the window.
                // However, we need to subtract the cost contributed by the current max at index r.
                current_cost -= (long long)(nums[dq.front()] - nums[r]);
                if (dq.front() == r) {
                    dq.pop_front();
                }
                r--;
            }
            ans += (r - l + 1);
        }

        return ans;
    }
};
# @lc code=end