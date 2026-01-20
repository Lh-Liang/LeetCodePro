#
# @lc app=leetcode id=3513 lang=cpp
#
# [3513] Number of Unique XOR Triplets I
#

# @lc code=start
#include <vector>
#include <cmath>

using namespace std;

class Solution {
public:
    int uniqueXorTriplets(vector<int>& nums) {
        int n = nums.size();
        if (n == 1) return 1;
        if (n == 2) return 2;
        
        // For n >= 3, the unique XOR triplets will cover all values from 0 to 2^m - 1
        // where m is the number of bits required to represent n.
        // This is because we can always form 0 (1^2^3) and any value x in [1, n].
        // XORing x with 0 (as 1^2^3) and other combinations allows us to span the basis.
        int m = 0;
        int temp_n = n;
        while (temp_n > 0) {
            temp_n >>= 1;
            m++;
        }
        
        return (1 << m);
    }
};
# @lc code=end