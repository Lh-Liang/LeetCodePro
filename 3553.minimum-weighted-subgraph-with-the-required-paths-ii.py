#
# @lc app=leetcode id=3553 lang=python3
#
# [3553] Minimum Weighted Subgraph With the Required Paths II
#

# @lc code=start
from typing import List
import math

class Solution:
    def minimumWeight(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        n = len(edges) + 1  # edges length is n-1
        # Build adjacency list
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        
        # Preprocess LCA and path weights
        LOG = (n).bit_length()
        parent = [[-1] * n for _ in range(LOG)]
        depth = [0] * n
        # weight_up[u][k] is sum of weights from u up 2^k steps (excluding the weight of the edge from u to parent)
        weight_up = [[0] * n for _ in range(LOG)]
        
        # DFS to build parent[0] and depth
        stack = [(0, -1, 0)]  # node, par, dep
        while stack:
            node, par, dep = stack.pop()
            if node >= 0:
                # first visit
                parent[0][node] = par
                depth[node] = dep
                stack.append((~node, par, dep))
                for nei, w in adj[node]:
                    if nei == par:
                        continue
                    weight_up[0][nei] = w
                    stack.append((nei, node, dep + 1))
            else:
                node = ~node
                # post-order if needed
                pass
        
        # Build binary lifting tables
        for k in range(1, LOG):
            for i in range(n):
                mid = parent[k-1][i]
                if mid != -1:
                    parent[k][i] = parent[k-1][mid]
                    weight_up[k][i] = weight_up[k-1][i] + weight_up[k-1][mid]
                else:
                    parent[k][i] = -1
                    weight_up[k][i] = weight_up[k-1][i]
        
        def get_path_weight(u: int, v: int) -> int:
            # returns sum of weights on unique path between u and v in tree
            if u == v:
                return 0
            res = 0
            if depth[u] < depth[v]:
                u, v = v, u
            # lift u to same depth as v and add weights
            diff = depth[u] - depth[v]
            k = 0
            while diff:
                if diff & 1:
                    res += weight_up[k][u]
                    u = parent[k][u]
                diff >>= 1
                k += 1
            if u == v:
                return res
            for k in range(LOG - 1, -1, -1):
                if parent[k][u] != parent[k][v]:
                    res += weight_up[k][u] + weight_up[k][v]
                    u = parent[k][u]
                    v = parent[k][v]
            # now u and v are children of LCA; add the two edges to LCA.
            res += weight_up[0][u] + weight_up[0][v]
            return res
        
        # For each query (src1, src2, dest), we need minimal subtree that contains paths from src1->dest and src2->dest.
        # In a tree, the minimal subtree containing these three nodes is the union of paths from each src to dest.	# The total weight is sum of edges in that union.	# Since tree is undirected and paths are unique,	# we can compute sum of edges on path src1->dest plus src2->dest minus edges common to both.	# The common edges are exactly the edges on path from LCA(src1,src2,dest) to dest? Actually need intersection.	# Let's think: union of two paths from A to C and B to C. The union is path A->C plus path B->C minus the intersection (common part).	# The intersection is the path from LCA(A,B,C) to C? Actually the common part is from the meeting point (the deepest node that lies on both paths) to C.	# In a tree, that meeting point is the LCA of A,B with respect to C? Let's define LCA(A,B) but we need consider C.	# The intersection of paths A->C and B->C is the path from LCA(A,B) to C? Not exactly. Example: A and B are on same side of C? Actually because paths are directed towards C.	# Let’s denote X = LCA(A,B). Then path A->C goes up to X then down? Wait tree is undirected. The unique path from A to C may not go through X unless X lies between them.	# Better approach: The minimal subtree containing nodes A,B,C is the Steiner tree with three terminals. In a tree, Steiner tree is just union of paths between pairs. It can be computed as sum of three pairwise distances minus max pairwise distance divided by something? Actually in a tree,
the minimal subtree connecting three nodes is the union of three simple paths between them. Its total edge weight equals (dist(A,B)+dist(B,C)+dist(C,A))/2.	Because each edge in union counted twice? Let's verify: For three nodes A,B,C in a tree,
the union of paths between them forms a subtree where each edge lies on at least one path. The sum dist(A,B)+dist(B,C)+dist(C,A) counts each edge twice if it lies on two paths and three times if on all three? Actually each edge on two paths gets counted twice; edge on all three gets counted three times. But there might be no edge lying on all three because tree has no cycles; but maybe the meeting point is a node. Anyway there's known formula: Steiner tree weight for three terminals in a tree equals (dist(A,B)+dist(B,C)+dist(C,A))/2.	Let's test with example: A=2,B=3,C=4 from Example1. Compute distances: dist(2,3)=? Edges: (0-1:2),(1-2:3),(1-3:5),(1-4:4),(2-5:6). dist(2,3)=3+5=8 via node 1. dist(3,4)=5+4=9 via node 1. dist(2,4)=3+4=7 via node 1? Actually path 2-1-4 => 3+4=7. Sum=8+9+7=24; half=12 matches answer[0]. Good.	Second query (0,2,5): distances: dist(0,2)=2+3=5; dist(2,5)=6; dist(0,5)=2+3+6=11; sum=22 half=11 matches answer[1]. So formula works!	Thus answer for query (src1,src2,dest) is (dist(src1,dest) + dist(src2,dest) + dist(src1,dest? Wait formula uses all three pairwise distances among src1,src2,dest. But we have only two sources and one dest. Actually terminals are src1,src2,dest. So compute d12,d23,d31 where d12 between src1 and src2; d23 between src2 and dest; d31 between dest and src1. Then total weight =(d12+d23+d31)/2.	But note d12 appears which we didn't have directly but we can compute using get_path_weight.	Thus algorithm per query O(log n). Preprocessing O(n log n). Queries up to 10^5 => O(q log n). Good.	Need integer division by 2 because all distances sums even? Indeed each distance sum twice the actual edge weights because each edge counted twice across three pairwise distances? Let's trust formula yields integer."																				\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"We'll implement get_path_weight using binary lifting with cumulative weights."	"Edge cases: ensure root at node 0 works; tree may not be rooted but we arbitrarily root at 0."	"Now code accordingly."