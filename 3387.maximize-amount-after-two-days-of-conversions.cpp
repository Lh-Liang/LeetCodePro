#
# @lc app=leetcode id=3387 lang=cpp
#
# [3387] Maximize Amount After Two Days of Conversions
#
# @lc code=start
class Solution {
public:
    double maxAmount(string initialCurrency, vector<vector<string>>& pairs1, vector<double>& rates1, vector<vector<string>>& pairs2, vector<double>& rates2) {
        // Step 1: Map all currencies to indices
        unordered_map<string, int> currencyIndex;
        int idx = 0;
        auto registerCurrency = [&](const string& s) {
            if (!currencyIndex.count(s)) currencyIndex[s] = idx++;
        };
        registerCurrency(initialCurrency);
        for (auto& p : pairs1) { registerCurrency(p[0]); registerCurrency(p[1]); }
        for (auto& p : pairs2) { registerCurrency(p[0]); registerCurrency(p[1]); }
        int n = idx;
        // Step 2: Build adjacency lists for both days with direct and reverse rates
        vector<vector<pair<int, double>>> g1(n), g2(n);
        for (int i = 0; i < pairs1.size(); ++i) {
            int u = currencyIndex[pairs1[i][0]], v = currencyIndex[pairs1[i][1]];
            g1[u].emplace_back(v, rates1[i]);
            g1[v].emplace_back(u, 1.0 / rates1[i]);
        }
        for (int i = 0; i < pairs2.size(); ++i) {
            int u = currencyIndex[pairs2[i][0]], v = currencyIndex[pairs2[i][1]];
            g2[u].emplace_back(v, rates2[i]);
            g2[v].emplace_back(u, 1.0 / rates2[i]);
        }
        // Step 3: Day 1 DP (Bellman-Ford-like for max product)
        vector<double> day1(n, 0.0);
        day1[currencyIndex[initialCurrency]] = 1.0;
        for (int iter = 0; iter < n; ++iter) {
            vector<double> next = day1;
            for (int u = 0; u < n; ++u) {
                for (auto& [v, rate] : g1[u]) {
                    if (day1[u] * rate > next[v]) {
                        next[v] = day1[u] * rate;
                    }
                }
            }
            day1 = next;
        }
        // Step 4: For each possible currency after day 1, run Day 2 DP to maximize initialCurrency
        double res = day1[currencyIndex[initialCurrency]]; // Option to do nothing
        for (int start = 0; start < n; ++start) {
            if (day1[start] == 0.0) continue;
            vector<double> day2(n, 0.0);
            day2[start] = day1[start];
            for (int iter = 0; iter < n; ++iter) {
                vector<double> next = day2;
                for (int u = 0; u < n; ++u) {
                    for (auto& [v, rate] : g2[u]) {
                        if (day2[u] * rate > next[v]) {
                            next[v] = day2[u] * rate;
                        }
                    }
                }
                day2 = next;
            }
            res = max(res, day2[currencyIndex[initialCurrency]]);
        }
        return res;
    }
};
# @lc code=end