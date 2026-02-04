#
# @lc app=leetcode id=3387 lang=cpp
#
# [3387] Maximize Amount After Two Days of Conversions
#

# @lc code=start
#include <unordered_map>
#include <vector>
#include <string>
#include <queue>
using namespace std;

class Solution {
public:
    double maxAmount(string initialCurrency, vector<vector<string>>& pairs1, vector<double>& rates1, vector<vector<string>>& pairs2, vector<double>& rates2) {
        // Collect all currencies
        unordered_map<string, int> currency2idx;
        vector<string> currencies;
        auto add_currency = [&](const string& c) {
            if (!currency2idx.count(c)) {
                currency2idx[c] = currencies.size();
                currencies.push_back(c);
            }
        };
        add_currency(initialCurrency);
        for (const auto& p : pairs1) { add_currency(p[0]); add_currency(p[1]); }
        for (const auto& p : pairs2) { add_currency(p[0]); add_currency(p[1]); }
        int n = currencies.size();
        
        // Build day 1 graph with inverses
        vector<vector<pair<int, double>>> g1(n);
        for (int i = 0; i < pairs1.size(); ++i) {
            int u = currency2idx[pairs1[i][0]], v = currency2idx[pairs1[i][1]];
            double r = rates1[i];
            g1[u].emplace_back(v, r);
            g1[v].emplace_back(u, 1.0 / r);
        }
        // Day 1 DP: maximize each currency
        vector<double> dp1(n, 0.0);
        dp1[currency2idx[initialCurrency]] = 1.0;
        for (int iter = 0; iter < n-1; ++iter) {
            for (int u = 0; u < n; ++u) {
                if (dp1[u] > 0) {
                    for (auto& [v, r] : g1[u]) {
                        if (dp1[v] < dp1[u] * r)
                            dp1[v] = dp1[u] * r;
                    }
                }
            }
        }
        // Build day 2 graph with inverses
        vector<vector<pair<int, double>>> g2(n);
        for (int i = 0; i < pairs2.size(); ++i) {
            int u = currency2idx[pairs2[i][0]], v = currency2idx[pairs2[i][1]];
            double r = rates2[i];
            g2[u].emplace_back(v, r);
            g2[v].emplace_back(u, 1.0 / r);
        }
        // For each currency, propagate through day 2
        double ans = dp1[currency2idx[initialCurrency]]; // handle no conversion on day 2
        for (int start = 0; start < n; ++start) {
            if (dp1[start] == 0) continue;
            vector<double> dp2(n, 0.0);
            dp2[start] = dp1[start];
            for (int iter = 0; iter < n-1; ++iter) {
                for (int u = 0; u < n; ++u) {
                    if (dp2[u] > 0) {
                        for (auto& [v, r] : g2[u]) {
                            if (dp2[v] < dp2[u] * r)
                                dp2[v] = dp2[u] * r;
                        }
                    }
                }
            }
            ans = max(ans, dp2[currency2idx[initialCurrency]]);
        }
        // Final verification: compare with no conversion at all
        ans = max(ans, 1.0);
        return ans;
    }
};
# @lc code=end