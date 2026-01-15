#
# @lc app=leetcode id=3615 lang=python3
#
# [3615] Longest Palindromic Path in Graph
#

from typing import List
from collections import defaultdict, deque

# @lc code=start
class Solution:
    def maxLen(self, n: int, edges: List[List[int]], label: str) -> int:
        # Build adjacency list
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # Since n <= 14, we can use bitmask DP.
        # We want the longest palindrome that can be formed by a path (simple path).
        # We can think of DP[mask][i][j] = whether we can form a palindrome using nodes in mask,
        # with i and j being the two ends of the path (or same node if odd length).
        # But storing all masks and pairs is expensive: 2^14 * 14 * 14 = 2^14 * 196 ≈ 16k * 200 = 3.2M, which is okay.
        # However we need to know the palindrome string? Actually we only care about matching characters.
        # The palindrome condition: For a path, the sequence of labels must be a palindrome.
        # If we have a path with nodes v1, v2, ..., vk, then label[v1] == label[vk], label[v2] == label[vk-1], etc.
        # We can model DP as: dp[mask][i][j] = True if there exists a path using exactly nodes in mask,
        # with i and j as endpoints, and the sequence of labels along the path forms a palindrome.
        # Then we can extend by adding new nodes to either end.
        # Base case: mask with single node i: dp[1<<i][i][i] = True.
        # Also mask with two nodes i and j if there is an edge and label[i]==label[j]: dp[mask][i][j] = True.
        # Then transition: For a given dp[mask][i][j] = True, we can extend by adding node u adjacent to i (and not in mask)
        # provided label[u] == label[j]? Wait careful: The palindrome condition: when we extend at one end, we need to match the other end.
        # Actually think of building palindrome from both ends. Let the current path be from i to j, with internal nodes forming a palindrome.
        # Then if we add node u to the i side (new start), and node v to the j side (new end), we need label[u]==label[v].
        # But our DP only stores two endpoints. So when extending only one side at a time, we need to know the other endpoint that matches?
        # Alternative approach: Use DP on subsets for paths but also store the multiset of characters? Too complex.
        
        # Better approach: Since n is small (<=14), we can brute force all simple paths? Number of simple paths could be huge but maybe manageable? 
        # For complete graph, number of simple paths is exponential. But n=14, worst-case number of Hamiltonian paths is 14! ≈ 87B too big.
        
        # Let's think differently. We want longest palindrome subsequence along a path? Actually it's contiguous along the path.
        # So it's essentially finding a simple path whose node labels read in order form a palindrome.
        # This is similar to finding longest palindromic path in an undirected graph. This is NP-hard? But n <= 14 allows exponential solutions.
        
        # We can use meet-in-the-middle? Or BFS over states (mask, i, j) as described.
        
        # Let's implement DP[mask][i][j] as described. But note that the palindrome condition must hold for the entire path.
        # How to ensure that when extending from dp[mask][i][j], the new node added to i side must match the character at the other end?
        # Actually if we have a palindrome path from i to j, then extending on i side with node u (adjacent to i) requires that label[u] equals label[some node at symmetric position]. That symmetric position is currently j? Not necessarily; because if we add u at start, then new start becomes u, new end remains j. For the new path u -> ... -> j to be palindrome, we need label[u]==label[j] and also the inner part (original i...j) must be palindrome. But original dp[mask][i][j] already ensures inner part is palindrome. So condition: label[u]==label[j]. Similarly extending on j side with v requires label[i]==label[v].
        
        # So transitions:
        # If dp[mask][i][j] is True:
        #   For each neighbor u of i not in mask:
        #       if label[u]==label[j]:
        #           new_mask = mask | (1<<u)
        #           dp[new_mask][u][j] = True
        #   For each neighbor v of j not in mask:
        #       if label[i]==label[v]:
n#           new_mask = mask | (1<<v)
n#           dp[new_mask][i][v] = True
# However note that when extending from both ends simultaneously? Actually you can extend one at a time; eventually you might add nodes on both ends.
n# Also note that for odd-length palindromes, i==j; for even-length, i!=j.
n# Base cases:
n# Single node: dp[1<<i][i][i]=True
# Two nodes with edge and same label: dp[mask][i][j]=True where mask has bits i and j set.
n# Then run BFS/DP increasing mask size.
n# Complexity: O(2^n * n^2 * deg) but deg up to n; overall O(2^n * n^3). With n=14: 2^14=16384; n^3=2744; product ~45M which is okay in Python maybe borderline but acceptable given constraints small and many masks unreachable.
n# We'll store dp as dictionary keyed by (mask,i,j) or use 3D list boolean.
n# Let's implement using BFS over states; start from all base states and expand until no more states.
n
# Implementation steps:
n# Build adjacency list adj
# Initialize dp as dictionary or set of tuples (mask,i,j)
n# For each node i: add state (1<<i,i,i)
n# For each edge (u,v): if label[u]==label[v]: add state ((1<<u)|(1<<v), u,v) and also symmetric state? Since undirected, path from u to v same as v to u? Our DP state includes ordered endpoints? Actually our DP state uses unordered endpoints because when extending we consider neighbors of either endpoint. However our transition uses neighbors of i and neighbors of j separately. If we store both orders? Let's store unordered but treat endpoints as ordered pair? We'll store both orders because extending from i side vs j side matters. So store both (mask,i,j) and (mask,j,i)? Actually our transitions are symmetric; if we have state (mask,i,j), then extending from i side requires matching label[j]; extending from j side requires matching label[i]. If we also have state (mask,j,i), it would be redundant because it's same set of nodes but reversed direction. However when extending from i side in state (mask,i,j), it corresponds to adding node before i; while in reversed state it would be adding after j? The palindrome condition doesn't care about direction because graph undirected. So storing one order is enough provided we treat endpoints as ordered pair where first endpoint is 'left' and second 'right' relative to palindrome construction. Actually our construction builds palindrome by adding nodes symmetrically around center. So storing order matters because when extending left side we compare with right endpoint's char. So if we have state (mask,i,j) meaning current left endpoint is i and right endpoint is j (path from left to right reads forward). Then adding node u left of i requires label[u]==label[j]. Adding node v right of j requires label[i]==label[v]. That's fine. If we reverse order (mask,j,i), then left endpoint becomes j and right becomes i; then adding left would require matching right char which is original i char etc. So both orders are essentially equivalent but might lead to different extensions because adjacency might differ. However since graph undirected, adjacency symmetric; so having both orders might help simplify code but not necessary if we always consider neighbors of both endpoints regardless of order? Actually our transition already considers neighbors of both endpoints separately. So storing only one order per unordered pair should suffice because when considering extension on 'left' endpoint we look at neighbors of whichever endpoint we designate as left; but if we only store one arbitrary order for each unordered pair, then extension on 'right' endpoint might be missed if that endpoint was designated as left? Wait our transition uses both sides anyway regardless which is left/right? In our transition above for state (mask,i,j) we consider neighbors of i and neighbors of j separately. So it covers both sides regardless whether we call them left/right. So storing only one order per unordered pair should work because extension from either endpoint is considered independently based on matching character with opposite endpoint. However note that when extending from endpoint i, we compare with character at j; when extending from endpoint j compare with character at i. That's exactly what our transition does regardless of ordering. So no need for symmetric duplicate states.
n
# But careful: When mask contains only two nodes {u,v}, there are two possible states: (mask,u,v) and (mask,v,u). Both represent same set but different ordering; however they are distinct states because they differ in which endpoint is considered first/second. Are they both needed? Consider starting base case for two nodes: suppose edge between u,v with same label; then state (mask,u,v) means left=u right=v; now you could extend left side by adding neighbor w adjacent to u such that label[w]==label[v]; similarly extend right side by neighbor adjacent to v such that label[u]==label[w']. If you only have one ordering say always store smaller index first? Then you might lose ability to extend from v side because your designated left endpoint might be smaller index but you need extension from larger index side depending on adjacency. However since our transition considers neighbors of both endpoints regardless which is first/second, having only one ordering still allows extension from both sides! Because state (mask,u,v) has endpoints u and v; transition checks neighbors of u AND neighbors of v separately. So it doesn't matter which you call left/right; it checks both endpoints equally. Therefore storing only one ordering per unordered pair suffices.
n
# To avoid duplicate work let's decide canonical ordering like i <= j for base cases where mask size >=2? But actually when mask size >2 there may be multiple ways to assign endpoints leading to same unordered pair but different internal ordering matters for future extensions because internal structure matters for palindrome condition beyond just endpoints? Our DP state assumes that given mask and endpoints i,j there exists some ordering internal nodes such that entire sequence forms palindrome consistent with those endpoints being outermost positions along path direction relative to reading order from one end to other end?
n
# Wait important subtlety: The DP definition I proposed may not guarantee full palindrome condition except at outermost characters matched each step during building process ensures overall palindrome due to induction base cases being palindromes themselves single char or two same chars plus each extension adds matching outer characters while inner part remains palindrome indeed ensures whole remains palindrome by construction similar to building palindromic string symmetrically using insertions at ends requiring matched characters each time ensures final string reads same forwards backwards . That's correct . Therefore our transitions ensure any reachable state corresponds to some simple path whose labels form palindrome . And any such palindrome path can be built by iteratively adding matched pairs outward starting from center or single char . Thus DP captures all possibilities . Good .
n
Now implementation details :
mask up to 14 bits ; use integer bitmask . Use dictionary mapping mask -> set of tuples(i,j) where dp[mask][i][j]=True . Or use list : dp[mask][i*n+j]=bool . Since n small , use list comprehension . Let's create dp array size [1<<14]*[14]*[14] boolean ; allocate memory about 16384*196 ≈ 3 million booleans ; okay . Use list comprehensions . But many masks may not be used ; still manageable . Use array('b') or just list comprehension .
nWe'll initialize all False ; set base cases ; then iterate over masks increasing size or BFS style queue . Because transitions always add exactly one new node , so masks increase by one bit ; so iterate over masks in increasing order number bits works fine . Use BFS queue maybe simpler : queue containing tuples(mask,i,j); visited set prevent reprocessing same state . Start queue all base states . While queue pop , try extensions on both sides ; push new states if not visited . Keep track maximum length computed as number bits set in mask ; update answer accordingly .
nComplexities : number states reachable limited ; each state processed once ; each tries up deg(i)+deg(j) extensions ; total operations manageable .
nEdge Cases : single node answer at least 1 always possible ; ensure answer initialized as 1 . Also handle disconnected graphs etc .
nNow let's code accordingly ."","code": """\","code": "\"\","code": "\"\"\","code": "\"\"\"\","code": "\"\"\"\"\","code": "\"\"\"\"\"\","code": "\"\"\"\"\"\", I'll write clean code now.