#
# @lc app=leetcode id=3457 lang=cpp
#
# [3457] Eat Pizzas!
#
# @lc code=start
class Solution {
public:
    long long maxWeight(vector<int>& pizzas) {
        sort(pizzas.begin(), pizzas.end()); // Step 1: Sort the pizzas by weight.
        long long totalWeight = 0;
        int n = pizzas.size(); // Step 2: Get size of pizzas array.
        // Step 3: Iterate backwards through sorted pizzas in chunks of 4.
        for (int i = n - 1; i >= 0; i -= 4) {
            // Step 4: Add Z (heaviest in group of four) on odd days.
            totalWeight += pizzas[i]; 
            if (i - 1 >= 0) { // Ensure there is a second pizza to consider.
                // Add Y (second heaviest) on even days.
                totalWeight += pizzas[i - 1];
            }
        }
        return totalWeight; // Return maximum weight gained.
    }
};
# @lc code=end