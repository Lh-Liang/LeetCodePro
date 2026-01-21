#
# @lc app=leetcode id=3605 lang=cpp
#
# [3605] Minimum Stability Factor of Array
#
# @lc code=start
class Solution {
public:
    int gcd(int a, int b) {
        while (b) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
    
    bool canAchieve(vector<int>& nums, int maxC, int K) {
        int n = nums.size();
        int i = 0;
        int total_breaks = 0;
        
        while (i < n) {
            if (nums[i] < 2) {
                i++;
                continue;
            }
            
            int j = i;
            int current_gcd = nums[i];
            while (j + 1 < n) {
                int new_gcd = gcd(current_gcd, nums[j + 1]);
                if (new_gcd < 2) {
                    break;
                }
                current_gcd = new_gcd;
                j++;
            }
            
            int L = j - i + 1;
            if (L > K) {
                int breaks_needed = L / (K + 1);
                total_breaks += breaks_needed;
            }
            
            i = j + 1;
        }
        
        return total_breaks <= maxC;
    }
    
    int minStable(vector<int>& nums, int maxC) {
        int n = nums.size();
        
        int elements_gte_2 = 0;
        for (int num : nums) {
            if (num >= 2) elements_gte_2++;
        }
        
        if (elements_gte_2 <= maxC) {
            return 0;
        }
        
        int left = 1, right = n;
        int answer = n;
        
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (canAchieve(nums, maxC, mid)) {
                answer = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        
        return answer;
    }
};
# @lc code=end