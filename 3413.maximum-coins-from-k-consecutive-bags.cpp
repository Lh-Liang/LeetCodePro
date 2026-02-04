#
# @lc app=leetcode id=3413 lang=cpp
#
# [3413] Maximum Coins From K Consecutive Bags
#

# @lc code=start
class Solution {
public:
    long long maximumCoins(vector<vector<int>>& coins, int k) {
        map<int, int> coinMap;
        for (auto &c : coins) {
            coinMap[c[0]] += c[2];
            coinMap[c[1] + 1] -= c[2];
        }
        long long maxCoins = 0, currentCoins = 0;
        vector<pair<int, int>> points(coinMap.begin(), coinMap.end());
        size_t left = 0, right = 0; 
        while (right < points.size()) {
            currentCoins += points[right].second;
            while (points[right].first - points[left].first >= k) {
                currentCoins -= points[left].second;
                ++left;
            }
            maxCoins = max(maxCoins, currentCoins);
            ++right;
        }
        return maxCoins;
    }
};
# @lc code=end