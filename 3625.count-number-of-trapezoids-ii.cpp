#
# @lc app=leetcode id=3625 lang=cpp
#
# [3625] Count Number of Trapezoids II
#

# @lc code=start
class Solution {
public:
    int countTrapezoids(vector<vector<int>>& points) {
        int n = points.size();
        int count = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                for (int k = j + 1; k < n; ++k) {
                    for (int l = k + 1; l < n; ++l) {
                        // Use integer arithmetic to determine parallel lines.
                        int dx_ij = points[j][0] - points[i][0];
                        int dy_ij = points[j][1] - points[i][1];
                        int dx_kl = points[l][0] - points[k][0];
                        int dy_kl = points[l][1] - points[k][1];
                        int dx_ik = points[k][0] - points[i][0];
                        int dy_ik = points[k][1] - points[i][1];
                        int dx_jl = points[l][0] - points[j][0];
                        int dy_jl = points[l][1] - points[j][1];
                        // Check for parallelism using cross multiplication.
                        if ((dy_ij * dx_kl == dy_kl * dx_ij && dy_ik * dx_jl != dy_jl * dx_ik) || 
                            (dy_ik * dx_jl == dy_jl * dx_ik && dy_ij * dx_kl != dy_kl * dx_ij)) {
                            count++;
                        }
                    }
                }
            } 
        } 
        return count; 
    } 
}; 
# @lc code=end