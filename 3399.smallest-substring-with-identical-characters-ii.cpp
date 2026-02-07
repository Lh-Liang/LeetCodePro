# @lc app=leetcode id=3399 lang=cpp
# [3399] Smallest Substring With Identical Characters II
# @lc code=start
class Solution {
public:
    int minLength(string s, int numOps) {
        int n = s.size();
        if (numOps >= n) return 1; // If operations exceed or equal string length, all can be made identical
        vector<int> prefixZeros(n + 1, 0), prefixOnes(n + 1, 0);
        
        // Create prefix sum arrays for zeros and ones
        for (int i = 0; i < n; ++i) {
            prefixZeros[i + 1] = prefixZeros[i] + (s[i] == '0');
            prefixOnes[i + 1] = prefixOnes[i] + (s[i] == '1');
        }
        
        int result = n; // Initialize result with maximum possible length 
        // Use sliding windows to find minimum max segment length
        for (int start = 0, end = 0; end < n; ++end) {
            while (start <= end && min(prefixOnes[end + 1] - prefixOnes[start], \
prefixZeros[end + 1] - prefixZeros[start]) > numOps) {
                ++start;
            }
            result = min(result, end - start + 1);
        }
        return result;
    }
};
# @lc code=end