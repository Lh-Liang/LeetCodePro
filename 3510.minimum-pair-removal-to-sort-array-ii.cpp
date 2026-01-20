#
# @lc app=leetcode id=3510 lang=cpp
#
# [3510] Minimum Pair Removal to Sort Array II
#

# @lc code=start
#include <vector>
#include <queue>
#include <tuple>

using namespace std;

class Solution {
    struct Node {
        long long val;
        int prev;
        int next;
        bool removed;
    };

public:
    int minimumPairRemoval(vector<int>& nums) {
        int n = nums.size();
        if (n <= 1) return 0;

        vector<Node> nodes(n);
        int unsorted_cnt = 0;
        
        // Priority Queue: {sum, left_idx, right_idx}
        // We use a min-heap. The default priority_queue is a max-heap, so we use 'greater'.
        // Tuple comparison is lexicographical: sum first, then left_idx, then right_idx.
        // This satisfies the condition: minimum sum, then leftmost (smallest index).
        using Element = tuple<long long, int, int>;
        priority_queue<Element, vector<Element>, greater<Element>> pq;

        for (int i = 0; i < n; ++i) {
            nodes[i].val = nums[i];
            nodes[i].prev = i - 1;
            nodes[i].next = (i == n - 1) ? -1 : i + 1;
            nodes[i].removed = false;
            
            if (i < n - 1) {
                if (nums[i] > nums[i+1]) unsorted_cnt++;
                pq.push({(long long)nums[i] + nums[i+1], i, i + 1});
            }
        }

        // If already sorted, return 0
        if (unsorted_cnt == 0) return 0;

        int ops = 0;
        while (unsorted_cnt > 0 && !pq.empty()) {
            auto [sum, u, v] = pq.top();
            pq.pop();

            // Validity check:
            // 1. Nodes must not be removed.
            // 2. Nodes must still be adjacent.
            // 3. The sum must match current values (handles stale entries where values changed but sum didn't update in heap yet)
            if (nodes[u].removed || nodes[v].removed || nodes[u].next != v) {
                continue;
            }
            if (nodes[u].val + nodes[v].val != sum) {
                continue;
            }

            // Remove contributions of current connections to unsorted_cnt before merging
            int prev = nodes[u].prev;
            int next = nodes[v].next;

            if (prev != -1 && nodes[prev].val > nodes[u].val) unsorted_cnt--;
            if (nodes[u].val > nodes[v].val) unsorted_cnt--;
            if (next != -1 && nodes[v].val > nodes[next].val) unsorted_cnt--;

            // Perform Merge: u absorbs v
            long long newVal = nodes[u].val + nodes[v].val;
            nodes[u].val = newVal;
            nodes[u].next = next;
            nodes[v].removed = true;
            if (next != -1) {
                nodes[next].prev = u;
            }

            // Add contributions of new connections to unsorted_cnt after merging
            if (prev != -1 && nodes[prev].val > nodes[u].val) unsorted_cnt++;
            if (next != -1 && nodes[u].val > nodes[next].val) unsorted_cnt++;

            // Push new potential merges to heap
            if (prev != -1) {
                pq.push({nodes[prev].val + nodes[u].val, prev, u});
            }
            if (next != -1) {
                pq.push({nodes[u].val + nodes[next].val, u, next});
            }

            ops++;
        }

        return ops;
    }
};
# @lc code=end