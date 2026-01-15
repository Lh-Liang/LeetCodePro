#
# @lc app=leetcode id=3776 lang=python3
#
# [3776] Minimum Moves to Balance Circular Array
#

# @lc code=start
from typing import List

class Solution:
    def minMoves(self, balance: List[int]) -> int:
        n = len(balance)
        # Find the index of the negative value (if any)
        neg_idx = -1
        for i, val in enumerate(balance):
            if val < 0:
                neg_idx = i
                break
        
        # If no negative value, already balanced (all non-negative)
        if neg_idx == -1:
            return 0
        
        # The negative value is at neg_idx.
        # We need to bring units from other indices to this index.
        # Since we can only transfer 1 unit at a time to left or right neighbor,
        # the cost of bringing a unit from index i to neg_idx is the minimum clockwise distance.
        # In a circular array of length n, distance between i and j is min(|i-j|, n-|i-j|).
        # However, because transfers happen through neighbors, the number of moves required for a unit from i to neg_idx is exactly that distance.
        # The total moves needed is sum over all positive contributions (balance[i] > 0) of balance[i] * dist(i, neg_idx).
        # But wait: we need exactly -balance[neg_idx] units to bring to neg_idx.
        # However, the total sum of balance must be >= 0 for it to be possible.
        total = sum(balance)
        if total < 0:
            return -1
        
        # Actually, we need to ensure that after moving units, all balances are non-negative.
        # Since only one negative exists initially, we can think of it as we need to send enough units to cover that negative.
        # The minimum moves is the sum over all positive indices of (balance[i] * min distance) but only up to the amount needed.
        # However, we may have more positive balance than needed. We can choose which indices contribute.
        # To minimize moves, we should take units from the closest positive indices first.
        # So we need to compute for each positive index its distance to neg_idx (clockwise and anticlockwise).
        # But note: because the array is circular, moving clockwise vs anticlockwise might have different distances.
        # Actually, when transferring from index i to neg_idx, we can choose either direction (left or right) and the number of moves is the minimum distance in terms of steps between them along the circle.
        # So dist(i) = min(|i - neg_idx|, n - |i - neg_idx|).
        
        # We need to select a set of units from positive indices such that total units >= -balance[neg_idx], minimizing sum(units * dist).
        # This becomes a knapSack-like problem? But note: each unit from index i costs dist(i). We can take any number of units from i up to balance[i].
        # This is essentially: minimize sum over i of x_i * dist(i) subject to sum x_i >= needed and 0 <= x_i <= balance[i].
        # Since dist(i) are integers and we have many units (up to 10^9), but n up to 10^5.
        	# This is like a fractional knapsack? Actually each unit from same i has same cost. So we should take units from indices with smallest dist first. That's greedy.													   	   	   	   	   	   	   	   	   	   	   	   	   	   	   	   	   	   	   	   So algorithm:

















1. Compute needed = -balance[neg_idx].2. For each index i where balance[i] > 0:    compute d = min((i - neg_idx) % n, (neg_idx - i) % n)? Actually min(|i-neg_idx|, n-|i-neg_idx|).3. Sort these (d_i, balance_i) by d ascending.4. Iterate through sorted list; take as many as possible from each until needed is met. Add d * taken moves.5. If after iterating needed > 0, return -1 (should not happen because total >=0). But total might be exactly zero? Actually if total >= needed then possible. Since only one negative and total >=0, then total >= needed? Yes because needed = -negative and total = sum positives + negative => sum positives = total - negative >= -negative because total >=0 => sum positives >= needed. So always enough positives.6. Return total moves.But wait: Example 2: balance = [1,2,-5,2]. n=4. neg_idx=2 (-5). needed=5. distances: index0: min(|0-2|=2,4-2=2)=2; index1: min(1,3)=1; index3: min(1,3)=1. Sorted: (d=1 at idx1 with bal=2), (d=1 at idx3 with bal=2), (d=2 at idx0 with bal=1). Greedy: take 2 from idx1 -> moves+=1*2=2; needed now 3; take 2 from idx3 -> moves+=1*2=4; needed now 1; take 1 from idx0 -> moves+=2*1=6; total moves=6 matches example. Good.Example1: [5,1,-4] n=3 neg_idx=2 needed=4 distances: idx0: min(|0-2|=2,3-2=1)=1; idx1: min(1,2)=1. Sorted both d=1. Take first idx0 bal5 but only need4 => moves+=4*1=4 => answer4 matches.Example3: [-3,2] n=2 neg_idx=0 needed=3 distances: idx1: min(|1-0|=1,n-|...|=1)=1 bal2 -> can provide only 2 units <3? But total sum=-3+2=-1<0 so should be impossible. Our check total>=0 will catch that (-1<0) return -1. Good.But what about case where total>=0 but there are multiple positives but not enough? Actually since only one negative and total>=0 then sum positives >= needed as argued above. So always enough.Thus algorithm works?Wait edge case: If there are zero positive balances? Then all non-negative except one negative? Then if negative <0 and others zero? Then total<0 unless negative zero? But if negative then others zero => total<0 so impossible -> check catches it.Another edge case: The negative could be zero? The problem says "at most one index has a negative balance", so could be none or one strictly less than zero. If none negative then already balanced return 0 as earlier handled.Implementation details:We'll compute distances for all indices except the negative one where balance[i]>0. Use list comprehension then sort by distance.Then iterate and accumulate moves until needed becomes zero.Complexities O(n log n) due to sorting worst-case O(n log n) with n up to 10^5 acceptable.Potential overflow? Moves could be large up to sum(balance[i])*dist which could be up to 10^9 *10^5 =10^14 fits in Python int fine.Let's test with some random cases mentally:Case where there are multiple positive indices far away etc greedy works because cost per unit increases with distance so taking closest first optimal indeed like fractional knapsack with integer items where each unit identical cost per source index -> greedy optimal by sorting by cost per unit (distance). Yes it's optimal because we are minimizing linear objective with constraints that we must take at least N units and each source has capacity unlimited up to its balance but same cost per unit within source -> so taking as much as possible from smallest cost sources yields optimum (standard resource allocation).So solution seems correct.