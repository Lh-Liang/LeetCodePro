#
# @lc app=leetcode id=3605 lang=cpp
#
# [3605] Minimum Stability Factor of Array
#

# @lc code=start
class Solution {
    vector<vector<int>> st;
    vector<int> logs;
    int n;

    int gcd(int a, int b) {
        while (b) {
            a %= b;
            swap(a, b);
        }
        return a;
    }

    void buildST(const vector<int>& nums) {
        n = nums.size();
        logs.resize(n + 1);
        logs[1] = 0;
        for (int i = 2; i <= n; i++)
            logs[i] = logs[i / 2] + 1;
        
        int K = logs[n];
        st.assign(n, vector<int>(K + 1));

        for (int i = 0; i < n; i++)
            st[i][0] = nums[i];

        for (int j = 1; j <= K; j++) {
            for (int i = 0; i + (1 << j) <= n; i++) {
                st[i][j] = gcd(st[i][j - 1], st[i + (1 << (j - 1))][j - 1]);
            }
        }
    }

    int query(int L, int R) {
        int j = logs[R - L + 1];
        return gcd(st[L][j], st[R - (1 << j) + 1][j]);
    }

    bool check(int len, int maxC) {
        // We want to check if it's possible to satisfy that max stable subarray length is <= len
        // This means we need to break all stable subarrays of length len + 1
        int target = len + 1;
        if (target > n) return true;

        int count = 0;
        int last_mod = -1;

        for (int i = target - 1; i < n; ++i) {
            // Consider the window ending at i with length 'target': [i - target + 1, i]
            
            // If we recently modified an element within this window, the chain is already broken.
            // The window starts at 'start = i - target + 1'.
            // If last_mod >= start, then the window is broken.
            if (last_mod < i - target + 1) {
                // Check stability of the original subarray
                if (query(i - target + 1, i) >= 2) {
                    // It is stable, so we must modify an element to break it.
                    // Greedy strategy: modify the rightmost element (index i) to maximize the effect on future windows.
                    count++;
                    last_mod = i;
                    if (count > maxC) return false;
                }
            }
        }
        return count <= maxC;
    }

public:
    int minStable(vector<int>& nums, int maxC) {
        buildST(nums);
        int left = 0, right = n;
        int ans = n;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (check(mid, maxC)) {
                ans = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return ans;
    }
};
# @lc code=end