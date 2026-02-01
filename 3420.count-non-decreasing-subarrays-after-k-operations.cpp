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
        long long total_count = 0;
        long long current_cost = 0;
        int r = n - 1;
        // Deque stores indices of elements that are maximums for some suffix
        // Elements in deque are in increasing order of index and decreasing order of value
        deque<int> dq;
        
        for (int l = n - 1; l >= 0; --l) {
            // When adding nums[l] to the left, it may become the new prefix maximum
            // for several elements to its right.
            while (!dq.empty() && nums[l] >= nums[dq.front()]) {
                int idx = dq.front();
                dq.pop_front();
                // This element was the maximum until the next element in the deque or the end of the window
                int next_max_idx = dq.empty() ? r + 1 : dq.front();
                current_cost += (long long)(next_max_idx - idx) * (nums[l] - nums[idx]);
            }
            dq.push_front(l);
            
            // If cost exceeds k, shrink window from the right
            while (current_cost > (long long)k) {
                // The contribution of nums[r] to the cost is (prefix_max_at_r - nums[r])
                // The prefix_max_at_r is nums[dq.back()]
                current_cost -= (long long)(nums[dq.back()] - nums[r]);
                
                // If r was the index providing the maximum value, remove it
                if (r == dq.back()) {
                    dq.pop_back();
                }
                r--;
            }
            
            total_count += (long long)(r - l + 1);
        }
        
        return total_count;
    }
};
# @lc code=end