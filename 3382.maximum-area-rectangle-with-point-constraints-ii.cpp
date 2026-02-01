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

// Iterative Segment Tree for range maximum query
class SegmentTree {
    int n;
    vector<int> tree;
public:
    SegmentTree(int n) : n(n), tree(2 * n, -1) {}
    
    void update(int i, int val) {
        for (tree[i += n] = val; i > 1; i >>= 1)
            tree[i >> 1] = max(tree[i], tree[i ^ 1]);
    }
    
    int query(int l, int r) { // range [l, r] inclusive
        int res = -1;
        for (l += n, r += n + 1; l < r; l >>= 1, r >>= 1) {
            if (l & 1) res = max(res, tree[l++]);
            if (r & 1) res = max(res, tree[--r]);
        }
        return res;
    }
};

struct Point {
    int x, y, y_idx;
};

class Solution {
public:
    long long maxRectangleArea(vector<int>& xCoord, vector<int>& yCoord) {
        int n = xCoord.size();
        if (n < 4) return -1;
        
        // Coordinate compression for y-coordinates
        vector<int> ys = yCoord;
        sort(ys.begin(), ys.end());
        ys.erase(unique(ys.begin(), ys.end()), ys.end());
        int m = ys.size();

        vector<Point> points(n);
        for (int i = 0; i < n; ++i) {
            points[i].x = xCoord[i];
            points[i].y = yCoord[i];
            points[i].y_idx = (int)(lower_bound(ys.begin(), ys.end(), yCoord[i]) - ys.begin());
        }

        // Sort points by x then y
        sort(points.begin(), points.end(), [](const Point& a, const Point& b) {
            if (a.x != b.x) return a.x < b.x;
            return a.y < b.y;
        });

        SegmentTree st(m);
        unordered_map<long long, int> lastX;
        lastX.reserve(n);
        long long maxArea = -1;

        for (int i = 0; i < n; ) {
            int j = i;
            while (j < n && points[j].x == points[i].x) j++;

            // Process all adjacent pairs in current x-column
            for (int k = i; k < j - 1; ++k) {
                int y1_idx = points[k].y_idx;
                int y2_idx = points[k + 1].y_idx;
                
                // Unique key for the pair of y-indices
                long long key = 1LL * y1_idx * m + y2_idx;
                auto it = lastX.find(key);
                if (it != lastX.end()) {
                    int lx = it->second;
                    // If max x in [y1, y2] range is lx, no points are inside or on border
                    if (st.query(y1_idx, y2_idx) == lx) {
                        long long area = 1LL * (points[i].x - lx) * (points[k + 1].y - points[k].y);
                        if (area > maxArea) maxArea = area;
                    }
                }
            }

            // Update segment tree with current x for each point in this column
            for (int k = i; k < j; ++k) {
                st.update(points[k].y_idx, points[i].x);
            }

            // Record current x for the adjacent pairs to be used in future columns
            for (int k = i; k < j - 1; ++k) {
                long long key = 1LL * points[k].y_idx * m + points[k + 1].y_idx;
                lastX[key] = points[i].x;
            }

            i = j;
        }

        return maxArea;
    }
};
# @lc code=end