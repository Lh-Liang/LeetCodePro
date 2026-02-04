#
# @lc app=leetcode id=3510 lang=cpp
#
# [3510] Minimum Pair Removal to Sort Array II
#
# @lc code=start
#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    int minimumPairRemoval(vector<int>& nums) {
        int n = nums.size();
        if (n <= 1) return 0;
        bool sorted = true;
        for (int i = 1; i < n; ++i)
            if (nums[i] < nums[i-1]) { sorted = false; break; }
        if (sorted) return 0;
        // Doubly linked list simulation
        struct Node {
            int val;
            int prev, next;
            bool removed;
        };
        vector<Node> arr(n);
        for (int i = 0; i < n; ++i) {
            arr[i] = { nums[i], i-1, i+1, false };
        }
        // Min-heap: (sum, left index, timestamp)
        typedef tuple<long long, int, int> T;
        priority_queue<T, vector<T>, greater<T>> pq;
        int timestamp = 0;
        vector<int> time_idx(n-1, 0);
        for (int i = 0; i < n-1; ++i) {
            pq.emplace((long long)arr[i].val + arr[i+1].val, i, timestamp++);
            time_idx[i] = timestamp-1;
        }
        int ops = 0;
        int remain = n;
        while (remain > 1) {
            // Find leftmost valid min pair
            while (!pq.empty()) {
                auto [sum, i, t] = pq.top();
                pq.pop();
                if (arr[i].removed || arr[i+1].removed) continue;
                // Merge arr[i] and arr[i+1]
                arr[i].val += arr[arr[i].next].val;
                int r = arr[i].next;
                arr[i].next = arr[r].next;
                if (arr[r].next < n) arr[arr[r].next].prev = i;
                arr[r].removed = true;
                ++ops; --remain;
                // Update heap: if arr[i].prev exists
                if (arr[i].prev >= 0 && !arr[arr[i].prev].removed)
                    pq.emplace((long long)arr[arr[i].prev].val + arr[i].val, arr[i].prev, timestamp++);
                // Update heap: if arr[i].next exists and not removed
                if (arr[i].next < n && !arr[arr[i].next].removed)
                    pq.emplace((long long)arr[i].val + arr[arr[i].next].val, i, timestamp++);
                break;
            }
            // After each merge, check if array is non-decreasing
            int last = -1;
            bool ok = true;
            for (int i = 0; i < n; ++i) {
                if (!arr[i].removed) {
                    if (last != -1 && arr[i].val < arr[last].val) { ok = false; break; }
                    last = i;
                }
            }
            if (ok) break;
        }
        return ops;
    }
};
# @lc code=end