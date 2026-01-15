#
# @lc app=leetcode id=3414 lang=python3
#
# [3414] Maximum Score of Non-overlapping Intervals
#

from typing import List

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        # Sort intervals by end point, then start, then weight? Actually we need to consider lexicographically smallest indices.
        # We'll keep original indices.
        indexed = [(l, r, w, i) for i, (l, r, w) in enumerate(intervals)]
        # Sort by end point ascending, then start ascending, then weight descending? Actually we need to later choose up to 4 intervals.
        # For DP we need sorted by end to find previous non-overlapping interval.
        indexed.sort(key=lambda x: (x[1], x[0], -x[2]))
        # Extract sorted lists
        starts = [x[0] for x in indexed]
        ends = [x[1] for x in indexed]
        weights = [x[2] for x in indexed]
        indices = [x[3] for x in indexed]  # original index
        # Precompute prev[i]: index of last interval that ends before start of i (non-overlapping)
        prev = [-1] * n
        for i in range(n):
            # binary search for rightmost interval with end < starts[i]
            lo, hi = 0, n-1
            while lo <= hi:
                mid = (lo + hi) // 2
                if ends[mid] < starts[i]:
                    lo = mid + 1
                else:
                    hi = mid - 1
            prev[i] = hi  # hi is the last index with end < starts[i]
        # DP: dp[i][k] = max total weight using first i intervals (sorted by end) and selecting at most k intervals.
        # We need up to 4 intervals. So k from 0 to 4.
        K = 4
        dp = [[0] * (K+1) for _ in range(n+1)]
        # parent array to reconstruct indices. We'll store for each dp[i][k] the previous state and whether we took interval i-1.
        parent = [[(-1, -1)] * (K+1) for _ in range(n+1)]  # (prev_i, prev_k) if we didn't take; else if we took, store something.
        # Actually we need to reconstruct the chosen indices. We'll store a tuple (prev_i, prev_k, taken) maybe.
        taken = [[False] * (K+1) for _ in range(n+1)]
        
        # dp[0][*] is 0. For i from 1 to n:
        for i in range(1, n+1):
            idx = i-1  # zero-based index in sorted list
            p = prev[idx] + 1  # number of intervals before that are non-overlapping? Actually prev[idx] is index in sorted list; we want number of intervals considered before that.
            # Since dp is defined on first i intervals (sorted), we can consider taking interval idx or not.
            for k in range(0, K+1):
                # Option 1: skip interval idx
                best_val = dp[i-1][k]
                best_parent_i = i-1
                best_parent_k = k
                best_taken = False
                # Option 2: take interval idx if k >= 1
                if k >= 1:
                    val_take = weights[idx] + dp[p][k-1] if p >= 0 else weights[idx]
                    if val_take > best_val or (val_take == best_val and self.compare_sequences(parent, taken, p, k-1, best_parent_i, best_parent_k)):
                        best_val = val_take
                        best_parent_i = p
                        best_parent_k = k-1
                        best_taken = True
                dp[i][k] = best_val
                parent[i][k] = (best_parent_i, best_parent_k)
                taken[i][k] = best_taken
        
        # Now find the maximum weight among dp[n][k] for k from 0..4. But we need at most 4 intervals. So we find max over all k.
        max_score = -1
        best_k = -1
        for k in range(K+1):
            if dp[n][k] > max_score:
                max_score = dp[n][k]
                best_k = k
            elif dp[n][k] == max_score and self.compare_sequences(parent, taken, n, k, n, best_k):
                max_score = dp[n][k]
                best_k = k
        
        # Reconstruct chosen indices lexicographically smallest.
        chosen_sorted_indices_list = []
        cur_i, cur_k = n, best_k
        while cur_i > 0:
            if taken[cur_i][cur_k]:
                idx_in_sorted = cur_i - 1
                chosen_sorted_indices_list.append(indices[idx_in_sorted])  # original index
                cur_i, cur_k = parent[cur_i][cur_k]
            else:
                cur_i, cur_k = parent[cur_i][cur_k]
        chosen_sorted_indices_list.reverse()
        return chosen_sorted_indices_list[:best_k]
error: name 'self' is not defined in compare_sequences call. Actually I need to define a helper function inside class. Also compare_sequences logic: when scores are equal we need lexicographically smallest list of indices. But our reconstruction might not guarantee lexicographically smallest because DP might have multiple ways. We need to ensure DP picks lexicographically smallest sequence when scores tie. We can modify DP transition to prefer lexicographically smaller sequence when weight equal. How? When taking an interval and weight equal to skipping case or other options, we need to compare sequences. Instead of storing sequences each time which is heavy O(k), we can define order: lexicographically smallest means smaller indices earlier? Wait: The output is array of indices from original intervals list. Lexicographically smallest means compare two arrays element by element; smaller first element wins. Since indices are unique integers from 0..len-1.We want the sequence of indices sorted? Actually the output order? The problem says "Return the lexicographically smallest array of at most 4 indices from intervals with maximum score". The array is the list of chosen indices; they don't have to be sorted? Usually they mean list of indices sorted ascending? Example outputs: Example 1 output [2,3]. That's ascending order because they chose intervals with indices 2 and3 which are increasing after sorting? In example2 output [1,3,5,6], also ascending order. So likely they mean the list of chosen indices sorted ascendingly because non-overlapping intervals may be selected out of order but they probably want the indices sorted ascendingly as a set representation. Lexicographic comparison on sorted list makes sense.Thus our reconstruction currently gives sorted indices because we reconstruct from earliest to latest based on sorted order by end time? Wait we added original indices and later reversed them; they will be in increasing order of original index? Not necessarily; because sorting by end time may reorder original indices. So when we reconstruct we get the original indices but not necessarily sorted ascendingly. However the DP ensures that selected intervals are non-overlapping and ordered by increasing end time because we processed them sorted by end time; but their original indices could be any order. For lexicographically smallest array of indices (when comparing arrays), we want the sequence sorted ascendingly because that's natural representation of set? But example shows exactly that: they return increasing order.Thus after reconstruction we should sort the list ascendingly? But careful: If two different sets have same total weight but different orders of indices when sorted ascendingly produce different lexicographic ordering; e.g., set {2} vs {3} -> [2] vs [3]; obviously [2]. So our DP must choose set with smaller minimal index when tie? Actually lexicographic comparison on sorted arrays is equivalent to comparing sets via their sorted representation.We can incorporate this tie-breaking into DP by preferring selection of intervals with smaller original index when weight equal? Not exactly because it's about whole set ordering.Simpler approach: Instead of DP that tracks only up to K intervals and tries tie-breaking during transition which is messy but possible via storing additional information like the sequence itself limited length <=4 so maybe store as tuple? Since K=4 small and n up to 5e4 but storing tuple per state would be O(n*K*4) which might be okay? Actually each state stores a tuple of up to K integers; memory ~5e4*5*4*8 bytes ~8MB maybe okay but overhead high.Alternative: After computing maximum score via DP without tie-breaking; then do a second pass reconstruction using greedy tie-breaking with lexicographic order: among all optimal solutions reconstruct one that yields lexicographically smallest sequence. This can be done by backtracking and choosing earliest possible index whenever there is choice between equivalent scores.We can modify DP transition to store not only weight but also the sequence as a tuple length up to K; but comparing tuples lexicographically is straightforward; however Python tuple comparison works elementwise as desired.Given K=4 small and n up to5e4; storing tuple per state may be acceptable memory wise but might cause TLE due to many tuple copies? Let's approximate: number states ~5e4*5=250k tuples each length up to4 => about250k*4 ints ~800k ints ~6MB plus overhead maybe okay within limits?But Python overhead per tuple significant; each tuple object has overhead ~56 bytes plus references => could blow memory maybe not too bad but risk TLE due copying tuples during DP transitions O(nK). However there are only O(nK) transitions each copying at most K elements -> O(nK^2)=~5e4*16=800k operations fine.I'll implement using storing sequence directly as list stored as tuple for immutability.Let's redesign DP:Define f[i][k]: pair (max_weight_best_sequence_tuple) where sequence_tuple contains up to k original indices in increasing order?Actually since our DP processes intervals in sorted order by end time; when taking an interval idx (original index orig_idx), its index may be larger or smaller than previous ones depending on ordering. To maintain increasing order after reconstruction we can store sequences as tuples already sorted ascendingly because later added index will always be greater than previous ones if previous ones were selected from earlier processed intervals? Not necessarily because sorting by end time may reorder original indices arbitrarily; e.g., an interval with earlier start but later end could have larger original index than another interval with later start but earlier end? Original index unrelated. So adding new orig_idx may break monotonicity if inserted into sequence unsorted.Thus after constructing set S of selected original indices via reconstruction (list unsorted), I will sort S before returning; but that might change lexicographic comparison because sorting changes representation; however output requires array of at most four indices representing your choice—the array likely expected sorted ascendingly as per examples—so sorting final result ascendingly seems correct regardless internal order.Therefore I can just store total weight and during reconstruction I collect unsorted list then sort before returning—but tie-breaking must consider sorted representation across different solutions! If two solutions yield same total weight but different sets whose sorted representations differ lexicographically; my final sorting would produce one representation each; I need choose solution whose sorted representation is lexicographically smallest overall among all optimal solutions! Sorting after reconstruction doesn't help choose between multiple optimal sets! So I must incorporate tie-breaking into DP such that when weights equal I prefer set whose sorted representation is smaller lexicographically—which essentially means prefer sets with smaller minimal index etc.—but easier way: After constructing all optimal sets via backtracking search limited depth <=4 maybe feasible via recursion exploring choices—but n large so not feasible enumerating all combos!Thus better incorporate tie-breaking into DP directly using stored sequences as tuples already sorted ascendingly—but again adding new orig_idx may break monotonicity unless I insert it into correct position while maintaining sort order—but then sequence may no longer correspond strictly to processing order—but still can compute transition taking previous sequence from p and inserting new orig_idx into appropriate position preserving increasing order—then compare sequences directly via Python's tuple comparison which does lexicographic compare exactly what needed!This works! Complexity per transition O(K). Good!Let's implement:f[i][k]: pair (max_weight_best_sequence_tuple). Initialize f[0][*]= (0 empty_tuple). Then iterate i from0.. n-1?We'll use zero-based indexing for convenience maybe easier using array size n+11 where f[0]=base case no intervals considered yet . Actually let’s define f[i+11]=best considering first i+11 intervals after sorting . Better use same approach as earlier but store sequences directly . We'll have arrays dp_weight[n+11[k]]and seq[n+11[k]]as tuple . But updating seq requires copying tuple possibly expensive but K<=4 fine . Let’s code accordingly .