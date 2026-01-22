#
# @lc app=leetcode id=3548 lang=cpp
#
# [3548] Equal Sum Grid Partition II
#

# @lc code=start
class Solution {
public:
    bool canPartitionGrid(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        
        long long total = 0;
        unordered_map<long long, set<int>> valueRows, valueCols;
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                long long v = grid[i][j];
                total += v;
                valueRows[v].insert(i);
                valueCols[v].insert(j);
            }
        }
        
        auto existsInRows = [&](long long v, int r1, int r2) -> bool {
            auto it = valueRows.find(v);
            if (it == valueRows.end()) return false;
            auto iter = it->second.lower_bound(r1);
            return iter != it->second.end() && *iter <= r2;
        };
        
        auto existsInCols = [&](long long v, int c1, int c2) -> bool {
            auto it = valueCols.find(v);
            if (it == valueCols.end()) return false;
            auto iter = it->second.lower_bound(c1);
            return iter != it->second.end() && *iter <= c2;
        };
        
        // Horizontal cuts
        long long upperSum = 0;
        for (int i = 0; i < m - 1; i++) {
            for (int j = 0; j < n; j++) upperSum += grid[i][j];
            long long lowerSum = total - upperSum;
            
            if (upperSum == lowerSum) return true;
            
            long long diff = upperSum - lowerSum;
            int upperH = i + 1, lowerH = m - i - 1;
            
            if (diff > 0) {
                if (upperH == 1 && n == 1) { }
                else if (upperH == 1) { 
                    if ((long long)grid[0][0] == diff || (long long)grid[0][n-1] == diff) return true; 
                }
                else if (n == 1) { 
                    if ((long long)grid[0][0] == diff || (long long)grid[i][0] == diff) return true; 
                }
                else { if (existsInRows(diff, 0, i)) return true; }
            } else if (diff < 0) {
                diff = -diff;
                if (lowerH == 1 && n == 1) { }
                else if (lowerH == 1) { 
                    if ((long long)grid[m-1][0] == diff || (long long)grid[m-1][n-1] == diff) return true; 
                }
                else if (n == 1) { 
                    if ((long long)grid[i+1][0] == diff || (long long)grid[m-1][0] == diff) return true; 
                }
                else { if (existsInRows(diff, i+1, m-1)) return true; }
            }
        }
        
        // Vertical cuts
        long long leftSum = 0;
        for (int j = 0; j < n - 1; j++) {
            for (int i = 0; i < m; i++) leftSum += grid[i][j];
            long long rightSum = total - leftSum;
            
            if (leftSum == rightSum) return true;
            
            long long diff = leftSum - rightSum;
            int leftW = j + 1, rightW = n - j - 1;
            
            if (diff > 0) {
                if (m == 1 && leftW == 1) { }
                else if (m == 1) { 
                    if ((long long)grid[0][0] == diff || (long long)grid[0][j] == diff) return true; 
                }
                else if (leftW == 1) { 
                    if ((long long)grid[0][0] == diff || (long long)grid[m-1][0] == diff) return true; 
                }
                else { if (existsInCols(diff, 0, j)) return true; }
            } else if (diff < 0) {
                diff = -diff;
                if (m == 1 && rightW == 1) { }
                else if (m == 1) { 
                    if ((long long)grid[0][j+1] == diff || (long long)grid[0][n-1] == diff) return true; 
                }
                else if (rightW == 1) { 
                    if ((long long)grid[0][n-1] == diff || (long long)grid[m-1][n-1] == diff) return true; 
                }
                else { if (existsInCols(diff, j+1, n-1)) return true; }
            }
        }
        
        return false;
    }
};
# @lc code=end