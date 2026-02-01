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
        int n = pizzas.size();
        sort(pizzas.begin(), pizzas.end());
        
        int totalDays = n / 4;
        int oddDays = (totalDays + 1) / 2;
        int evenDays = totalDays / 2;
        
        long long totalWeight = 0;
        int right = n - 1;
        
        // On odd-numbered days (1, 3, 5, ...), we gain the weight of the largest pizza (Z).
        // To maximize this, we pick the largest available pizzas for these days.
        for (int i = 0; i < oddDays; ++i) {
            totalWeight += pizzas[right--];
        }
        
        // On even-numbered days (2, 4, 6, ...), we gain the weight of the second largest pizza (Y).
        // To maximize this, we pick the two largest available pizzas; 
        // the first is the 'largest' (Z) and the second is the 'second largest' (Y) which we gain.
        for (int i = 0; i < evenDays; ++i) {
            right--; // Skip the largest available pizza (this will be Z for the even day)
            totalWeight += pizzas[right--]; // Gain the second largest (this will be Y for the even day)
        }
        
        return totalWeight;
    }
};
# @lc code=end