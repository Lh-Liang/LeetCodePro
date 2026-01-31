#
# @lc app=leetcode id=3762 lang=cpp
#
# [3762] Minimum Operations to Equalize Subarrays
#

# @lc code=start
#include <vector>
#include <algorithm>
#include <utility>

using namespace std;

class Solution {
    struct Node {
        int count;
        long long sum;
        int left, right;
    };
    vector<Node> tree;
    vector<int> roots;
    vector<int> sorted_vals;

    int build(int l, int r) {
        int node_idx = tree.size();
        tree.push_back({0, 0, -1, -1});
        if (l < r) {
            int mid = l + (r - l) / 2;
            int L = build(l, mid);
            int R = build(mid + 1, r);
            tree[node_idx].left = L;
            tree[node_idx].right = R;
        }
        return node_idx;
    }

    int update(int prev_idx, int l, int r, int val_idx, int val) {
        int node_idx = tree.size();
        tree.push_back(tree[prev_idx]);
        tree[node_idx].count++;
        tree[node_idx].sum += val;
        if (l < r) {
            int mid = l + (r - l) / 2;
            if (val_idx <= mid) {
                int L = update(tree[prev_idx].left, l, mid, val_idx, val);
                tree[node_idx].left = L;
            } else {
                int R = update(tree[prev_idx].right, mid + 1, r, val_idx, val);
                tree[node_idx].right = R;
            }
        }
        return node_idx;
    }

    pair<int, long long> query(int node_l, int node_r, int l, int r, int ql, int qr) {
        if (ql > qr || l > qr || r < ql) return {0, 0};
        if (l >= ql && r <= qr) {
            return {tree[node_r].count - tree[node_l].count, tree[node_r].sum - tree[node_l].sum};
        }
        int mid = l + (r - l) / 2;
        auto left_res = query(tree[node_l].left, tree[node_r].left, l, mid, ql, qr);
        auto right_res = query(tree[node_l].right, tree[node_r].right, mid + 1, r, ql, qr);
        return {left_res.first + right_res.first, left_res.second + right_res.second};
    }

    int find_kth(int node_l, int node_r, int l, int r, int rank) {
        if (l == r) return l;
        int mid = l + (r - l) / 2;
        int left_count = tree[tree[node_r].left].count - tree[tree[node_l].left].count;
        if (rank <= left_count)
            return find_kth(tree[node_l].left, tree[node_r].left, l, mid, rank);
        else
            return find_kth(tree[node_l].right, tree[node_r].right, mid + 1, r, rank - left_count);
    }

public:
    vector<long long> minOperations(vector<int>& nums, int k, vector<vector<int>>& queries) {
        int n = nums.size();
        tree.clear();
        roots.clear();
        sorted_vals.clear();

        vector<int> rem_diff(n, 0);
        for (int i = 1; i < n; ++i) {
            rem_diff[i] = rem_diff[i - 1] + (nums[i] % k != nums[i - 1] % k);
        }

        vector<int> y(n);
        for (int i = 0; i < n; ++i) y[i] = nums[i] / k;
        sorted_vals = y;
        sort(sorted_vals.begin(), sorted_vals.end());
        sorted_vals.erase(unique(sorted_vals.begin(), sorted_vals.end()), sorted_vals.end());
        int m = sorted_vals.size();

        tree.reserve(n * 40);
        roots.push_back(build(0, m - 1));
        for (int i = 0; i < n; ++i) {
            int idx = lower_bound(sorted_vals.begin(), sorted_vals.end(), y[i]) - sorted_vals.begin();
            roots.push_back(update(roots.back(), 0, m - 1, idx, y[i]));
        }

        vector<long long> ans;
        ans.reserve(queries.size());
        for (const auto& q : queries) {
            int l = q[0], r = q[1];
            if (rem_diff[r] - rem_diff[l] != 0) {
                ans.push_back(-1);
                continue;
            }
            int len = r - l + 1;
            int m_idx = find_kth(roots[l], roots[r + 1], 0, m - 1, (len + 1) / 2);
            long long median = sorted_vals[m_idx];

            auto left_part = query(roots[l], roots[r + 1], 0, m - 1, 0, m_idx);
            auto right_part = query(roots[l], roots[r + 1], 0, m - 1, m_idx + 1, m - 1);

            long long ops = (long long)left_part.first * median - left_part.second;
            ops += right_part.second - (long long)right_part.first * median;
            ans.push_back(ops);
        }
        return ans;
    }
};
# @lc code=end