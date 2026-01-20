#
# @lc app=leetcode id=3569 lang=cpp
#
# [3569] Maximize Count of Distinct Primes After Split
#

# @lc code=start

// Global sieve to be computed once
const int MAX_VAL = 100005;
bool is_prime[MAX_VAL];
bool sieve_initialized = false;

void run_sieve() {
    if (sieve_initialized) return;
    fill(is_prime, is_prime + MAX_VAL, true);
    is_prime[0] = is_prime[1] = false;
    for (int p = 2; p * p < MAX_VAL; p++) {
        if (is_prime[p]) {
            for (int i = p * p; i < MAX_VAL; i += p)
                is_prime[i] = false;
        }
    }
    sieve_initialized = true;
}

class Solution {
    struct SegmentTree {
        int n;
        vector<int> tree;
        vector<int> lazy;

        SegmentTree(int size) : n(size), tree(4 * size, 0), lazy(4 * size, 0) {}

        void push(int node) {
            if (lazy[node] != 0) {
                tree[2 * node] += lazy[node];
                lazy[2 * node] += lazy[node];
                tree[2 * node + 1] += lazy[node];
                lazy[2 * node + 1] += lazy[node];
                lazy[node] = 0;
            }
        }

        void update(int node, int start, int end, int l, int r, int val) {
            if (l > end || r < start) return;
            if (l <= start && end <= r) {
                tree[node] += val;
                lazy[node] += val;
                return;
            }
            push(node);
            int mid = (start + end) / 2;
            update(2 * node, start, mid, l, r, val);
            update(2 * node + 1, mid + 1, end, l, r, val);
            tree[node] = max(tree[2 * node], tree[2 * node + 1]);
        }

        int query(int node, int start, int end, int l, int r) {
            if (l > end || r < start) return 0;
            if (l <= start && end <= r) return tree[node];
            push(node);
            int mid = (start + end) / 2;
            return max(query(2 * node, start, mid, l, r), 
                       query(2 * node + 1, mid + 1, end, l, r));
        }

        void update_range(int l, int r, int val) {
            if (l > r) return;
            update(1, 1, n, l, r, val);
        }

        int query_max(int l, int r) {
            if (l > r) return 0;
            return query(1, 1, n, l, r);
        }
    };

public:
    vector<int> maximumCount(vector<int>& nums, vector<vector<int>>& queries) {
        run_sieve();

        int n = nums.size();
        vector<set<int>> pos(MAX_VAL);
        int distinct_primes = 0;

        SegmentTree st(n - 1);

        // Initial population
        for (int i = 0; i < n; ++i) {
            int val = nums[i];
            if (is_prime[val]) {
                pos[val].insert(i);
            }
        }

        for (int v = 0; v < MAX_VAL; ++v) {
            if (!pos[v].empty()) {
                distinct_primes++;
                int first = *pos[v].begin();
                int last = *pos[v].rbegin();
                if (first < last) {
                    st.update_range(first + 1, last, 1);
                }
            }
        }

        vector<int> results;
        results.reserve(queries.size());

        for (auto& q : queries) {
            int idx = q[0];
            int new_val = q[1];
            int old_val = nums[idx];

            if (old_val != new_val) {
                // Handle removal of old_val
                if (is_prime[old_val]) {
                    int first = *pos[old_val].begin();
                    int last = *pos[old_val].rbegin();
                    if (first < last) {
                        st.update_range(first + 1, last, -1);
                    }
                    
                    pos[old_val].erase(idx);
                    
                    if (pos[old_val].empty()) {
                        distinct_primes--;
                    } else {
                        int new_first = *pos[old_val].begin();
                        int new_last = *pos[old_val].rbegin();
                        if (new_first < new_last) {
                            st.update_range(new_first + 1, new_last, 1);
                        }
                    }
                }

                // Handle addition of new_val
                if (is_prime[new_val]) {
                    if (pos[new_val].empty()) {
                        distinct_primes++;
                        pos[new_val].insert(idx);
                    } else {
                        int first = *pos[new_val].begin();
                        int last = *pos[new_val].rbegin();
                        if (first < last) {
                            st.update_range(first + 1, last, -1);
                        }
                        
                        pos[new_val].insert(idx);
                        
                        int new_first = *pos[new_val].begin();
                        int new_last = *pos[new_val].rbegin();
                        if (new_first < new_last) {
                            st.update_range(new_first + 1, new_last, 1);
                        }
                    }
                }
                nums[idx] = new_val;
            }

            if (distinct_primes == 0) {
                results.push_back(0);
            } else {
                results.push_back(distinct_primes + st.query_max(1, n - 1));
            }
        }

        return results;
    }
};
# @lc code=end