# @lc code=start
#include <vector>
#include <numeric> // for gcd
typedef long long ll;
const int MOD = 1000000007;
using namespace std;

class Solution {
public:
    int countCoprime(vector<vector<int>>& mat) {
        int m = mat.size();
        int n = mat[0].size();
        vector<vector<ll>> dp(m, vector<ll>(151));
        // Initialize for the first row
        for (int num : mat[0]) {
            dp[0][num]++;
        }
        
        // Fill dp table for subsequent rows
        for (int i = 1; i < m; ++i) {
            vector<ll> new_dp(151);
            for (int num : mat[i]) {
                for (int g = 1; g <= 150; ++g) {
                    int new_gcd = gcd(g, num);
                    new_dp[new_gcd] = (new_dp[new_gcd] + dp[i-1][g]) % MOD;
                }
            }
            dp[i] = new_dp;
        }
        
        return dp[m-1][1]; // Return the count of combinations with GCD=1
    }
};
# @lc code=end