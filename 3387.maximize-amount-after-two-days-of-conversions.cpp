#include <bits/stdc++.h>
using namespace std;

// @lc code=start
class Solution {
    using Graph = unordered_map<string, vector<pair<string,double>>>;

    Graph buildGraph(const vector<vector<string>>& pairs, const vector<double>& rates) {
        Graph g;
        int n = (int)pairs.size();
        for (int i = 0; i < n; i++) {
            const string& a = pairs[i][0];
            const string& b = pairs[i][1];
            double r = rates[i];
            g[a].push_back({b, r});
            g[b].push_back({a, 1.0 / r});
        }
        return g;
    }

    unordered_map<string,double> computeFromStart(const Graph& g, const string& start) {
        unordered_map<string,double> val;
        val[start] = 1.0;
        deque<string> dq;
        dq.push_back(start);

        while (!dq.empty()) {
            string u = dq.front();
            dq.pop_front();
            auto it = g.find(u);
            if (it == g.end()) continue;
            for (auto &[v, w] : it->second) {
                if (!val.count(v)) {
                    val[v] = val[u] * w;
                    dq.push_back(v);
                }
            }
        }
        return val;
    }

public:
    double maxAmount(string initialCurrency, vector<vector<string>>& pairs1, vector<double>& rates1,
                     vector<vector<string>>& pairs2, vector<double>& rates2) {
        Graph g1 = buildGraph(pairs1, rates1);
        Graph g2 = buildGraph(pairs2, rates2);

        auto day1 = computeFromStart(g1, initialCurrency);           // initial -> X (day1)
        auto day2FromInit = computeFromStart(g2, initialCurrency);   // initial -> X (day2)

        double ans = 1.0;
        for (auto &kv : day1) {
            const string& cur = kv.first;
            double rateDay1 = kv.second;
            auto it = day2FromInit.find(cur);
            if (it == day2FromInit.end()) continue;
            double rateDay2InitToCur = it->second;
            // cur -> initial on day2 is inverse
            ans = max(ans, rateDay1 / rateDay2InitToCur);
        }
        return ans;
    }
};
// @lc code=end
