#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

class Solution {
    // GCD Stack supporting O(1) GCD of its elements
    struct GCDStack {
        vector<long long> val, g;
        void push(long long x) {
            val.push_back(x);
            if (g.empty()) g.push_back(x);
            else g.push_back(std::gcd(x, g.back()));
        }
        void pop() {
            val.pop_back();
            g.pop_back();
        }
        long long top_val() { return val.back(); }
        long long top_gcd() { return g.empty() ? 0 : g.back(); }
        bool empty() { return val.empty(); }
    };

    // GCD Queue using two stacks for O(1) amortized sliding window GCD
    struct GCDQueue {
        GCDStack s1, s2;
        void push(long long x) { s1.push(x); }
        void pop() {
            if (s2.empty()) {
                while (!s1.empty()) {
                    s2.push(s1.top_val());
                    s1.pop();
                }
            }
            if (!s2.empty()) s2.pop();
        }
        long long gcd() {
            if (s1.empty()) return s2.top_gcd();
            if (s2.empty()) return s1.top_gcd();
            return std::gcd(s1.top_gcd(), s2.top_gcd());
        }
    };

    bool check(int K, const vector<int>& nums, int maxC) {
        // If we want to check if stability factor <= K, we must break all subarrays of length K+1
        int n = nums.size();
        if (K >= n) return true;
        
        int mods = 0;
        int last_modified_idx = -1;
        GCDQueue q;
        int L = K + 1;

        for (int i = 0; i < n; ++i) {
            q.push(nums[i]);
            if (i >= L) {
                q.pop();
            }
            
            if (i >= L - 1) {
                int start_idx = i - L + 1;
                // If the current subarray [start_idx, i] is stable AND 
                // hasn't been broken by a previous modification within its range
                if (last_modified_idx < start_idx) {
                    if (q.gcd() >= 2) {
                        mods++;
                        last_modified_idx = i; // Greedy: modify the rightmost element
                    }
                }
            }
            if (mods > maxC) return false;
        }
        return mods <= maxC;
    }

public:
    int minStable(vector<int>& nums, int maxC) {
        int n = nums.size();
        if (maxC >= n) return 0;

        int low = 0, high = n;
        int ans = n;

        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (check(mid, nums, maxC)) {
                ans = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }

        return ans;
    }
};