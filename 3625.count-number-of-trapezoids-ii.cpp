#
# @lc app=leetcode id=3625 lang=cpp
#
# [3625] Count Number of Trapezoids II
#

# @lc code=start
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <numeric>
using namespace std;

class Solution {
public:
    using pii = pair<int, int>;
    using vi = vector<int>;
    int countTrapezoids(vector<vector<int>>& points) {
        int n = points.size();
        // Map slope to list of segments (each segment is a pair of indices)
        map<pii, vector<pair<int,int>>> slope_map;
        // Helper to reduce slope to canonical form
        auto get_slope = [](const vi& a, const vi& b) {
            int dx = b[0] - a[0];
            int dy = b[1] - a[1];
            if (dx == 0) return pii{1, 0}; // vertical
            if (dy == 0) return pii{0, 1}; // horizontal
            int g = gcd(dx, dy);
            dx /= g; dy /= g;
            if (dx < 0) { dx = -dx; dy = -dy; }
            return pii{dy, dx}; // (dy/dx)
        };
        // Step 1: For each pair of points, store by slope
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                pii slope = get_slope(points[i], points[j]);
                slope_map[slope].emplace_back(i, j);
            }
        }
        set<vector<int>> quads;
        // Step 2: For each slope group, choose two non-overlapping segments
        for (auto& [slope, segs] : slope_map) {
            int m = segs.size();
            for (int i = 0; i < m; ++i) {
                for (int j = i+1; j < m; ++j) {
                    auto& [a1, a2] = segs[i];
                    auto& [b1, b2] = segs[j];
                    set<int> pts = {a1, a2, b1, b2};
                    if (pts.size() != 4) continue; // skip overlapping
                    // Step 3: Check if quadrilateral is convex
                    vector<vi> quad;
                    for (int idx : pts) quad.push_back(points[idx]);
                    // To check convexity, compute cross products for all 4 corners
                    bool convex = true;
                    for (int k = 0; k < 4 && convex; ++k) {
                        auto& A = quad[k];
                        auto& B = quad[(k+1)%4];
                        auto& C = quad[(k+2)%4];
                        int dx1 = B[0] - A[0], dy1 = B[1] - A[1];
                        int dx2 = C[0] - B[0], dy2 = C[1] - B[1];
                        int cross = dx1*dy2 - dy1*dx2;
                        if (cross == 0) { convex = false; break; } // degenerate
                    }
                    if (!convex) continue;
                    // Step 4: Canonicalize this quad and add to set to avoid duplicates
                    vector<int> idxs(pts.begin(), pts.end());
                    sort(idxs.begin(), idxs.end());
                    quads.insert(idxs);
                }
            }
        }
        return quads.size();
    }
};
# @lc code=end