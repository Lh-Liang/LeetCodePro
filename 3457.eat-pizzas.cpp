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
        long long totalWeight = 0;
        int n = pizzas.size();
        for (int i = n - 1; i >= 0; i -= 4) {
            // Odd days: take Z (largest) from group of four
            totalWeight += pizzas[i]; 
            if (i - 2 >= 0) { 
                // Even days: take Y (second largest) from group of four
                totalWeight += pizzas[i - 2]; 
            }
        }
        return totalWeight;
    }
};
# @lc code=end