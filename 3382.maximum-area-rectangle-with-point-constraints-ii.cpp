#
# @lc app=leetcode id=3382 lang=cpp
#
# [3382] Maximum Area Rectangle With Point Constraints II
#

# @lc code=start
#include <vector>
#include <algorithm>
#include <unordered_map>

using namespace std;

class Solution {
    vector<int> tree;
    int size;

    void update(int node, int start, int end, int idx, int val) {
        if (start == end) {
            tree[node] = val;
            return;
        }
        int mid = start + (end - start) / 2;
        if (idx <= mid) update(2 * node, start, mid, idx, val);
        else update(2 * node + 1, mid + 1, end, idx, val);
        tree[node] = max(tree[2 * node], tree[2 * node + 1]);
    }

    int query(int node, int start, int end, int L, int R) {
        if (R < start || end < L) return -1;
        if (L <= start && end <= R) return tree[node];
        int mid = start + (end - start) / 2;
        return max(query(2 * node, start, mid, L, R), query(2 * node + 1, mid + 1, end, L, R));
    }

public:
    long long maxRectangleArea(vector<int>& xCoord, vector<int>& yCoord) {
        int n = xCoord.size();
        vector<pair<int, int>> points(n);
        vector<int> ys;
        for (int i = 0; i < n; ++i) {
            points[i] = {xCoord[i], yCoord[i]};
            ys.push_back(yCoord[i]);
        }
        
        sort(points.begin(), points.end());
        sort(ys.begin(), ys.end());
        ys.erase(unique(ys.begin(), ys.end()), ys.end());
        
        int m = ys.size();
        size = m;
        tree.assign(4 * m + 1, -1);

        auto get_y_idx = [&](int y) {
            return lower_bound(ys.begin(), ys.end(), y) - ys.begin();
        };

        unordered_map<long long, int> last_x_for_pair;
        long long max_area = -1;

        int i = 0;
        while (i < n) {
            int j = i;
            while (j < n && points[j].first == points[i].first) j++;

            // Step 1: Check pairs in current x-column
            for (int k = i; k < j - 1; ++k) {
                int y1 = points[k].second;
                int y2 = points[k+1].second;
                long long pair_key = ((long long)y1 << 32) | y2;

                if (last_x_for_pair.count(pair_key)) {
                    int prev_x = last_x_for_pair[pair_key];
                    int y1_idx = get_y_idx(y1);
                    int y2_idx = get_y_idx(y2);

                    // Verify no points in [prev_x, curr_x] within y-range [y1, y2]
                    if (query(1, 0, m - 1, y1_idx, y2_idx) == prev_x) {
                        long long area = (long long)(points[i].first - prev_x) * (y2 - y1);
                        if (area > max_area) max_area = area;
                    }
                }
                last_x_for_pair[pair_key] = points[i].first;
            }

            // Step 2: Update segment tree with current x for all points in this column
            for (int k = i; k < j; ++k) {
                update(1, 0, m - 1, get_y_idx(points[k].second), points[i].first);
            }

            i = j;
        }

        return max_area;
    }
};
# @lc code=end