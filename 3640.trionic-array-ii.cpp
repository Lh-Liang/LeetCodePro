#
# @lc app=leetcode id=3640 lang=cpp
#
# [3640] Trionic Array II
#

# @lc code=start
class Solution {
public:
    long long maxSumTrionic(vector<int>& nums) {
        int n = nums.size();
        vector<long long> prefix(n+1, 0);
        for (int i = 0; i < n; ++i) prefix[i+1] = prefix[i] + nums[i];

        // Compute length of strictly increasing run ending at i
        vector<int> incL(n, 1), incR(n, 1), dec(n, 1);
        for (int i = 1; i < n; ++i) {
            if (nums[i] > nums[i-1]) incL[i] = incL[i-1] + 1;
            if (nums[i] < nums[i-1]) dec[i] = dec[i-1] + 1;
        }
        // Compute length of strictly increasing run starting at i
        for (int i = n-2; i >= 0; --i) {
            if (nums[i] < nums[i+1]) incR[i] = incR[i+1] + 1;
        }

        long long ans = LLONG_MIN;
        // For each possible p (peak at dec), try to expand left and right
        for (int mid = 1; mid < n-2; ++mid) {
            // p is mid, q is mid+1
            // incL[mid]: length of inc ending at mid, dec[mid+1]: length of dec ending at mid+1
            int lmax = incL[mid]-1; // at least 1
            int dmax = dec[mid+1]-1;
            int rmax = incR[mid+1]-1;
            if (lmax >= 1 && dmax >= 1 && rmax >= 1) {
                int l = mid - lmax;
                int r = mid+1 + rmax;
                long long sum = prefix[r] - prefix[l];
                ans = max(ans, sum);
            }
        }
        return ans;
    }
};
# @lc code=end