#
# @lc app=leetcode id=3569 lang=cpp
#
# [3569] Maximize Count of Distinct Primes After Split
#
# @lc code=start
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

class SegmentTree {
    int n;
    vector<int> tree;
    vector<int> lazy;

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

public:
    SegmentTree(int n) : n(n) {
        if (n > 0) {
            tree.assign(4 * n + 1, 0);
            lazy.assign(4 * n + 1, 0);
        }
    }

    void update(int l, int r, int add) {
        if (n <= 0 || l > r) return;
        update(1, 1, n, l, r, add);
    }

    int query_max() {
        if (n <= 0) return 0;
        return tree[1];
    }
};

class Solution {
    static bool is_prime[100001];
    static bool sieved;
    void sieve() {
        if (sieved) return;
        fill(is_prime, is_prime + 100001, true);
        is_prime[0] = is_prime[1] = false;
        for (int p = 2; p * p <= 100000; p++) {
            if (is_prime[p]) {
                for (int i = p * p; i <= 100000; i += p)
                    is_prime[i] = false;
            }
        }
        sieved = true;
    }

public:
    vector<int> maximumCount(vector<int>& nums, vector<vector<int>>& queries) {
        sieve();
        int n = nums.size();
        vector<set<int>> pos(100001);
        int current_S = 0;
        SegmentTree st(n - 1);

        auto update_prime_range = [&](int v, int delta) {
            if (pos[v].size() < 2) return;
            int f = *pos[v].begin();
            int l = *pos[v].rbegin();
            st.update(f + 1, l, delta);
        };

        for (int i = 0; i < n; i++) {
            if (is_prime[nums[i]]) {
                if (pos[nums[i]].empty()) current_S++;
                pos[nums[i]].insert(i);
            }
        }

        for (int i = 2; i <= 100000; i++) {
            if (is_prime[i]) update_prime_range(i, 1);
        }

        vector<int> results;
        for (const auto& q : queries) {
            int idx = q[0], val = q[1];
            if (nums[idx] == val) {
                results.push_back(current_S + st.query_max());
                continue;
            }

            if (is_prime[nums[idx]]) {
                update_prime_range(nums[idx], -1);
                pos[nums[idx]].erase(idx);
                if (pos[nums[idx]].empty()) current_S--;
                else update_prime_range(nums[idx], 1);
            }

            nums[idx] = val;

            if (is_prime[nums[idx]]) {
                if (pos[nums[idx]].empty()) current_S++;
                else update_prime_range(nums[idx], -1);
                pos[nums[idx]].insert(idx);
                update_prime_range(nums[idx], 1);
            }
            results.push_back(current_S + st.query_max());
        }

        return results;
    }
};

bool Solution::is_prime[100001];
bool Solution::sieved = false;
# @lc code=end