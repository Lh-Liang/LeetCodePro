//
// @lc app=leetcode id=3457 lang=cpp
//
// [3457] Eat Pizzas!
//

// @lc code=start
class Solution {
public:
    long long maxWeight(vector<int>& pizzas) {
        int n = pizzas.size();
        sort(pizzas.begin(), pizzas.end());
        long long total = 0;
        int day = 1;
        for (int i = n - 1; i >= 3; i -= 4) {
            // pizzas[i-3], pizzas[i-2], pizzas[i-1], pizzas[i]
            if (day % 2 == 1) {
                total += pizzas[i];      // Odd day: add largest (Z)
            } else {
                total += pizzas[i - 1];  // Even day: add second largest (Y)
            }
            day++;
        }
        return total;
    }
};
// @lc code=end