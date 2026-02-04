class Solution {
public:
    vector<bool> findAnswer(vector<int>& parent, string s) {
        int n = parent.size();
        vector<vector<int>> tree(n);
        for (int i = 1; i < n; ++i) {
            tree[parent[i]].push_back(i);
        }
        for (int i = 0; i < n; ++i) {
            sort(tree[i].begin(), tree[i].end());
        }
        vector<bool> answer(n);
        function<void(int, string&)> dfs = [&](int node, string& dfsStr) {
            for (int child : tree[node]) {
                dfs(child, dfsStr);
            }
            dfsStr.push_back(s[node]);
        };
        for (int i = 0; i < n; ++i) {
            string dfsStr;
            dfs(i, dfsStr);
            int l = 0, r = dfsStr.size() - 1;
            bool isPalindrome = true;
            while (l < r) {
                if (dfsStr[l] != dfsStr[r]) {
                    isPalindrome = false;
                    break;
                }
                ++l; --r;
            }
            answer[i] = isPalindrome;
        }
        return answer;
    }
};