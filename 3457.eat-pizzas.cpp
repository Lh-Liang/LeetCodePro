#
# @lc app=leetcode id=3457 lang=cpp
#
# [3457] Eat Pizzas!
#

# @lc code=start
class Solution {
public:
    long long maxWeight(vector<int>& pizzas) {
        int n = pizzas.size();
        sort(pizzas.begin(), pizzas.end());
        int days = n / 4;
        int odd_days = (days + 1) / 2;
        int even_days = days / 2;
        long long sum = 0;
        // Sum the largest odd_days pizzas
        for (int i = 0; i < odd_days; ++i) {
            sum += pizzas[n - 1 - i];
        }
        // For even days, sum the mins of pairs from next 2*even_days
        int end_pair = n - odd_days - 1;
        for (int j = 0; j < even_days; ++j) {
            int offset = 1 + 2 * j;
            sum += pizzas[end_pair - offset];
        }
        return sum;
    }
};
# @lc code=end