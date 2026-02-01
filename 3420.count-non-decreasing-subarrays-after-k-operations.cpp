#include <vector>
#include <deque>

using namespace std;

class Solution {
public:
    long long countNonDecreasingSubarrays(vector<int>& nums, int k) {
        int n = nums.size();
        long long ans = 0;
        long long current_cost = 0;
        // segments stores {max_value, count} for the current window [l, r]
        deque<pair<int, int>> segments;
        int r = n - 1;

        // We iterate l from right to left to easily update the running maximums.
        for (int l = n - 1; l >= 0; --l) {
            int count = 1;
            // When adding nums[l], it becomes the running max for subsequent elements
            // until we hit an element larger than nums[l].
            while (!segments.empty() && nums[l] >= segments.front().first) {
                current_cost += (long long)(nums[l] - segments.front().first) * segments.front().second;
                count += segments.front().second;
                segments.pop_front();
            }
            segments.push_front({nums[l], count});

            // Maintain the condition that current_cost <= k by shrinking from the right.
            while (current_cost > k) {
                // Remove the contribution of the element at index r.
                // Its running maximum is the value of the last segment in the deque.
                current_cost -= (long long)(segments.back().first - nums[r]);
                segments.back().second--;
                if (segments.back().second == 0) {
                    segments.pop_back();
                }
                r--;
            }
            // All subarrays [l, i] for l <= i <= r are valid.
            ans += (long long)(r - l + 1);
        }

        return ans;
    }
};