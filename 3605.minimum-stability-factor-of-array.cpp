#
# @lc app=leetcode id=3605 lang=cpp
#
# [3605] Minimum Stability Factor of Array
#

# @lc code=start
class Solution {
public:
    int hcf(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
    
    bool canAchieveStability(vector<int>& nums, int maxC, int targetLength) {
        int n = nums.size();
        for (int i = 0; i <= n - targetLength; ++i) {
            int currentHCF = nums[i];
            int modificationCount = 0;
            for (int j = i; j < i + targetLength && j < n; ++j) {
                currentHCF = hcf(currentHCF, nums[j]);
                if (currentHCF < 2) break;
                if (j == i + targetLength - 1) {
                    modificationCount++;
                    if (modificationCount > maxC) return false;
                }
            }
        }
        return true;
    }
    
    int minStable(vector<int>& nums, int maxC) {
        int left = 1, right = nums.size();
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (canAchieveStability(nums, maxC, mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return canAchieveStability(nums, maxC, left) ? left : 0;
    }
};
# @lc code=end