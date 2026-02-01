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
        // Sort pizzas in descending order to easily pick the largest weights.
        sort(pizzas.begin(), pizzas.end(), greater<int>());
        
        int n = pizzas.size();
        int totalDays = n / 4;
        int oddDays = (totalDays + 1) / 2;
        int evenDays = totalDays / 2;
        
        long long totalWeight = 0;
        
        // On odd days, we gain the weight of the largest pizza (Z).
        // We take the 'oddDays' largest pizzas available.
        for (int i = 0; i < oddDays; ++i) {
            totalWeight += pizzas[i];
        }
        
        // On even days, we gain the weight of the second largest pizza (Y).
        // To maximize Y, we must skip one larger pizza (to act as Z) for each even day.
        // We start from the index immediately following the pizzas used for odd days.
        int currentIndex = oddDays;
        for (int j = 0; j < evenDays; ++j) {
            // Skip pizzas[currentIndex] (used as Z) and take pizzas[currentIndex + 1] (used as Y).
            totalWeight += pizzas[currentIndex + 1];
            currentIndex += 2;
        }
        
        return totalWeight;
    }
};
# @lc code=end