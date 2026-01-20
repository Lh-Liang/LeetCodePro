#include <vector>
#include <set>
#include <algorithm>

using namespace std;

#
# @lc app=leetcode id=3569 lang=cpp
#
# [3569] Maximize Count of Distinct Primes After Split
#

# @lc code=start
class SegTree {
public:
    int n;
    vector<int> tree, lazy;
    SegTree(int n) : n(n), tree(4 * n + 1, 0), lazy(4 * n + 1, 0) {}
    void push(int v) {
        if (lazy[v] != 0) {
            tree[2 * v] += lazy[v];
            lazy[2 * v] += lazy[v];
            tree[2 * v + 1] += lazy[v];
            lazy[2 * v + 1] += lazy[v];
            lazy[v] = 0;
        }
    }
    void update(int v, int tl, int tr, int l, int r, int add) {
        if (l > r) return;
        if (l == tl && r == tr) {
            tree[v] += add;
            lazy[v] += add;
        } else {
            push(v);
            int tm = (tl + tr) / 2;
            update(2 * v, tl, tm, l, min(r, tm), add);
            update(2 * v + 1, tm + 1, tr, max(l, tm + 1), r, add);
            tree[v] = max(tree[2 * v], tree[2 * v + 1]);
        }
    }
    int query() {
        return tree[1];
    }
};

class Solution {
    static const int MAXV = 100001;
    bool isPrime[MAXV];
    bool sieved = false;

    void sieve() {
        if (sieved) return;
        fill(isPrime, isPrime + MAXV, true);
        isPrime[0] = isPrime[1] = false;
        for (int p = 2; p * p < MAXV; p++) {
            if (isPrime[p]) {
                for (int i = p * p; i < MAXV; i += p)
                    isPrime[i] = false;
            }
        }
        sieved = true;
    }

    void update_prime(int p, int idx, bool adding, int n, int& total_distinct, vector<set<int>>& pos, SegTree& st) {
        if (p < 2 || !isPrime[p]) return;
        if (!pos[p].empty() && *pos[p].begin() < *pos[p].rbegin()) {
            st.update(1, 1, n - 1, *pos[p].begin() + 1, *pos[p].rbegin(), -1);
        }
        if (adding) {
            if (pos[p].empty()) total_distinct++;
            pos[p].insert(idx);
        } else {
            pos[p].erase(idx);
            if (pos[p].empty()) total_distinct--;
        }
        if (!pos[p].empty() && *pos[p].begin() < *pos[p].rbegin()) {
            st.update(1, 1, n - 1, *pos[p].begin() + 1, *pos[p].rbegin(), 1);
        }
    }

public:
    vector<int> maximumCount(vector<int>& nums, vector<vector<int>>& queries) {
        sieve();
        int n = nums.size();
        vector<set<int>> pos(MAXV);
        int total_distinct = 0;
        SegTree st(n - 1);

        for (int i = 0; i < n; i++) {
            update_prime(nums[i], i, true, n, total_distinct, pos, st);
        }

        vector<int> results;
        for (const auto& q : queries) {
            int idx = q[0], val = q[1];
            if (nums[idx] != val) {
                update_prime(nums[idx], idx, false, n, total_distinct, pos, st);
                nums[idx] = val;
                update_prime(nums[idx], idx, true, n, total_distinct, pos, st);
            }
            results.push_back(total_distinct + st.query());
        }
        return results;
    }
};
# @lc code=end