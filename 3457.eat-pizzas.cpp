#
# @lc app=leetcode id=3457 lang=cpp
#
# [3457] Eat Pizzas!
#

# @lc code=start
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

class Solution {
public:
    long long maxWeight(vector<int>& pizzas) {
        int n = pizzas.size();
        sort(pizzas.begin(), pizzas.end(), greater<int>());

        int total_days = n / 4;
        int odd_days = (total_days + 1) / 2;
        int even_days = total_days / 2;

        long long total_weight = 0;

        // On odd days, we take the heaviest available pizza as Z.
        for (int i = 0; i < odd_days; ++i) {
            total_weight += pizzas[i];
        }

        // On even days, we need a pizza to be the second heaviest (Y).
        // We skip one (to act as Z for that day) and take the next as Y.
        int current_idx = odd_days;
        for (int i = 0; i < even_days; ++i) {
            total_weight += pizzas[current_idx + 1];
            current_idx += 2;
        }

        return total_weight;
    }
};
# @lc code=end