#
# @lc app=leetcode id=3387 lang=cpp
#
# [3387] Maximize Amount After Two Days of Conversions
#

# @lc code=start
#include <string>
#include <vector>
#include <unordered_map>
#include <queue>
#include <algorithm>

using namespace std;

class Solution {
public:
    double maxAmount(string initialCurrency, vector<vector<string>>& pairs1, vector<double>& rates1, vector<vector<string>>& pairs2, vector<double>& rates2) {
        // Map to store max amount of each currency reachable on Day 1
        unordered_map<string, double> day1_amounts;
        day1_amounts[initialCurrency] = 1.0;
        
        // Build graph for Day 1
        unordered_map<string, vector<pair<string, double>>> adj1;
        for (int i = 0; i < (int)pairs1.size(); ++i) {
            adj1[pairs1[i][0]].push_back({pairs1[i][1], rates1[i]});
            adj1[pairs1[i][1]].push_back({pairs1[i][0], 1.0 / rates1[i]});
        }
        
        // BFS to find all reachable currencies and their amounts at the end of Day 1
        queue<string> q;
        q.push(initialCurrency);
        while (!q.empty()) {
            string u = q.front();
            q.pop();
            if (adj1.count(u)) {
                for (auto& edge : adj1[u]) {
                    if (day1_amounts.find(edge.first) == day1_amounts.end()) {
                        day1_amounts[edge.first] = day1_amounts[u] * edge.second;
                        q.push(edge.first);
                    }
                }
            }
        }
        
        // Map to store relative rates from initialCurrency on Day 2
        unordered_map<string, double> day2_relative_rates;
        day2_relative_rates[initialCurrency] = 1.0;
        
        // Build graph for Day 2
        unordered_map<string, vector<pair<string, double>>> adj2;
        for (int i = 0; i < (int)pairs2.size(); ++i) {
            adj2[pairs2[i][0]].push_back({pairs2[i][1], rates2[i]});
            adj2[pairs2[i][1]].push_back({pairs2[i][0], 1.0 / rates2[i]});
        }
        
        // BFS to find conversion rates from initialCurrency on Day 2
        q.push(initialCurrency);
        while (!q.empty()) {
            string u = q.front();
            q.pop();
            if (adj2.count(u)) {
                for (auto& edge : adj2[u]) {
                    if (day2_relative_rates.find(edge.first) == day2_relative_rates.end()) {
                        day2_relative_rates[edge.first] = day2_relative_rates[u] * edge.second;
                        q.push(edge.first);
                    }
                }
            }
        }
        
        // Calculate the maximum possible initialCurrency at the end of Day 2
        double max_val = 1.0;
        for (auto const& [curr, amount1] : day1_amounts) {
            if (day2_relative_rates.count(curr)) {
                // Rate to convert curr back to initialCurrency is 1 / day2_relative_rates[curr]
                max_val = max(max_val, amount1 / day2_relative_rates[curr]);
            }
        }
        
        return max_val;
    }
};
# @lc code=end