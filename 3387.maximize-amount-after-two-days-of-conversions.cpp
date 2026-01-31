#
# @lc app=leetcode id=3387 lang=cpp
#
# [3387] Maximize Amount After Two Days of Conversions
#

# @lc code=start
#include <vector>
#include <string>
#include <map>
#include <queue>
#include <algorithm>

using namespace std;

class Solution {
public:
    /**
     * Helper function to find the conversion rates from a starting currency to all reachable currencies
     * using a BFS approach on the conversion graph.
     */
    map<string, double> getRates(string start, map<string, vector<pair<string, double>>>& adj) {
        map<string, double> rates;
        rates[start] = 1.0;
        queue<string> q;
        q.push(start);
        
        while (!q.empty()) {
            string u = q.front();
            q.pop();
            
            if (adj.count(u)) {
                for (auto& edge : adj[u]) {
                    string v = edge.first;
                    double r = edge.second;
                    // If we haven't visited this currency, calculate its rate and add to queue
                    if (rates.find(v) == rates.end()) {
                        rates[v] = rates[u] * r;
                        q.push(v);
                    }
                }
            }
        }
        return rates;
    }

    double maxAmount(string initialCurrency, vector<vector<string>>& pairs1, vector<double>& rates1, vector<vector<string>>& pairs2, vector<double>& rates2) {
        // Step 1: Build adjacency lists for Day 1 and Day 2 conversion graphs
        map<string, vector<pair<string, double>>> adj1, adj2;
        
        for (int i = 0; i < (int)pairs1.size(); ++i) {
            string u = pairs1[i][0];
            string v = pairs1[i][1];
            double r = rates1[i];
            adj1[u].push_back({v, r});
            adj1[v].push_back({u, 1.0 / r});
        }
        
        for (int i = 0; i < (int)pairs2.size(); ++i) {
            string u = pairs2[i][0];
            string v = pairs2[i][1];
            double r = rates2[i];
            adj2[u].push_back({v, r});
            adj2[v].push_back({u, 1.0 / r});
        }
        
        // Step 2: Calculate maximum possible amount of each currency at the end of Day 1
        map<string, double> day1_amounts = getRates(initialCurrency, adj1);
        
        // Step 3: Calculate the conversion rates from initialCurrency to other currencies on Day 2
        // We use this to find the reverse rate (C -> initialCurrency) as 1 / rate(initialCurrency -> C)
        map<string, double> day2_rates_from_initial = getRates(initialCurrency, adj2);
        
        double max_val = 1.0; // The minimum result is 1.0 (by doing nothing)
        
        // Step 4: For each currency held at the end of Day 1, try to convert it back to initialCurrency on Day 2
        for (auto const& [curr, amount] : day1_amounts) {
            if (day2_rates_from_initial.count(curr)) {
                // amount_final = amount_day1 * rate_day2(curr -> initial)
                // where rate_day2(curr -> initial) = 1.0 / rate_day2(initial -> curr)
                max_val = max(max_val, amount / day2_rates_from_initial[curr]);
            }
        }
        
        return max_val;
    }
};
# @lc code=end