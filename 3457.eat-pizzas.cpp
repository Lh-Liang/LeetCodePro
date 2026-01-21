#include <bits/stdc++.h>
using namespace std;

/*
 * @lc app=leetcode id=3457 lang=cpp
 *
 * [3457] Eat Pizzas!
 */

// @lc code=start
class Solution {
public:
    long long maxWeight(vector<int>& pizzas) {
        int n = (int)pizzas.size();
        sort(pizzas.begin(), pizzas.end());

        int m = n / 4;
        int oddDays = (m + 1) / 2;
        int evenDays = m / 2;

        long long ans = 0;
        int l = 0, r = n - 1;

        // Odd days: gain Z (maximum). Use 3 smallest as fillers.
        for (int i = 0; i < oddDays; i++) {
            ans += pizzas[r--];
            l += 3;
        }

        // Even days: gain Y (second maximum). Use largest as Z (wasted), next as Y (gained), 2 smallest as fillers.
        for (int i = 0; i < evenDays; i++) {
            r--;                // take Z (wasted)
            ans += pizzas[r--]; // take Y (gained)
            l += 2;
        }

        return ans;
    }
};
// @lc code=end
