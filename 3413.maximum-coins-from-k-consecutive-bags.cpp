class Solution {
public:
    long long maximumCoins(vector<vector<int>>& coins, int k) {
        map<int, long long> points;
        // Accumulate coins at each point
        for (auto& coin : coins) {
            points[coin[0]] += coin[2];
            points[coin[1] + 1] -= coin[2];
        }
        // Create prefix sum array
        vector<pair<int, long long>> prefix;
        long long sum = 0;
        for (auto& p : points) {
            sum += p.second;
            if (!prefix.empty() && prefix.back().first == p.first - 1) {
                prefix.back().second = sum;
            } else {
                prefix.emplace_back(p.first - 1, sum);
                prefix.emplace_back(p.first, sum);
            }
        }
        // Apply sliding window on accumulated values to find max within k consecutive positions
        long long max_coins = 0;
        int n = prefix.size(); 
        for (int i = 0, j = 0; i < n && j < n;) { 
            if (prefix[j].first - prefix[i].first + 1 <= k) { 
                max_coins = max(max_coins, j > 0 ? prefix[j].second - (i > 0 ? prefix[i-1].second : 0LL) : prefix[j].second); 
                ++j; 
            } else { 
                ++i; 
            } 
        } 
        return max_coins; 
    } 
};