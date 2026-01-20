#
# @lc app=leetcode id=3457 lang=cpp
#
# [3457] Eat Pizzas!
#

# @lc code=start
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    long long maxWeight(vector<int>& pizzas) {
        // Sort pizzas in descending order to easily pick the heaviest ones
        sort(pizzas.rbegin(), pizzas.rend());
        
        int n = pizzas.size();
        int total_days = n / 4;
        
        // Calculate how many odd and even days we have
        int odd_days = (total_days + 1) / 2;
        int even_days = total_days / 2;
        
        long long total_weight = 0;
        int current_idx = 0;
        
        // On odd-numbered days, we gain the heaviest pizza (Z) of the 4.
        // To maximize, we pick the largest available pizzas.
        for (int i = 0; i < odd_days; ++i) {
            total_weight += pizzas[current_idx++];
        }
        
        // On even-numbered days, we gain the second heaviest pizza (Y) of the 4.
        // To maximize, we pick the next largest available pizzas, but for each one,
        // we must skip one heavier pizza to act as the 'Z' for that day.
        for (int i = 0; i < even_days; ++i) {
            current_idx++; // Skip the pizza that will act as Z
            total_weight += pizzas[current_idx++]; // Take the pizza that will act as Y
        }
        
        return total_weight;
    }
};
# @lc code=end