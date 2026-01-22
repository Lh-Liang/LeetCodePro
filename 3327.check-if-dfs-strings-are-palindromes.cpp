#
# @lc app=leetcode id=3327 lang=cpp
#
# [3327] Check if DFS Strings Are Palindromes
#

# @lc code=start
class Solution {
public:
    vector<bool> findAnswer(vector<int>& parent, string s) {
        const int MOD = 1000000007;
        const int BASE = 131;
        int n = parent.size();
        
        // Build adjacency list
        vector<vector<int>> children(n);
        for (int i = 1; i < n; ++i)
            children[parent[i]].push_back(i);
        
        // Sort each child list by node number
        for (int i = 0; i < n; ++i)
            sort(children[i].begin(), children[i].end());
        
        // Precompute powers of BASE
        vector<long long> power(n+1);
        power[0] = 1;
        for (int i = 1; i <= n; ++i)
            power[i] = power[i-1] * BASE % MOD;
        
        vector<int> sz(n);          // Subtree size
        vector<long long> FH(n);    // Forward hash
        vector<long long> RH(n);    // Reverse hash
        
        stack<int> st;
        st.push(0);
        vector<int> idx(n, 0);      // Next child index
        
        while (!st.empty()) {
            int u = st.top();
            
            // If still unprocessed children
            if (idx[u] < static_cast<int>(children[u].size())) {
                int v = children[u][idx[u]++];
                st.push(v);
                continue;
            }
            
            // All children processed → compute values
            long long cumulFH = 0;
            int totLenChilds = 0;
            
            // Forward pass over sorted children
            for (int v : children[u]) {
                cumulFH = (cumulFH + FH[v] * power[totLenChilds]) % MOD;
                totLenChilds += sz[v];
            }
            
            int charVal = s[u] - 'a' + 1;
            sz[u] = totLenChilds + 1;
            FH[u] = (cumulFH + charVal * power[totLenChilds]) % MOD;
            
            // Reverse pass over sorted children
            long long cumulRH = 0;
            totLenChilds = 0;
            
            auto &childList = children[u];
            auto rit = childList.rbegin();
            auto rend = childList.rend();
            
            while (rit != rend) {
                int v = *rit;
                cumulRH = (cumulRH + RH[v] * power[totLenChilds]) % MOD;
                totLenChilds += sz[v];
                ++rit;
            }
            
            RH[u] = (charVal + cumulRH * BASE) % MOD;
            
            st.pop();
        }
        
        vector<bool> ans(n);
        for (int i = 0; i < n; ++i)
            ans[i] = FH[i] == RH[i];
        
        return ans;
    }
};
# @lc code=end