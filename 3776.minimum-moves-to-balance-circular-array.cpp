#
# @lc app=leetcode id=3776 lang=cpp
#
# [3776] Minimum Moves to Balance Circular Array
#

# @lc code=start
class Solution {
public:
    long long minMoves(vector<int>& balance) {
        int n = balance.size();
        long long sum = 0;
        for (int x : balance) sum += x;
        if (sum < 0) return -1;
        
        // Find deficit position
        int deficitPos = -1;
        long long D = 0;
        for (int i = 0; i < n; i++) {
            if (balance[i] < 0) {
                deficitPos = i;
                D = -(long long)balance[i];
                break;
            }
        }
        
        if (deficitPos == -1) return 0; // No deficit
        
        // Greedy fill by distance
        long long cost = 0;
        long long filled = 0;
        
        for (int d = 1; d <= n / 2 && filled < D; d++) {
            int pos1 = (deficitPos + d) % n;
            int pos2 = (deficitPos - d + n) % n;
            
            if (pos1 == pos2) {
                long long take = min((long long)balance[pos1], D - filled);
                cost += (long long)d * take;
                filled += take;
            } else {
                long long take1 = min((long long)balance[pos1], D - filled);
                cost += (long long)d * take1;
                filled += take1;
                
                if (filled < D) {
                    long long take2 = min((long long)balance[pos2], D - filled);
                    cost += (long long)d * take2;
                    filled += take2;
                }
            }
        }
        
        return cost;
    }
};
# @lc code=end