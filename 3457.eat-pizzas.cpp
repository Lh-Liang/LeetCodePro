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
        int n = pizzas.size();
        int k = n / 4;
        int left = 0;
        int right = n - 1;
        long long ans = 0;
        
        for(int i = 0; i < k; ++i){
            if(i % 2 == 0){ // Odd day
                ans += pizzas[right];
                --right;
                left += 3;
            }
            else{ // Even day
                --right; // Largest becomes Max of this group without adding
                ans += pizzas[right]; // Second-largest added
                --right;
                left += 2;
            }
        }
        return ans;
    }
};
# @lc code=end