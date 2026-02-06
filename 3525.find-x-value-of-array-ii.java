#
# @lc app=leetcode id=3525 lang=java
#
# [3525] Find X Value of Array II
#
# @lc code=start
class Solution {
    public int[] resultArray(int[] nums, int k, int[][] queries) {
        int n = nums.length;
        int[] result = new int[queries.length];
        
        // Precompute powers modulo k for efficiency
        int[] powerMod = new int[n+1]; // powerMod[i] will store (nums[i] % k) * (nums[i+1] % k) * ... % k
        powerMod[n] = 1; // Base case: product is 1 when no elements are considered
        for (int i = n - 1; i >= 0; i--) {
            powerMod[i] = (powerMod[i+1] * (nums[i] % k)) % k;
        }
        
        for (int q = 0; q < queries.length; q++) {
            int index = queries[q][0];
            int value = queries[q][1];
            int start = queries[q][2];
            int xValueTarget = queries[q][3];
            
            // Update nums[index]
            nums[index] = value;
            
            // Recompute powerMod from start to end due to update at index `index` if necessary
            for (int i = Math.max(start, index); i < n; i++) {
                powerMod[i] = ((i == n-1 ? 1 : powerMod[i+1]) * (nums[i] % k)) % k;
            }
            
            // Calculate number of suffixes resulting in remainder xValueTarget when taken mod k from start to end suffixes possible from current state starting at `start` prefix removed. 
            int countXValues = 0;
            for (int i = start; i < n; i++) {  
                if(powerMod[i] == xValueTarget){ countXValues++; } 
            }               	   	           	           	           	          		      		    	   		    		     	          	       	      	     	   	o     o      o      o      o      o     o    o     o    o   o   o   o   o   	o     	o    	o   ->->->->->->->o->x->o!>o!>o!>o!>o!>o!>o!>o!>o!>o!>o!>o!>o!>o!>o!>o!--$--$--$--$--$--$--$--$--$--$--$--$!!-->!!-->!!-->!!-->!!-->!!-->!!-->!!-->!!-->!!_____}____}____}_____}____}__}__}_____}. $}$}$}$}$}$}}}}}}}}}}}}}}}}/ / / / / / / / / / / . . . x     - - - - - . . . . x         - - - . . ..x---... ... ... ... ... ... ..x....x.x.x...x.x.x.x.x.x..x..x..x..x..x..xx.x.....xxxxxxxxxxxxxxx....##@##@##@##@##@##@##@##@###@@@@@@####@@@@####@@@@@@####@@@@@@@@########@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#@@@@@###@@@@@###@@@@@@@@@@@@@@###@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@###@@@@@@$$$$$$$$$$$$$$$$$$######@@@@@@@@#####@@###@@@@#####@@@@#####@@@@@@@@########@@@@@@@@###@@@@#####@@@@@@######@@###$$######$$#####$$########$$#########################.//././././././././././.,.,.,.,.,.,,,.,,,,,,,,,,,,,,,,,,,,,,,///////////oooooooooooooooooooooo...oooooo......ooooooo..ooooooooooooooooooooooo//////..../////...../////...../////......//////........////////......////////..........////////////.........////////////////............................/////////////////////////////.......//////////////////////////////////////////////////////////////////////............../////////////////////////////////////////////////////////////////////////////////////////////////////////////.....................\\\\\\\\\\