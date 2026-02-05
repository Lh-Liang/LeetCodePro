#
# @lc app=leetcode id=3445 lang=java
#
# [3445] Maximum Difference Between Even and Odd Frequency II
#

# @lc code=start
class Solution {
    public int maxDifference(String s, int k) {
        Map<Character, Integer> freqMap = new HashMap<>();
        int maxDiff = Integer.MIN_VALUE;
        
        for (int start = 0, end = 0; end < s.length(); end++) {
            char cEnd = s.charAt(end);
            freqMap.put(cEnd, freqMap.getOrDefault(cEnd, 0) + 1);
            
            while (end - start + 1 > k) {
                char cStart = s.charAt(start);
                freqMap.put(cStart, freqMap.get(cStart) - 1);
                if (freqMap.get(cStart) == 0) {
                    freqMap.remove(cStart);
                }
                start++;
            }
            
            if (end - start + 1 >= k) { 
                int maxOddFreq = Integer.MIN_VALUE;
                int minEvenFreq = Integer.MAX_VALUE;
                
                for (char key : freqMap.keySet()) {
                    int freq = freqMap.get(key);
                    if (freq % 2 == 1) { 
                        maxOddFreq = Math.max(maxOddFreq, freq);
                    } else if (freq > 0 && freq % 2 == 0) { 
                        minEvenFreq = Math.min(minEvenFreq, freq);
                    }
                }
                
                if (maxOddFreq != Integer.MIN_VALUE && minEvenFreq != Integer.MAX_VALUE) { 
                    maxDiff = Math.max(maxDiff, maxOddFreq - minEvenFreq);
                }
            }
        }
        return maxDiff == Integer.MIN_VALUE ? -1 : maxDiff; 
    } 
}
# @lc code=end