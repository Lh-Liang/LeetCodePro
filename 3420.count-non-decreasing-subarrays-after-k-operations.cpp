# @lc code=start
#include <vector>

class Solution {
public:
    long long countNonDecreasingSubarrays(std::vector<int>& nums, int k) {
        long long count = 0;
        int n = nums.size();
        int start = 0;
        int total_increments = 0;

        for (int end = 0; end < n; ++end) {
            if (end > 0 && nums[end] < nums[end - 1]) {
                total_increments += nums[end - 1] - nums[end];
            }
            
            while (total_increments > k && start <= end) {
                if (start + 1 < n && nums[start + 1] < nums[start]) {
                    total_increments -= nums[start] - nums[start + 1];
                }
                start++;
            }

            count += (end - start + 1);
        }

        return count;
    }
};
# @lc code=end