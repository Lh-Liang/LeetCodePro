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
    bool is_null;

    Node() {
        for (int i = 0; i < 5; ++i) cnt[i] = 0;
        total_prod = 1;
        is_null = true;
    }

    void set(int val, int k) {
        for (int i = 0; i < 5; ++i) cnt[i] = 0;
        total_prod = val % k;
        cnt[total_prod] = 1;
        is_null = false;
    }
};

Node merge(const Node& left, const Node& right, int k) {
    if (left.is_null) return right;
    if (right.is_null) return left;

    Node res;
    res.is_null = false;
    res.total_prod = (left.total_prod * right.total_prod) % k;
    for (int i = 0; i < k; ++i) {
        res.cnt[i] = left.cnt[i];
    }
    for (int i = 0; i < k; ++i) {
        if (right.cnt[i] > 0) {
            int target = (left.total_prod * i) % k;
            res.cnt[target] += right.cnt[i];
        }
    }
    return res;
}

class SegmentTree {
    int n, k;
    vector<Node> tree;

public:
    SegmentTree(const vector<int>& nums, int _k) : n(nums.size()), k(_k) {
        tree.resize(4 * n);
        build(nums, 1, 0, n - 1);
    }

    void build(const vector<int>& nums, int node, int start, int end) {
        if (start == end) {
            tree[node].set(nums[start], k);
            return;
        }
        int mid = (start + end) / 2;
        build(nums, 2 * node, start, mid);
        build(nums, 2 * node + 1, mid + 1, end);
        tree[node] = merge(tree[2 * node], tree[2 * node + 1], k);
    }

    void update(int node, int start, int end, int idx, int val) {
        if (start == end) {
            tree[node].set(val, k);
            return;
        }
        int mid = (start + end) / 2;
        if (idx <= mid) update(2 * node, start, mid, idx, val);
        else update(2 * node + 1, mid + 1, end, idx, val);
        tree[node] = merge(tree[2 * node], tree[2 * node + 1], k);
    }

    Node query(int node, int start, int end, int l, int r) {
        if (r < start || end < l) return Node();
        if (l <= start && end <= r) return tree[node];
        int mid = (start + end) / 2;
        Node left = query(2 * node, start, mid, l, r);
        Node right = query(2 * node + 1, mid + 1, end, l, r);
        return merge(left, right, k);
    }

    int get_ans(int starti, int xi) {
        Node res = query(1, 0, n - 1, starti, n - 1);
        return res.cnt[xi];
    }

    void update_val(int idx, int val) {
        update(1, 0, n - 1, idx, val);
    }
};

class Solution {
public:
    vector<int> resultArray(vector<int>& nums, int k, vector<vector<int>>& queries) {
        int n = nums.size();
        int q = queries.size();
        SegmentTree st(nums, k);
        vector<int> results;
        results.reserve(q);

        for (int i = 0; i < q; ++i) {
            int idx = queries[i][0];
            int val = queries[i][1];
            int start = queries[i][2];
            int target_x = queries[i][3];

            st.update_val(idx, val);
            results.push_back(st.get_ans(start, target_x));
        }

        return results;
    }
};
# @lc code=end