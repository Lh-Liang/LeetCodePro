#
# @lc app=leetcode id=3743 lang=python3
#
# [3743] Maximize Cyclic Partition Score
#

# @lc code=start
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if k == 1:
            return max(nums) - min(nums)
        
        # Since it's a cyclic array, we can flatten it by appending nums to itself.
        # However, to avoid O(N^2 K), we need a smarter approach or realize N is small enough for optimized DP.
        # With N=1000, O(N^2) is acceptable (10^6). O(N^2 K) is not.
        
        # Let's fix the start point. Since we want to partition the cycle into at most k parts,
        # there must be a boundary between two subarrays. There are n possible boundaries.
        # If we cut the cycle at index i (making it a linear array starting at i), 
        # we solve the linear partition problem.
        # Doing this for all i is too slow.
        
        # However, notice that we only need to split the cycle ONCE to make it linear. 
        # Any valid partition has at least one boundary. 
        # Actually, if we just solve the linear problem on nums + nums (length 2n)
        # and look for a solution that uses exactly length n with at most k partitions?
        # That is also tricky.
        
        # Let's reconsider the structure. We typically fix the first split.
        # Is there a split that is 'safe' to assume? No.
        
        # But wait, do we really need to run the DP for ALL shifts? 
        # No. We can just run the DP on the doubled array `nums + nums` of length `2n`.
        # We want to find a chain of subarrays $S_1, S_2, ..., S_m$ ($m \le k$) such that 
        # they cover a range of exactly length $n$ (i.e., from index $i$ to $i+n-1$).
        # 
        # Let $dp[i]$ be the max score of partitioning a prefix ending at $i$ using some number of parts.
        # But we need to track the number of parts. $dp[k][i]$.
        # This is essentially finding a path of length at most $k$ edges in a DAG where nodes are $0..2n$
        # and edge $u \to v$ has weight $range(nums[u:v])$. We want a path from $i$ to $i+n$.
        
        # Since we just need *one* valid start $i$, and we want to maximize the score,
        # maybe we can just compute for all $i$ efficiently?
        
        # Actually, for N=1000, O(N^2) is fine. Can we solve the linear version in O(N^2) independent of K?
        # Let $f[i]$ be the max score for prefix $i$ with *any* number of partitions? No, K matters.
        # 
        # Let's look at the constraints again. N=1000. 
        # What if we assume the split is at index 0? We get a candidate answer.
        # What if the optimal answer wraps around index 0? Then index 0 is inside some subarray.
        # That subarray must have a start $s$ and end $e$ in the cyclic sense.
        # In the linear view of `nums + nums`, this corresponds to a subarray covering index $n$ (or $0$ and $n$).
        # 
        # Let's try a randomized approach or heuristics? No, hard problem requires exactness.
        # 
        # Let's observe: if we partition into $m$ subarrays, we make $m$ cuts.
        # At least one cut must occur within every $n/k$ elements? Not really.
        # But we can iterate over the position of the *first* cut. 
        # If we fix the first cut to be at index $i$, we are solving the linear problem for `nums[i:] + nums[:i]` with $k$ parts.
        # If we try ALL $i$, it's too slow. 
        # BUT, we don't need to try all $i$. We only need to try enough $i$ to ensure one of them is a valid cut in the optimal solution.
        # In an optimal solution with $m$ parts ($1 < m \le k$), there are $m$ cuts.
        # These cuts are distributed. The distance between consecutive cuts is at least 1.
        # By Pigeonhole Principle, or just simple logic, if we pick a set of indices $S$ such that every possible interval of length greater than something contains a point from $S$, we might hit a cut.
        # Actually, simply: In the optimal solution, there is at least one subarray. 
        # If we iterate through all possible *first* subarrays that start at index 0 (length 1 to n), 
        # and for each, we solve the remaining problem? That's still slow.
        
        # Wait, there's a simpler logic. 
        # Maximize range sum. 
        # If $k=1$, trivial.
        # If $k \ge 1$, we can just try to cut at index 0. This covers all cases where index 0 is a boundary.
        # What if index 0 is NOT a boundary? Then index 0 is strictly inside a subarray $S_{wrap}$.
        # $S_{wrap}$ starts at $i$ (in `nums`) and ends at $j$ (in `nums`), wrapping.
        # In `nums + nums`, this is a subarray starting at $i$ and ending at $j+n$ (if $j<i$).
        # The length of this wrapping subarray is $L$. Since we have at most $k$ subarrays, and total length is $n$,
        # does this constrain $L$? Not necessarily, $L$ could be near $n$.
        # BUT, if we consider all possible 