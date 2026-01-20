#
# @lc app=leetcode id=3513 lang=cpp
#
# [3513] Number of Unique XOR Triplets I
#

# @lc code=start
class Solution {
public:
    int uniqueXorTriplets(vector<int>& nums) {
        int n = nums.size();
        if (n == 1) return 1;
        if (n == 2) return 2;
        
        // For n >= 3, the reachable values cover the range [0, P-1] where P is the 
        // smallest power of 2 strictly greater than n.
        // This is because with {1, 2, 3} (n=3) we can form {0, 1, 2, 3}. 
        // By induction, if we can form [0, 2^k - 1], adding 2^k allows us to form 
        // [2^k, 2^{k+1} - 1] as well, provided we have enough elements to form any XOR pair.
        
        long long p = 1;
        while (p <= n) {
            p <<= 1;
        }
        return (int)p;
    }
};
# @lc code=end