#
# @lc app=leetcode id=3721 lang=cpp
#
# [3721] Longest Balanced Subarray II
#

# @lc code=start
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

class SegmentTree {
    int n;
    vector<int> min_val;
    vector<int> max_val;
    vector<int> lazy;

public:
    SegmentTree(int size) {
        n = size;
        min_val.resize(4 * n, 0);
        max_val.resize(4 * n, 0);
        lazy.resize(4 * n, 0);
    }

    void push(int node) {
        if (lazy[node] != 0) {
            lazy[2 * node] += lazy[node];
            min_val[2 * node] += lazy[node];
            max_val[2 * node] += lazy[node];

            lazy[2 * node + 1] += lazy[node];
            min_val[2 * node + 1] += lazy[node];
            max_val[2 * node + 1] += lazy[node];

            lazy[node] = 0;
        }
    }

    void update(int node, int start, int end, int l, int r, int val) {
        if (l > end || r < start) return;
        if (l <= start && end <= r) {
            lazy[node] += val;
            min_val[node] += val;
            max_val[node] += val;
            return;
        }
        push(node);
        int mid = (start + end) / 2;
        update(2 * node, start, mid, l, r, val);
        update(2 * node + 1, mid + 1, end, l, r, val);
        min_val[node] = min(min_val[2 * node], min_val[2 * node + 1]);
        max_val[node] = max(max_val[2 * node], max_val[2 * node + 1]);
    }

    // Find the leftmost index in [qL, qR] that has value 0
    int findFirstZero(int node, int start, int end, int qL, int qR) {
        if (start > qR || end < qL) return -1;
        
        // Optimization: if 0 is not in the range of values for this node, return -1
        if (min_val[node] > 0 || max_val[node] < 0) return -1;

        if (start == end) {
            return (min_val[node] == 0) ? start : -1;
        }

        push(node);
        int mid = (start + end) / 2;
        int res = findFirstZero(2 * node, start, mid, qL, qR);
        if (res != -1) return res;
        return findFirstZero(2 * node + 1, mid + 1, end, qL, qR);
    }

    void updateRange(int l, int r, int val) {
        if (l > r) return;
        update(1, 0, n - 1, l, r, val);
    }

    int queryLeftmostZero(int l, int r) {
        if (l > r) return -1;
        return findFirstZero(1, 0, n - 1, l, r);
    }
};

class Solution {
public:
    int longestBalanced(vector<int>& nums) {
        int n = nums.size();
        // The segment tree covers indices 0 to n. 
        // Index i in segment tree corresponds to subarrays starting at i.
        // We need size n + 1 because we conceptually might query up to n (though loop goes to n-1, range updates use arrays).
        // Actually, for a current ending j, valid start indices are 0..j.
        // So size n is sufficient for indices 0..n-1.
        // BUT, we need to handle the update logic carefully.
        
        SegmentTree st(n);
        vector<int> last_pos(100005, -1);
        int max_len = 0;

        for (int j = 0; j < n; ++j) {
            int val = nums[j];
            int prev = last_pos[val];
            
            // Determine if we add 1 or subtract 1
            int delta = (val % 2 != 0) ? -1 : 1;
            
            // Update range (prev + 1, j)
            st.updateRange(prev + 1, j, delta);
            
            // Find the smallest index k in [0, j] such that value is 0
            int k = st.queryLeftmostZero(0, j);
            
            if (k != -1) {
                max_len = max(max_len, j - k + 1);
            }
            
            last_pos[val] = j;
        }

        return max_len;
    }
};
# @lc code=end