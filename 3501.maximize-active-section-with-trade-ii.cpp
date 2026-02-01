#include <vector>
#include <string>
#include <algorithm>
#include <cmath>

using namespace std;

class SegmentTree {
    int n;
    vector<int> tree;
public:
    SegmentTree(const vector<int>& data) {
        n = data.size();
        if (n == 0) return;
        tree.assign(4 * n, 0);
        build(data, 1, 0, n - 1);
    }
    void build(const vector<int>& data, int node, int start, int end) {
        if (start == end) {
            tree[node] = data[start];
            return;
        }
        int mid = (start + end) / 2;
        build(data, 2 * node, start, mid);
        build(data, 2 * node + 1, mid + 1, end);
        tree[node] = max(tree[2 * node], tree[2 * node + 1]);
    }
    int query(int node, int start, int end, int l, int r) {
        if (r < start || end < l) return 0;
        if (l <= start && end <= r) return tree[node];
        int mid = (start + end) / 2;
        return max(query(2 * node, start, mid, l, r), query(2 * node + 1, mid + 1, end, l, r));
    }
};

class Solution {
public:
    vector<int> maxActiveSectionsAfterTrade(string s, vector<vector<int>>& queries) {
        int n = s.length();
        int total_ones = 0;
        for (char c : s) if (c == '1') total_ones++;

        struct Block { int start, end, len; };
        vector<Block> blocks;
        for (int i = 0; i < n; ) {
            if (s[i] == '0') {
                int start = i;
                while (i < n && s[i] == '0') i++;
                blocks.push_back({start, i - 1, i - start});
            } else i++;
        }

        if (blocks.empty()) return vector<int>(queries.size(), total_ones);

        int m = blocks.size();
        vector<int> pair_sums(m > 1 ? m - 1 : 0);
        for (int i = 0; i < m - 1; ++i) {
            pair_sums[i] = blocks[i].len + blocks[i + 1].len;
        }

        SegmentTree st(pair_sums);
        vector<int> starts;
        for (const auto& b : blocks) starts.push_back(b.start);

        vector<int> ans;
        for (const auto& q : queries) {
            int L = q[0], R = q[1];
            int i = lower_bound(starts.begin(), starts.end(), L) - starts.begin();
            if (i > 0 && blocks[i - 1].end >= L) i--;
            int j = upper_bound(starts.begin(), starts.end(), R) - starts.begin() - 1;

            if (i >= j) {
                ans.push_back(total_ones);
                continue;
            }

            int max_gain = 0;
            int len_i = min(blocks[i].len, blocks[i].end - L + 1);
            int len_j = min(blocks[j].len, R - blocks[j].start + 1);

            if (j == i + 1) {
                max_gain = len_i + len_j;
            } else {
                max_gain = max(len_i + blocks[i + 1].len, blocks[j - 1].len + len_j);
                if (j - 1 > i + 1) {
                    max_gain = max(max_gain, st.query(1, 0, pair_sums.size() - 1, i + 1, j - 2));
                }
            }
            ans.push_back(total_ones + max_gain);
        }
        return ans;
    }
};