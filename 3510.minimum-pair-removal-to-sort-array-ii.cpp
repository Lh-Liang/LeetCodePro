#include <vector>
#include <queue>

using namespace std;

struct Node {
    long long val;
    int prev, next;
    bool deleted;
};

class Solution {
public:
    int minimumPairRemoval(vector<int>& nums) {
        int n = nums.size();
        if (n <= 1) return 0;

        vector<Node> nodes(n);
        int violations = 0;

        // Helper to check if index i is the start of a non-decreasing violation
        auto is_violation = [&](int i) {
            if (i < 0 || nodes[i].deleted || nodes[i].next == -1) return 0;
            return nodes[i].val > nodes[nodes[i].next].val ? 1 : 0;
        };

        for (int i = 0; i < n; ++i) {
            nodes[i].val = nums[i];
            nodes[i].prev = i - 1;
            nodes[i].next = (i == n - 1) ? -1 : i + 1;
            nodes[i].deleted = false;
        }

        // Initial violation count
        for (int i = 0; i < n - 1; ++i) {
            if (nodes[i].val > nodes[i + 1].val) violations++;
        }

        if (violations == 0) return 0;

        // Priority queue stores {sum, leftmost_index}
        using Element = pair<long long, int>;
        priority_queue<Element, vector<Element>, greater<Element>> pq;

        for (int i = 0; i < n - 1; ++i) {
            pq.push({nodes[i].val + nodes[i + 1].val, i});
        }

        int ops = 0;
        while (violations > 0 && !pq.empty()) {
            auto [sum, i] = pq.top();
            pq.pop();

            // Validation: ensure node i and its next neighbor j still exist and form the pair
            if (nodes[i].deleted || nodes[i].next == -1) continue;
            int j = nodes[i].next;
            if (nodes[i].val + nodes[j].val != sum) continue;

            // Identify the neighborhood of effect (p -> i -> j -> nn)
            int p = nodes[i].prev;
            int nn = nodes[j].next;

            // Remove old violations from count
            violations -= is_violation(p);
            violations -= is_violation(i);
            violations -= is_violation(j);

            // Merge: sum goes into node i, node j is deleted
            nodes[i].val = sum;
            nodes[i].next = nn;
            if (nn != -1) nodes[nn].prev = i;
            nodes[j].deleted = true;

            // Add new violations to count
            violations += is_violation(p);
            violations += is_violation(i);

            ops++;

            // Add new possible pairs to PQ
            if (p != -1) pq.push({nodes[p].val + nodes[i].val, p});
            if (nn != -1) pq.push({nodes[i].val + nodes[nn].val, i});
        }

        return ops;
    }
};