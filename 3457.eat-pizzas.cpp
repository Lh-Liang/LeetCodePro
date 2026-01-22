#
# @lc app=leetcode id=3457 lang=cpp
#
# [3457] Eat Pizzas!
#
# @lc code=start
class Solution {
public:
    long long maxWeight(vector<int>& pizzas) {
        sort(pizzas.begin(), pizzas.end(), greater<int>());
        int n = pizzas.size();
        int days = n / 4;
        int oddDays = (days + 1) / 2;
        int evenDays = days / 2;
        
        long long result = 0;
        
        // Odd days: collect Z (max) from each group
        for (int i = 0; i < oddDays; i++) {
            result += pizzas[i];
        }
        
        // Even days: collect Y (second max) from each group
        // For each even day, we use two consecutive pizzas (Z, Y) starting from index oddDays
        // Y positions: oddDays+1, oddDays+3, oddDays+5, ...
        int idx = oddDays + 1;
        for (int i = 0; i < evenDays; i++) {
            result += pizzas[idx];
            idx += 2;
        }
        
        return result;
    }
};
# @lc code=end