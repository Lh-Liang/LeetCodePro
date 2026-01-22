#
# @lc app=leetcode id=3525 lang=cpp
#
# [3525] Find X Value of Array II
#
# @lc code=start
class Solution {
private:
    int k;
    int n;
    vector<int> mult;
    vector<vector<int>> cnt;
    
    void pushUp(int node) {
        int left = 2 * node, right = 2 * node + 1;
        mult[node] = (mult[left] * mult[right]) % k;
        fill(cnt[node].begin(), cnt[node].end(), 0);
        for (int p = 0; p < k; p++) {
            cnt[node][p] += cnt[left][p];
            cnt[node][(mult[left] * p) % k] += cnt[right][p];
        }
    }
    
    void build(vector<int>& nums, int node, int l, int r) {
        cnt[node].resize(k, 0);
        if (l == r) {
            int v = nums[l] % k;
            mult[node] = v;
            cnt[node][v] = 1;
            return;
        }
        int mid = (l + r) / 2;
        build(nums, 2 * node, l, mid);
        build(nums, 2 * node + 1, mid + 1, r);
        pushUp(node);
    }
    
    void update(int node, int l, int r, int idx, int val) {
        if (l == r) {
            int v = val % k;
            mult[node] = v;
            fill(cnt[node].begin(), cnt[node].end(), 0);
            cnt[node][v] = 1;
            return;
        }
        int mid = (l + r) / 2;
        if (idx <= mid) {
            update(2 * node, l, mid, idx, val);
        } else {
            update(2 * node + 1, mid + 1, r, idx, val);
        }
        pushUp(node);
    }
    
    pair<int, vector<int>> query(int node, int l, int r, int ql, int qr) {
        if (qr < l || ql > r) {
            return {1, vector<int>(k, 0)};
        }
        if (ql <= l && r <= qr) {
            return {mult[node], cnt[node]};
        }
        int mid = (l + r) / 2;
        auto leftRes = query(2 * node, l, mid, ql, qr);
        auto rightRes = query(2 * node + 1, mid + 1, r, ql, qr);
        
        int lm = leftRes.first;
        int rm = rightRes.first;
        vector<int>& lc = leftRes.second;
        vector<int>& rc = rightRes.second;
        
        vector<int> c(k, 0);
        for (int p = 0; p < k; p++) {
            c[p] += lc[p];
            c[(lm * p) % k] += rc[p];
        }
        return {(lm * rm) % k, c};
    }
    
public:
    vector<int> resultArray(vector<int>& nums, int K, vector<vector<int>>& queries) {
        k = K;
        n = nums.size();
        mult.resize(4 * n);
        cnt.resize(4 * n);
        build(nums, 1, 0, n - 1);
        
        vector<int> result;
        for (auto& q : queries) {
            int idx = q[0], val = q[1], start = q[2], x = q[3];
            update(1, 0, n - 1, idx, val);
            auto res = query(1, 0, n - 1, start, n - 1);
            result.push_back(res.second[x]);
        }
        return result;
    }
};
# @lc code=end