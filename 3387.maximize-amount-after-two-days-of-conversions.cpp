#
# @lc app=leetcode id=3387 lang=cpp
#
# [3387] Maximize Amount After Two Days of Conversions
#

# @lc code=start
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <queue>
#include <algorithm>

using namespace std;

class Solution {
public:
    double maxAmount(string initialCurrency, vector<vector<string>>& pairs1, vector<double>& rates1, vector<vector<string>>& pairs2, vector<double>& rates2) {
        
        // Helper lambda to perform BFS and calculate conversion rates from a start node
        auto bfs = [&](string startNode, const vector<vector<string>>& pairs, const vector<double>& rates) {
            unordered_map<string, vector<pair<string, double>>> adj;
            // Build the graph. Since conversions are reversible, add edges in both directions.
            // u -> v with rate r
            // v -> u with rate 1/r
            for (size_t i = 0; i < pairs.size(); ++i) {
                adj[pairs[i][0]].push_back({pairs[i][1], rates[i]});
                adj[pairs[i][1]].push_back({pairs[i][0], 1.0 / rates[i]});
            }

            unordered_map<string, double> conversionRates;
            conversionRates[startNode] = 1.0;
            queue<string> q;
            q.push(startNode);

            while (!q.empty()) {
                string curr = q.front();
                q.pop();

                double currentRate = conversionRates[curr];

                if (adj.find(curr) != adj.end()) {
                    for (const auto& edge : adj[curr]) {
                        string neighbor = edge.first;
                        double rate = edge.second;
                        // Since there are no contradictions/cycles, we only visit each node once.
                        if (conversionRates.find(neighbor) == conversionRates.end()) {
                            conversionRates[neighbor] = currentRate * rate;
                            q.push(neighbor);
                        }
                    }
                }
            }
            return conversionRates;
        };

        // Step 1: Calculate max conversion amounts from initialCurrency on Day 1
        // map1[C] will hold the amount of currency C we get for 1.0 initialCurrency
        unordered_map<string, double> map1 = bfs(initialCurrency, pairs1, rates1);

        // Step 2: Calculate conversion rates on Day 2.
        // We run BFS from initialCurrency again.
        // map2[C] holds the amount of C we get for 1.0 initialCurrency on Day 2.
        // Consequently, the rate to convert C back to initialCurrency is 1.0 / map2[C].
        unordered_map<string, double> map2 = bfs(initialCurrency, pairs2, rates2);

        double maxVal = 0.0;

        // Step 3: Iterate through all intermediate currencies reachable on Day 1
        for (const auto& [currency, amount1] : map1) {
            // Check if this currency is connected to initialCurrency on Day 2
            if (map2.count(currency)) {
                // Determine the rate to convert 'currency' back to 'initialCurrency'
                double rateBack = 1.0 / map2[currency];
                
                // Total amount after the full cycle
                double totalAmount = amount1 * rateBack;
                
                if (totalAmount > maxVal) {
                    maxVal = totalAmount;
                }
            }
        }

        return maxVal;
    }
};
# @lc code=end