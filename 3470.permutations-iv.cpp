# 
# @lc app=leetcode id=3470 lang=cpp
# 
# [3470] Permutations IV
# 

# @lc code=start
class Solution {
public:
    vector<int> permute(int n, long long k) {
        vector<int> result;
        vector<int> nums(n);
        iota(nums.begin(), nums.end(), 1); // Initialize nums with 1 to n
        long long count = 0;
        bool found = false;
        function<void(int)> backtrack = [&](int index) {
            if (index == n) {
                count++;
                if (count == k) {
                    result = nums;
                    found = true;
                }
                return;
            }
            for (int i = index; i < n && !found; ++i) {
                swap(nums[index], nums[i]);
                if (index == 0 || ((nums[index] % 2 != nums[index - 1] % 2))) { // Check alternating condition
                    backtrack(index + 1);
                }
                swap(nums[index], nums[i]); // Backtrack step (undo swap) 
            }
        };
        backtrack(0); 
        return result; 
    } 
}; 
# @lc code=end