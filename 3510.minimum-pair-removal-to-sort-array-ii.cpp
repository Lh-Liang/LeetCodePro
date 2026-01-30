#
# @lc app=leetcode id=3510 lang=cpp
#
# [3510] Minimum Pair Removal to Sort Array II
#
# @lc code=start
#include <vector>
#include <queue>

using namespace std;

struct Node {
    long long val;
    int pos;
    int prev = -1;
    int next = -1;
    bool deleted = false;
};

struct Pair {
    long long sum;
    int pos;
    int L_idx, R_idx;

    bool operator>(const Pair& other) const {
        if (sum != other.sum) return sum > other.sum;
        return pos > other.pos;
    }
};

class Solution {
public:
    int minimumPairRemoval(vector<int>& nums) {
        int n = nums.size();
        if (n <= 1) return 0;

        vector<Node> nodes(n);
        for (int i = 0; i < n; ++i) {
            nodes[i].val = nums[i];
            nodes[i].pos = i;
            if (i > 0) nodes[i].prev = i - 1;
            if (i < n - 1) nodes[i].next = i + 1;
        }

        int bad_count = 0;
        auto isBad = [&](int i, int j) {
            if (i == -1 || j == -1) return false;
            return nodes[i].val > nodes[j].val;
        };

        priority_queue<Pair, vector<Pair>, greater<Pair>> pq;
        for (int i = 0; i < n - 1; ++i) {
            if (isBad(i, i + 1)) bad_count++;
            pq.push({nodes[i].val + nodes[i + 1].val, nodes[i].pos, i, i + 1});
        }

        int ops = 0;
        while (bad_count > 0 && !pq.empty()) {
            Pair top = pq.top();
            pq.pop();

            int L = top.L_idx;
            int R = top.R_idx;

            // Validation: ensure nodes aren't deleted and are still adjacent
            if (nodes[L].deleted || nodes[R].deleted || nodes[L].next != R || (nodes[L].val + nodes[R].val) != top.sum) {
                continue;
            }

            ops++;
            int P = nodes[L].prev;
            int N = nodes[R].next;

            // Remove old 'bad' contributions
            if (isBad(P, L)) bad_count--;
            if (isBad(L, R)) bad_count--;
            if (isBad(R, N)) bad_count--;

            // Perform merge into L
            nodes[L].val += nodes[R].val;
            nodes[L].next = N;
            if (N != -1) nodes[N].prev = L;
            nodes[R].deleted = true;

            // Add new 'bad' contributions
            if (isBad(P, L)) bad_count++;
            if (isBad(L, N)) bad_count++;

            // Push new potential pairs
            if (P != -1) pq.push({nodes[P].val + nodes[L].val, nodes[P].pos, P, L});
            if (N != -1) pq.push({nodes[L].val + nodes[N].val, nodes[L].pos, L, N});
        }

        return ops;
    }
};
# @lc code=end