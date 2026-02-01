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
        // Step 1: Find the maximum amount of each currency we can get on Day 1.
        // Since there are no contradictions or cycles, any path will give the same rate.
        unordered_map<string, double> max_day1 = get_rates(initialCurrency, pairs1, rates1);

        // Step 2: Find the conversion rate from initialCurrency to any other currency on Day 2.
        // This allows us to calculate the rate from any currency back to initialCurrency on Day 2.
        unordered_map<string, double> rates_day2 = get_rates(initialCurrency, pairs2, rates2);

        // Step 3: For each currency reachable on Day 1, calculate how much initialCurrency we can get back on Day 2.
        // If we have 'amt' of currency 'C' and the rate 'initialCurrency -> C' on Day 2 is 'r2',
        // then the rate 'C -> initialCurrency' on Day 2 is '1/r2'.
        // So we get 'amt * (1/r2)' of initialCurrency.
        double max_initial = 1.0;
        for (auto const& [curr, amt] : max_day1) {
            if (rates_day2.count(curr)) {
                max_initial = max(max_initial, amt / rates_day2[curr]);
            }
        }

        return max_initial;
    }

private:
    unordered_map<string, double> get_rates(string start, const vector<vector<string>>& pairs, const vector<double>& rates) {
        unordered_map<string, vector<pair<string, double>>> adj;
        for (size_t i = 0; i < pairs.size(); ++i) {
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

            if (adj.count(u)) {
                for (auto& edge : adj[u]) {
                    const string& v = edge.first;
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
};
# @lc code=end