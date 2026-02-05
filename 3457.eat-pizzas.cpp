#
# @lc app=leetcode id=3457 lang=cpp
#
# [3457] Eat Pizzas!
#
# @lc code=start
class Solution {
public:
    long long maxWeight(vector<int>& pizzas) {
        sort(pizzas.begin(), pizzas.end());
        int n = pizzas.size();
        int days = n / 4;
        long long ans = 0;
        for (int i = 0; i < days; ++i) {
            // Odd day: take Z (largest in the group)
            if (i % 2 == 0) {
                ans += pizzas[n - 1 - i * 4];
            } else {
                // Even day: take Y (second largest in the group)
                ans += pizzas[n - 2 - i * 4];
            }
        }
        return ans;
    }
};
# @lc code=end