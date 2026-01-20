#
# @lc app=leetcode id=3721 lang=cpp
#
# [3721] Longest Balanced Subarray II
#

# @lc code=start
#include <vector>
#include <algorithm>

using namespace std;

struct Node {
    int min_val;
    int max_val;
};

class Solution {
    vector<Node> tree;
    vector<int> lazy;
    int n;

    void push(int v) {
        if (lazy[v] != 0) {
            tree[2 * v].min_val += lazy[v];
            tree[2 * v].max_val += lazy[v];
            lazy[2 * v] += lazy[v];
            tree[2 * v + 1].min_val += lazy[v];
            tree[2 * v + 1].max_val += lazy[v];
            lazy[2 * v + 1] += lazy[v];
            lazy[v] = 0;
        }
    }

    void update(int v, int tl, int tr, int l, int r, int add) {
        if (l > r) return;
        if (l == tl && r == tr) {
            tree[v].min_val += add;
            tree[v].max_val += add;
            lazy[v] += add;
        } else {
            push(v);
            int tm = (tl + tr) / 2;
            update(2 * v, tl, tm, l, min(r, tm), add);
            update(2 * v + 1, tm + 1, tr, max(l, tm + 1), r, add);
            tree[v].min_val = min(tree[2 * v].min_val, tree[2 * v + 1].min_val);
            tree[v].max_val = max(tree[2 * v].max_val, tree[2 * v + 1].max_val);
        }
    }

    int find_leftmost(int v, int tl, int tr, int l, int r, int target) {
        if (l > r || tree[v].min_val > target || tree[v].max_val < target) {
            return -1;
        }
        if (tl == tr) {
            return tl;
        }
        push(v);
        int tm = (tl + tr) / 2;
        int res = find_leftmost(2 * v, tl, tm, l, min(r, tm), target);
        if (res == -1) {
            res = find_leftmost(2 * v + 1, tm + 1, tr, max(l, tm + 1), r, target);
        }
        return res;
    }

public:
    int longestBalanced(vector<int>& nums) {
        n = nums.size();
        tree.assign(4 * n, {0, 0});
        lazy.assign(4 * n, 0);
        
        vector<int> prev_pos(100001, -1);
        int max_len = 0;

        for (int j = 0; j < n; ++j) {
            int val = nums[j];
            int p = prev_pos[val];
            int delta = (val % 2 == 0) ? 1 : -1;
            
            update(1, 0, n - 1, p + 1, j, delta);
            
            int i = find_leftmost(1, 0, n - 1, 0, j, 0);
            if (i != -1) {
                max_len = max(max_len, j - i + 1);
            }
            
            prev_pos[val] = j;
        }

        return max_len;
    }
};
# @lc code=end