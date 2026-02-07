class Solution {
public:
    long long maximizeXorAndXor(vector<int>& nums) {
        int n = nums.size();
        long long max_value = 0;

        // Helper function to calculate XOR of a set
        auto calculateXOR = [](const vector<int>& subset) {
            int xor_value = 0;
            for (int num : subset) xor_value ^= num;
            return xor_value;
        };

        // Helper function to calculate AND of a set
        auto calculateAND = [](const vector<int>& subset) {
            if (subset.empty()) return 0;
            int and_value = subset[0];
            for (int i = 1; i < subset.size(); ++i) and_value &= subset[i];
            return and_value;
        };

        // Try all possible partitions using bitmasks
        for (int maskA = 0; maskA < (1 << n); ++maskA) {
            for (int maskB = 0; maskB < (1 << n); ++maskB) {
                if ((maskA & maskB) != 0) continue; // A and B must be disjoint
                vector<int> A, B, C;
                for (int i = 0; i < n; ++i) {
                    if ((maskA & (1 << i)) != 0) A.push_back(nums[i]);
                    else if ((maskB & (1 << i)) != 0) B.push_back(nums[i]);
                    else C.push_back(nums[i]);
                }
                long long current_value = calculateXOR(A) + calculateAND(B) + calculateXOR(C);
                max_value = max(max_value, current_value);
            }
        }

        return max_value;
    }
};