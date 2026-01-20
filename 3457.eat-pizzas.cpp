#include <bits/stdc++.h>
using namespace std;

//
// @lc app=leetcode id=3457 lang=cpp
//
// [3457] Eat Pizzas!
//

// @lc code=start
class Solution {
public:
    long long maxWeight(vector<int>& pizzas) {
        sort(pizzas.begin(), pizzas.end());
        int n = (int)pizzas.size();
        int m = n / 4;
        int odd = (m + 1) / 2;
        int even = m / 2;

        long long ans = 0;
        int l = 0, r = n - 1;

        // Odd days: gain Z (largest in the group)
        for (int i = 0; i < odd; i++) {
            ans += pizzas[r--];
            l += 3; // consume 3 smallest as fillers
        }

        // Even days: gain Y (2nd largest in the group)
        for (int i = 0; i < even; i++) {
            // take Z (largest) but not counted
            r--;
            // take Y (next largest) and count it
            ans += pizzas[r--];
            l += 2; // consume 2 smallest as fillers
        }

        return ans;
    }
};
// @lc code=end
