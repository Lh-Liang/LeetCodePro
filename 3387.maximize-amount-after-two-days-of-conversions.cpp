#
# @lc app=leetcode id=3387 lang=cpp
#
# [3387] Maximize Amount After Two Days of Conversions
#

# @lc code=start
#include <vector>
#include <string>
#include <unordered_map>
#include <queue>
#include <algorithm>

using namespace std;

class Solution {
public:
    /**
     * Helper function to find the conversion rate from the start currency to all 
     * reachable currencies using a BFS approach.
     */
    unordered_map<string, double> getRates(string start, vector<vector<string>>& pairs, vector<double>& rates) {
        unordered_map<string, vector<pair<string, double>>> adj;
        for (int i = 0; i < (int)pairs.size(); ++i) {
            string u = pairs[i][0];
            string v = pairs[i][1];
            double r = rates[i];
            adj[u].push_back({v, r});
            adj[v].push_back({u, 1.0 / r});
        }

        unordered_map<string, double> dist;
        dist[start] = 1.0;
        queue<string> q;
        q.push(start);

        while (!q.empty()) {
            string u = q.front();
            q.pop();

            if (adj.count(u)) {
                for (auto& edge : adj[u]) {
                    string v = edge.first;
                    double r = edge.second;
                    if (dist.find(v) == dist.end()) {
                        dist[v] = dist[u] * r;
                        q.push(v);
                    }
                }
            }
        }
        return dist;
    }

    double maxAmount(string initialCurrency, vector<vector<string>>& pairs1, vector<double>& rates1, vector<vector<string>>& pairs2, vector<double>& rates2) {
        // Calculate the best conversion rate from initialCurrency to all others on Day 1
        unordered_map<string, double> map1 = getRates(initialCurrency, pairs1, rates1);
        // Calculate the best conversion rate from initialCurrency to all others on Day 2
        unordered_map<string, double> map2 = getRates(initialCurrency, pairs2, rates2);

        double max_val = 0.0;
        // For every currency we could hold at the end of Day 1
        for (auto const& item : map1) {
            string currency = item.first;
            double rate1 = item.second;
            
            // If we can convert this currency back to initialCurrency on Day 2
            if (map2.count(currency)) {
                // Amount of initialCurrency at end = (Amt of C at end Day 1) * (Rate C to Initial Day 2)
                // Rate C to Initial Day 2 = 1.0 / (Rate Initial to C Day 2)
                max_val = max(max_val, rate1 / map2[currency]);
            }
        }

        return max_val;
    }
};
# @lc code=end