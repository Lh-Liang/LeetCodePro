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
    double maxAmount(string initialCurrency, vector<vector<string>>& pairs1, vector<double>& rates1, vector<vector<string>>& pairs2, vector<double>& rates2) {
        // Helper function to find all reachable currencies and their rates from a start currency
        auto getRates = [&](const string& start, const vector<vector<string>>& pairs, const vector<double>& rates) {
            unordered_map<string, vector<pair<string, double>>> adj;
            for (int i = 0; i < (int)pairs.size(); ++i) {
                adj[pairs[i][0]].push_back({pairs[i][1], rates[i]});
                adj[pairs[i][1]].push_back({pairs[i][0], 1.0 / rates[i]});
            }
            
            unordered_map<string, double> dist;
            dist[start] = 1.0;
            queue<string> q;
            q.push(start);
            
            while (!q.empty()) {
                string u = q.front();
                q.pop();
                
                for (auto& edge : adj[u]) {
                    if (dist.find(edge.first) == dist.end()) {
                        dist[edge.first] = dist[u] * edge.second;
                        q.push(edge.first);
                    }
                }
            }
            return dist;
        };

        // Day 1: Maximize amount of any currency starting from initialCurrency
        unordered_map<string, double> day1_rates = getRates(initialCurrency, pairs1, rates1);
        
        // Day 2: Find conversion rates from initialCurrency to others to calculate the return path
        unordered_map<string, double> day2_rates = getRates(initialCurrency, pairs2, rates2);

        double max_val = 1.0; // Default: do nothing on both days

        // For every currency held at the end of Day 1, try converting it back on Day 2
        for (auto const& [curr, r1] : day1_rates) {
            // If currency 'curr' is part of the Day 2 graph
            if (day2_rates.count(curr)) {
                // Final amount = (initial -> curr on Day 1) * (curr -> initial on Day 2)
                // Since day2_rates[curr] is (initial -> curr), the inverse is (1.0 / day2_rates[curr])
                max_val = max(max_val, r1 / day2_rates[curr]);
            }
        }

        return max_val;
    }
};
# @lc code=end