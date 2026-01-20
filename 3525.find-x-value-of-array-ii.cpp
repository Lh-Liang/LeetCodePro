#
# @lc app=leetcode id=3525 lang=cpp
#
# [3525] Find X Value of Array II
#

# @lc code=start
#include <vector>

using namespace std;

struct Node {
    int cnt[5];
    int total_prod;

    Node() {
        for (int i = 0; i < 5; ++i) cnt[i] = 0;
        total_prod = 1;
    }
};

class Solution {
    vector<Node> tree;
    int n;

    Node merge(const Node& L, const Node& R, int k) {
        Node res;
        res.total_prod = (L.total_prod * R.total_prod) % k;
        for (int i = 0; i < k; ++i) {
            res.cnt[i] = L.cnt[i];
        }
        for (int i = 0; i < k; ++i) {
            if (R.cnt[i] > 0) {
                int p = (L.total_prod * i) % k;
                res.cnt[p] += R.cnt[i];
            }
        }
        return res;
    }

    void build(int node, int start, int end, const vector<int>& nums, int k) {
        if (start == end) {
            int v = nums[start] % k;
            tree[node].total_prod = v;
            for (int i = 0; i < 5; ++i) tree[node].cnt[i] = 0;
            tree[node].cnt[v] = 1;
            return;
        }
        int mid = (start + end) / 2;
        build(2 * node, start, mid, nums, k);
        build(2 * node + 1, mid + 1, end, nums, k);
        tree[node] = merge(tree[2 * node], tree[2 * node + 1], k);
    }

    void update(int node, int start, int end, int idx, int val, int k) {
        if (start == end) {
            int v = val % k;
            tree[node].total_prod = v;
            for (int i = 0; i < 5; ++i) tree[node].cnt[i] = 0;
            tree[node].cnt[v] = 1;
            return;
        }
        int mid = (start + end) / 2;
        if (idx <= mid) update(2 * node, start, mid, idx, val, k);
        else update(2 * node + 1, mid + 1, end, idx, val, k);
        tree[node] = merge(tree[2 * node], tree[2 * node + 1], k);
    }

    Node query(int node, int start, int end, int L, int R, int k) {
        if (L <= start && end <= R) {
            return tree[node];
        }
        int mid = (start + end) / 2;
        if (R <= mid) return query(2 * node, start, mid, L, R, k);
        if (L > mid) return query(2 * node + 1, mid + 1, end, L, R, k);
        Node leftRes = query(2 * node, start, mid, L, R, k);
        Node rightRes = query(2 * node + 1, mid + 1, end, L, R, k);
        return merge(leftRes, rightRes, k);
    }

public:
    vector<int> resultArray(vector<int>& nums, int k, vector<vector<int>>& queries) {
        n = nums.size();
        tree.assign(4 * n + 1, Node());
        build(1, 0, n - 1, nums, k);

        vector<int> results;
        for (const auto& q : queries) {
            int idx = q[0], val = q[1], start = q[2], x = q[3];
            update(1, 0, n - 1, idx, val, k);
            Node res = query(1, 0, n - 1, start, n - 1, k);
            if (x >= 0 && x < k) results.push_back(res.cnt[x]);
            else results.push_back(0);
        }
        return results;
    }
};
# @lc code=end