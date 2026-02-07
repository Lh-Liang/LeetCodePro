#
# @lc app=leetcode id=3398 lang=cpp
#
# [3398] Smallest Substring With Identical Characters I
#

# @lc code=start
class Solution {
public:
    int minLength(string s, int numOps) {
        // Initialize variables to track left and right pointers, number of zeroes and ones.
        int n = s.size();
        int left = 0, right = 0;
        int countZero = 0, countOne = 0;
        int maxBlockSize = INT_MAX;
        
        // Use sliding window technique.
        while (right < n) {
            // Increment counts based on current character.
            if (s[right] == '0') {
                countZero++;
            } else {
                countOne++;
            }
            
            // If more than numOps flips needed for either character, move left pointer.
            while (std::min(countZero, countOne) > numOps) {
                if (s[left] == '0') {
                    countZero--;
                } else {
                    countOne--;
                }
                left++;
            }
            
            // Update maxBlockSize with current window size.
            maxBlockSize = std::min(maxBlockSize, right - left + 1);
            right++;
        } 
        return maxBlockSize;   	// Return minimum block size found after operations. 	}	}; # @lc code=end