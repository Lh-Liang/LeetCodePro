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
    typedef pair<int, int> Point;
    typedef pair<Point, Point> Segment;
    
    // Helper to compute reduced slope as a pair
    pair<int, int> getSlope(const Point& a, const Point& b) {
        int dx = b.first - a.first, dy = b.second - a.second;
        if (dx == 0) return {1, 0};  // vertical
        if (dy == 0) return {0, 1};  // horizontal
        int g = gcd(dx, dy);
        dx /= g; dy /= g;
        // Normalize sign: only dx can be negative
        if (dx < 0) { dx = -dx; dy = -dy; }
        return {dy, dx};
    }
    
    // Check if the quadrilateral formed by p0,p1,p2,p3 is convex
    bool isConvex(const vector<Point>& quad) {
        vector<long long> cross;
        for (int i = 0; i < 4; ++i) {
            int j = (i + 1) % 4, k = (i + 2) % 4;
            long long dx1 = quad[j].first - quad[i].first;
            long long dy1 = quad[j].second - quad[i].second;
            long long dx2 = quad[k].first - quad[j].first;
            long long dy2 = quad[k].second - quad[j].second;
            cross.push_back(dx1 * dy2 - dy1 * dx2);
        }
        // All cross products must have the same sign
        bool pos = all_of(cross.begin(), cross.end(), [](long long x) { return x > 0; });
        bool neg = all_of(cross.begin(), cross.end(), [](long long x) { return x < 0; });
        return pos || neg;
    }

    int countTrapezoids(vector<vector<int>>& points) {
        int n = points.size();
        vector<Point> pts;
        for (auto& p : points) pts.emplace_back(p[0], p[1]);

        // Group all segments by reduced slope
        map<pair<int,int>, vector<Segment>> slope2seg;
        for (int i = 0; i < n; ++i) for (int j = i+1; j < n; ++j) {
            auto s = getSlope(pts[i], pts[j]);
            slope2seg[s].push_back({pts[i], pts[j]});
        }

        set<vector<Point>> uniqueQuads;
        // For each group of parallel segments, consider all non-overlapping pairs
        for (auto& [slope, segs] : slope2seg) {
            int m = segs.size();
            for (int i = 0; i < m; ++i) for (int j = i+1; j < m; ++j) {
                // Get the four endpoints
                vector<Point> quad = {segs[i].first, segs[i].second, segs[j].first, segs[j].second};
                // All points must be unique
                sort(quad.begin(), quad.end());
                if (adjacent_find(quad.begin(), quad.end()) != quad.end()) continue;
                // All points unique, check all permutations for convex
                do {
                    if (isConvex(quad)) {
                        uniqueQuads.insert(quad);
                        break;
                    }
                } while (next_permutation(quad.begin(), quad.end()));
            }
        }
        return uniqueQuads.size();
    }
};
# @lc code=end