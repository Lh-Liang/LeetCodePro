# @lc app=leetcode id=3625 lang=cpp
# # [3625] Count Number of Trapezoids II

#include <vector>
#include <unordered_set>
#include <algorithm>
#include <tuple>
using namespace std;

class Solution {
public:
    int countTrapezoids(vector<vector<int>>& points) {
        auto slope_equal = [](const vector<int>& a, const vector<int>& b,
                              const vector<int>& c, const vector<int>& d) {
            // Calculate cross product to check if two lines are parallel
            return (b[1] - a[1]) * (d[0] - c[0]) == (d[1] - c[1]) * (b[0] - a[0]);
        };
        
        unordered_set<string> unique_trapezoids;
        int n = points.size();
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                for (int k = j + 1; k < n; ++k) {
                    for (int l = k + 1; l < n; ++l) {
                        // Check pairs for parallelism
                        bool is_trapezoid = slope_equal(points[i], points[j], points[k], points[l]) ||
                                            slope_equal(points[i], points[k], points[j], points[l]) ||
                                            slope_equal(points[i], points[l], points[j], points[k]);
                        if (is_trapezoid) {
                            // Sort and encode points to ensure uniqueness
                            vector<vector<int>> quad = {points[i], points[j], points[k], points[l]};
                            sort(quad.begin(), quad.end());
                            string key;
                            for (const auto& p : quad) {
                                key += to_string(p[0]) + "," + to_string(p[1]) + ";";
                            }
                            unique_trapezoids.insert(key);
                        }
                    }
                }
            }
        }
        return unique_trapezoids.size();
    }
};