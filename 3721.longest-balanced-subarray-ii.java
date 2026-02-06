#
# @lc app=leetcode id=3721 lang=java
#
# [3721] Longest Balanced Subarray II
#

# @lc code=start
class Solution {
    public int longestBalanced(int[] nums) {
        int maxLen = 0;
        int left = 0;
        Map<Integer, Integer> evens = new HashMap<>();
        Map<Integer, Integer> odds = new HashMap<>();
        
        for (int right = 0; right < nums.length; right++) {
            int num = nums[right];
            if (num % 2 == 0) { // even number
                evens.put(num, evens.getOrDefault(num, 0) + 1);
            } else { // odd number
                odds.put(num, odds.getOrDefault(num, 0) + 1);
            }
            
            while (evens.size() > odds.size()) { // balance condition adjustment
                int leftNum = nums[left];
                if (leftNum % 2 == 0) { // adjust even map size
                    evens.put(leftNum, evens.get(leftNum) - 1);
                    if (evens.get(leftNum) == 0) { evens.remove(leftNum); }
                } else { // adjust odd map size
                    odds.put(leftNum, odds.get(leftNum) - 1);
                    if (odds.get(leftNum) == 0) { odds.remove(leftNum); }
                }
                left++; // move left pointer to shrink window
            } else if (odds.size() > evens.size()) { // balance condition adjustment in reverse case 
                while(odds.size() > evens.size()) { …
                                int leftNum = nums[left];
                                if (leftNum % 2 != 0) {
                                    odds.put(leftNum, odds.get(leftNum) - 1);
                                    if (odds.get(leftNum) == 0) {
                                        odds.remove(leftNum);
                                    }
                                } else {
                                    evens.put(leftNum, evens.get(leftNum) - 1);
                                    if (evens.get(leftNum) == 0) {
                                        evens.remove(leftNum);
                                    }
                                }
                                left++;
                            }
                        }
                        if (evens.size() == odds.size()) {
                            maxLen = Math.max(maxLen, right - left + 1);
                        }
                    }
                    return maxLen;
                }
            }