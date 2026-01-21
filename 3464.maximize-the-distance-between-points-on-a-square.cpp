#
# @lc app=leetcode id=3464 lang=cpp
#
# [3464] Maximize the Distance Between Points on a Square
#
# @lc code=start
class Solution {
public:
    int maxDistance(int side, vector<vector<int>>& points, int k) {
        // Binary search on the minimum distance
        long long left = 0, right = 2LL * side;
        long long answer = 0;
        
        while (left <= right) {
            long long mid = left + (right - left) / 2;
            if (canSelect(points, k, mid)) {
                answer = mid;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        
        return (int)answer;
    }
    
private:
    bool canSelect(vector<vector<int>>& points, int k, long long minDist) {
        vector<int> selected;
        return backtrack(points, k, minDist, 0, selected);
    }
    
    bool backtrack(vector<vector<int>>& points, int k, long long minDist, int start, vector<int>& selected) {
        if ((int)selected.size() == k) {
            return true;
        }
        
        // Pruning: check if we have enough points left
        if ((int)points.size() - start + (int)selected.size() < k) {
            return false;
        }
        
        for (int i = start; i < (int)points.size(); i++) {
            // Check if points[i] is valid (at least minDist from all selected)
            bool valid = true;
            for (int idx : selected) {
                long long dist = abs((long long)points[i][0] - points[idx][0]) + 
                                 abs((long long)points[i][1] - points[idx][1]);
                if (dist < minDist) {
                    valid = false;
                    break;
                }
            }
            
            if (valid) {
                selected.push_back(i);
                if (backtrack(points, k, minDist, i + 1, selected)) {
                    return true;
                }
                selected.pop_back();
            }
        }
        
        return false;
    }
};
# @lc code=end