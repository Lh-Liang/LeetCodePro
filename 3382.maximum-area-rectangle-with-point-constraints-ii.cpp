#
# @lc app=leetcode id=3382 lang=cpp
#
# [3382] Maximum Area Rectangle With Point Constraints II
#

# @lc code=start
class Solution {
    struct FenwickTree {
        int size;
        vector<int> tree;
        
        FenwickTree(int n) : size(n), tree(n + 1, 0) {}
        
        void add(int index, int val) {
            for (; index <= size; index += index & -index) {
                tree[index] += val;
            }
        }
        
        int query(int index) {
            int sum = 0;
            for (; index > 0; index -= index & -index) {
                sum += tree[index];
            }
            return sum;
        }
    };

public:
    long long maxRectangleArea(vector<int>& xCoord, vector<int>& yCoord) {
        int n = xCoord.size();
        vector<pair<int, int>> points(n);
        vector<int> distinctY;
        distinctY.reserve(n);
        
        for (int i = 0; i < n; ++i) {
            points[i] = {xCoord[i], yCoord[i]};
            distinctY.push_back(yCoord[i]);
        }
        
        sort(distinctY.begin(), distinctY.end());
        distinctY.erase(unique(distinctY.begin(), distinctY.end()), distinctY.end());
        
        auto getY = [&](int y) {
            return lower_bound(distinctY.begin(), distinctY.end(), y) - distinctY.begin() + 1;
        };
        
        sort(points.begin(), points.end());
        
        FenwickTree bit(distinctY.size());
        // Map key: (y1_compressed << 32 | y2_compressed)
        // Map value: {x_coord, bit_sum_snapshot}
        unordered_map<long long, pair<int, int>> activeSegments;
        
        long long maxArea = -1;
        
        for (int i = 0; i < n; ) {
            int j = i;
            while (j < n && points[j].first == points[i].first) {
                j++;
            }
            
            // Points from i to j-1 have the same x-coordinate
            // Check for valid rectangles with previous segments
            for (int k = i; k < j - 1; ++k) {
                int y1 = points[k].second;
                int y2 = points[k+1].second;
                int y1_idx = getY(y1);
                int y2_idx = getY(y2);
                
                long long key = ((long long)y1_idx << 32) | y2_idx;
                
                if (activeSegments.count(key)) {
                    auto [prevX, prevSum] = activeSegments[key];
                    int currentSum = bit.query(y2_idx) - bit.query(y1_idx - 1);
                    
                    if (currentSum == prevSum) {
                        long long area = (long long)(points[i].first - prevX) * (y2 - y1);
                        if (area > maxArea) {
                            maxArea = area;
                        }
                    }
                }
            }
            
            // Add current points to BIT
            for (int k = i; k < j; ++k) {
                bit.add(getY(points[k].second), 1);
            }
            
            // Update active segments
            for (int k = i; k < j - 1; ++k) {
                int y1 = points[k].second;
                int y2 = points[k+1].second;
                int y1_idx = getY(y1);
                int y2_idx = getY(y2);
                
                long long key = ((long long)y1_idx << 32) | y2_idx;
                int currentSum = bit.query(y2_idx) - bit.query(y1_idx - 1);
                activeSegments[key] = {points[i].first, currentSum};
            }
            
            i = j;
        }
        
        return maxArea;
    }
};
# @lc code=end