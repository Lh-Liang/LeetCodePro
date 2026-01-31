#
# @lc app=leetcode id=3721 lang=cpp
#
# [3721] Longest Balanced Subarray II
#
# @lc code=start
#include <vector>
#include <algorithm>

using namespace std;

class SegmentTree {
    struct Node {
        int sum;
        int min_sum;
        int max_sum;
    };
    int n;
    vector<Node> tree;

public:
    SegmentTree(int n) : n(n), tree(4 * (n + 1), {0, 0, 0}) {}

    void update(int idx, int val, int node, int start, int end) {
        if (start == end) {
            tree[node] = {val, min(0, val), max(0, val)};
            return;
        }
        int mid = start + (end - start) / 2;
        if (idx <= mid) update(idx, val, 2 * node, start, mid);
        else update(idx, val, 2 * node + 1, mid + 1, end);
        
        tree[node].sum = tree[2 * node].sum + tree[2 * node + 1].sum;
        tree[node].min_sum = min(tree[2 * node].min_sum, tree[2 * node].sum + tree[2 * node + 1].min_sum);
        tree[node].max_sum = max(tree[2 * node].max_sum, tree[2 * node].sum + tree[2 * node + 1].max_sum);
    }

    int find_first(int target, int current_sum, int node, int start, int end) {
        if (target < current_sum + tree[node].min_sum || target > current_sum + tree[node].max_sum) {
            return -1;
        }
        if (start == end) {
            return start;
        }
        
        int mid = start + (end - start) / 2;
        int res = find_first(target, current_sum, 2 * node, start, mid);
        if (res != -1) return res;
        return find_first(target, current_sum + tree[2 * node].sum, 2 * node + 1, mid + 1, end);
    }

    int get_total_sum() { return tree[1].sum; }
};

class Solution {
public:
    int longestBalanced(vector<int>& nums) {
        int n = nums.size();
        SegmentTree st(n);
        // Problem constraints: 1 <= nums[i] <= 10^5
        vector<int> last_pos_in_tree(100001, -1);
        
        int ans = 0;
        // Index 0 in segment tree represents the prefix sum before any elements (S_{-1} = 0)
        st.update(0, 0, 1, 0, n);

        for (int j = 0; j < n; ++j) {
            int val = nums[j];
            int weight = (val % 2 == 0) ? 1 : -1;
            
            if (last_pos_in_tree[val] != -1) {
                st.update(last_pos_in_tree[val], 0, 1, 0, n);
            }
            
            int tree_idx = j + 1;
            st.update(tree_idx, weight, 1, 0, n);
            last_pos_in_tree[val] = tree_idx;
            
            int total = st.get_total_sum();
            int first_idx = st.find_first(total, 0, 1, 0, n);
            
            if (first_idx != -1) {
                ans = max(ans, (j + 1) - first_idx);
            }
        }
        
        return ans;
    }
};
# @lc code=end