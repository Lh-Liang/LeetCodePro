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
        int k = n / 4; // number of days
        int odd = (k + 1) / 2; // number of odd days
        int even = k / 2; // number of even days
        
        // Sort in descending order
        sort(pizzas.begin(), pizzas.end(), greater<int>());
        
        long long ans = 0;
        
        // Z values from odd-day groups: indices 0 to odd-1
        for (int i = 0; i < odd; i++) {
            ans += pizzas[i];
        }
        
        // Y values from even-day groups: indices odd+1, odd+3, ...
        for (int i = 0; i < even; i++) {
            ans += pizzas[odd + 1 + 2 * i];
        }
        
        return ans;
    }
};
# @lc code=end