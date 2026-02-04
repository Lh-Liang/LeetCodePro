# @lc code=start
class Solution {
public:
    vector<bool> findAnswer(vector<int>& parent, string s) {
        int n = parent.size();
        vector<vector<int>> tree(n);
        for (int i = 1; i < n; ++i) {
            tree[parent[i]].push_back(i);
        }
        
        vector<bool> answer(n, false);

        function<void(int, string&)> dfs = [&](int node, string& dfsStr) {
            for (int child : tree[node]) {
                dfs(child, dfsStr);
            }
            dfsStr += s[node];
        };

        for (int i = 0; i < n; ++i) {
            string dfsStr;
            dfs(i, dfsStr);
            string reversedDfsStr = dfsStr;
            reverse(reversedDfsStr.begin(), reversedDfsStr.end());
            answer[i] = (dfsStr == reversedDfsStr);
        }

        return answer;
    }
};
# @lc code=end