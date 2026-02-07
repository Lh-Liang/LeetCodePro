#
# @lc app=leetcode id=3413 lang=cpp
#
# [3413] Maximum Coins From K Consecutive Bags
#

# @lc code=start
class Solution {
public:
    long long maximumCoins(vector<vector<int>>& coins, int k) {
        std::map<int, long long> coinChanges;
        // Register changes at boundaries
        for (const auto &coin : coins) {
            coinChanges[coin[0]] += coin[2];
            coinChanges[coin[1] + 1] -= coin[2];
        }
        // Construct cumulative coins array using prefix sum concept
        std::vector<std::pair<int, long long>> cumulativeCoins;
        long long currentCoins = 0;
        for (const auto &entry : coinChanges) {
            currentCoins += entry.second;
            cumulativeCoins.emplace_back(entry.first, currentCoins);
        }
        // Use sliding window to find max sum in any k consecutive positions
        long long maxCoins = 0;
        size_t start = 0;
        for (size_t end = 0; end < cumulativeCoins.size(); ++end) {
            if (end - start + 1 > k) {
                start++;
            }
            if (end - start + 1 == k) {
                long long windowSum = 0;
                for (size_t i = start; i < end; ++i) {
                    windowSum += cumulativeCoins[i].second * (cumulativeCoins[i + 1].first - cumulativeCoins[i].first);
                }
                maxCoins = std::max(maxCoins, windowSum);
            }
        }
        return maxCoins;
    }
};
# @lc code=end