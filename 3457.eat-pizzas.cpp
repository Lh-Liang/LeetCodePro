#
# @lc app=leetcode id=3457 lang=cpp
#
# [3457] Eat Pizzas!
#

# @lc code=start
class Solution {
public:
    long long maxWeight(vector<int>& pizzas) {
        std::sort(pizzas.begin(), pizzas.end(), std::greater<int>());
        long long totalWeight = 0;
        int n = pizzas.size();
        for (int i = 0; i < n; i += 4) {
            // Odd days: Gain Z (the largest of 4)
            totalWeight += pizzas[i];
            // Even days: Gain Y (the second largest of 4) if applicable
            if (i + 2 < n) {
                totalWeight += pizzas[i + 2];
            }
        }
        return totalWeight;
    }
};
# @lc code=end