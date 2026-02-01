#include <vector>
#include <algorithm>
#include <unordered_map>

using namespace std;

class Solution {
public:
    long long maxRectangleArea(vector<int>& xCoord, vector<int>& yCoord) {
        int n = xCoord.size();
        if (n < 4) return -1;

        // Coordinate compression for y
        vector<int> ys = yCoord;
        sort(ys.begin(), ys.end());
        ys.erase(unique(ys.begin(), ys.end()), ys.end());
        int m = ys.size();

        // Sort points by x, then by y index
        vector<pair<int, int>> points(n);
        for (int i = 0; i < n; ++i) {
            points[i] = {xCoord[i], (int)(lower_bound(ys.begin(), ys.end(), yCoord[i]) - ys.begin())};
        }
        sort(points.begin(), points.end());

        // Iterative Segment Tree for range max query
        vector<int> tree(2 * m, -1);
        auto update = [&](int i, int val) {
            for (tree[i += m] = val; i > 1; i >>= 1)
                tree[i >> 1] = max(tree[i], tree[i ^ 1]);
        };
        auto query = [&](int l, int r) {
            int res = -1;
            for (l += m, r += m + 1; l < r; l >>= 1, r >>= 1) {
                if (l & 1) res = max(res, tree[l++]);
                if (r & 1) res = max(res, tree[--r]);
            }
            return res;
        };

        // last_x stores the last x-coordinate where the pair (y1_idx, y2_idx) was adjacent
        unordered_map<long long, int> last_x;
        last_x.reserve(n);
        long long max_area = -1;

        for (int i = 0; i < n; ) {
            int j = i;
            while (j < n && points[j].first == points[i].first) j++;

            // 1. Check for rectangles using this column as the right side
            for (int k = i; k < j - 1; ++k) {
                int y1_idx = points[k].second;
                int y2_idx = points[k + 1].second;
                long long key = ((long long)y1_idx << 32) | y2_idx;
                
                auto it = last_x.find(key);
                if (it != last_x.end()) {
                    int lx = it->second;
                    // Verify no points are inside or on the boundary between lx and current x
                    if (query(y1_idx, y2_idx) == lx) {
                        long long area = (long long)(points[i].first - lx) * (ys[y2_idx] - ys[y1_idx]);
                        if (max_area == -1 || area > max_area) {
                            max_area = area;
                        }
                    }
                }
            }

            // 2. Update Segment Tree with points in the current column
            for (int k = i; k < j; ++k) {
                update(points[k].second, points[i].first);
            }

            // 3. Update last_x with adjacent pairs in the current column
            for (int k = i; k < j - 1; ++k) {
                long long key = ((long long)points[k].second << 32) | points[k + 1].second;
                last_x[key] = points[i].first;
            }

            i = j;
        }

        return max_area;
    }
};