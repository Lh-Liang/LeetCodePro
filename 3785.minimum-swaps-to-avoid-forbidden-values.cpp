#
# @lc app=leetcode id=3785 lang=cpp
#
# [3785] Minimum Swaps to Avoid Forbidden Values
#
# @lc code=start
class Solution {
public:
    int minSwaps(vector<int>& nums, vector<int>& forbidden) {
        int n = nums.size();
        unordered_map<int, int> num_count;
        unordered_map<int, int> t_count;
        unordered_map<int, int> conflict_count;
        int total_bad = 0;
        int max_conflict = 0;
        for (int i = 0; i < n; ++i) {
            num_count[nums[i]]++;
            t_count[forbidden[i]]++;
            if (nums[i] == forbidden[i]) {
                total_bad++;
                conflict_count[nums[i]]++;
            }
        }
        for (auto& p : t_count) {
            int v = p.first;
            int tv = p.second;
            int cv = num_count[v];
            if (tv > n - cv) {
                return -1;
            }
        }
        for (auto& p : conflict_count) {
            max_conflict = max(max_conflict, p.second);
        }
        if (total_bad == 0) {
            return 0;
        }
        int mm = min(total_bad / 2, total_bad - max_conflict);
        return total_bad - mm;
    }
};
# @lc code=end