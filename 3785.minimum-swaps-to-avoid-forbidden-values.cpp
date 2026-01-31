#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

class Solution {
public:
    int minSwaps(vector<int>& nums, vector<int>& forbidden) {
        int n = nums.size();
        
        // Global Feasibility: For any value x, count(nums, x) + count(forbidden, x) <= n
        unordered_map<int, int> num_freq;
        unordered_map<int, int> forbidden_freq;
        for (int i = 0; i < n; ++i) {
            num_freq[nums[i]]++;
            forbidden_freq[forbidden[i]]++;
        }
        
        for (auto const& it : num_freq) {
            if (it.second > n - forbidden_freq[it.first]) return -1;
        }

        // Identify conflicts (bad indices)
        int total_bad = 0;
        int max_bad_freq = 0;
        unordered_map<int, int> bad_val_freq;
        
        for (int i = 0; i < n; ++i) {
            if (nums[i] == forbidden[i]) {
                total_bad++;
                int freq = ++bad_val_freq[nums[i]];
                if (freq > max_bad_freq) max_bad_freq = freq;
            }
        }

        if (total_bad == 0) return 0;

        // The minimum swaps is constrained by two factors:
        // 1. Each swap can fix at most 2 conflicts: ceil(total_bad / 2)
        // 2. A dominant value appearing M times in conflicts requires at least M swaps
        int res = (total_bad + 1) / 2;
        if (max_bad_freq > res) res = max_bad_freq;
        
        return res;
    }
};