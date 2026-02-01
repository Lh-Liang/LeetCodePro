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
        // Step 1: Calculate all reachable currencies and their amounts at the end of Day 1.
        unordered_map<string, double> day1_amounts;
        day1_amounts[initialCurrency] = 1.0;
        
        unordered_map<string, vector<pair<string, double>>> adj1;
        for (size_t i = 0; i < pairs1.size(); ++i) {
            adj1[pairs1[i][0]].push_back({pairs1[i][1], rates1[i]});
            adj1[pairs1[i][1]].push_back({pairs1[i][0], 1.0 / rates1[i]});
        }
        
        queue<string> q1;
        q1.push(initialCurrency);
        while (!q1.empty()) {
            string curr = q1.front();
            q1.pop();
            for (auto& edge : adj1[curr]) {
                if (day1_amounts.find(edge.first) == day1_amounts.end()) {
                    day1_amounts[edge.first] = day1_amounts[curr] * edge.second;
                    q1.push(edge.first);
                }
            }
        }
        
        // Step 2: Calculate conversion rates from initialCurrency to other currencies on Day 2.
        unordered_map<string, double> day2_rates;
        day2_rates[initialCurrency] = 1.0;
        
        unordered_map<string, vector<pair<string, double>>> adj2;
        for (size_t i = 0; i < pairs2.size(); ++i) {
            adj2[pairs2[i][0]].push_back({pairs2[i][1], rates2[i]});
            adj2[pairs2[i][1]].push_back({pairs2[i][0], 1.0 / rates2[i]});
        }
        
        queue<string> q2;
        q2.push(initialCurrency);
        while (!q2.empty()) {
            string curr = q2.front();
            q2.pop();
            for (auto& edge : adj2[curr]) {
                if (day2_rates.find(edge.first) == day2_rates.end()) {
                    day2_rates[edge.first] = day2_rates[curr] * edge.second;
                    q2.push(edge.first);
                }
            }
        }
        
        // Step 3: Maximize the final amount of initialCurrency.
        double max_val = 1.0; 
        for (auto const& [curr, amount] : day1_amounts) {
            if (day2_rates.count(curr)) {
                max_val = max(max_val, amount / day2_rates[curr]);
            }
        }
        
        return max_val;
    }
};
# @lc code=end