# @lc code=start
class Solution {
public:
    int countNumbers(string l, string r, int b) {
        const int MOD = 1e9 + 7;
        
        // Helper function to convert a string number in base-10 to an integer in base-b
        auto convertToBase = [](const string &numStr, int base) -> vector<int> {
            vector<int> digits;
            int num = stoi(numStr);
            while (num > 0) {
                digits.push_back(num % base);
                num /= base;
            }
            reverse(digits.begin(), digits.end());
            return digits;
        };

        // Helper function using DP to calculate non-decreasing count up to n in base b
        auto calculateNonDecreasingCount = [&](const vector<int>& n) -> int {
            int len = n.size();
            vector<vector<int>> dp(len + 1, vector<int>(b));
            
            // Base case initialization
            for (int i = 0; i < b; ++i) dp[0][i] = 1;
            
            // Fill DP table based on transitions
            for (int i = 1; i <= len; ++i) {
                for (int d = 0; d < b; ++d) {
                    for (int prev_d = d; prev_d < b; ++prev_d) {
                        dp[i][d] += dp[i - 1][prev_d];
                        dp[i][d] %= MOD;
                    }
                }
            }

            // Sum all valid counts of full length 'len'
            int result = 0;
            for (int d = n[len - 1]; d >= 0; --d) {
                result += dp[len][d];
                result %= MOD;
            }

            return result;
        };
        
        // Convert l and r to base-b representation vectors
        vector<int> lb = convertToBase(l, b);
        vector<int> rb = convertToBase(r, b);
        
        // Calculate counts for ranges using helper function
        int result_r = calculateNonDecreasingCount(rb);
        int result_l_minus_1 = calculateNonDecreasingCount(lb); // Adjust logic if needed for l-1 handling

        // Ensure no negative results by adding MOD before applying modulo operation again.												};	}	};	# @lc code=end