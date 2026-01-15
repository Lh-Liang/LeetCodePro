#
# @lc app=leetcode id=3515 lang=python3
#
# [3515] Shortest Path in a Weighted Tree
#

from typing import List
import sys
sys.setrecursionlimit(10**7)

# @lc code=start
class Solution:
    def treeQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        # Build adjacency list with edge indices for updates
        adj = [[] for _ in range(n+1)]
        edge_map = {}  # maps (min(u,v), max(u,v)) -> (weight, index in edges list)
        for i, (u, v, w) in enumerate(edges):
            adj[u].append((v, w, i))
            adj[v].append((u, w, i))
            edge_map[(min(u,v), max(u,v))] = (w, i)
        
        # parent array and depth for LCA preprocessing
        parent = [0] * (n+1)
        depth = [0] * (n+1)
        dist_from_root = [0] * (n+1)  # distance from root (node 1) to each node
        # We'll also store the edge weight to each node from its parent
        weight_to_parent = [0] * (n+1)
        # Euler tour for segment tree on distances? Actually we need to support updates on edge weights.
        # Since the tree is rooted at 1, the shortest path from root to any node is simply the sum of weights along the unique path.
        # So we need to support updating an edge weight and querying the sum of weights on a path from root to node.
        # This is a classic problem: dynamic tree path sum with edge updates.
        # Since it's a tree rooted at 1, we can use Euler Tour + Segment Tree with Fenwick or Segment Tree for subtree updates?
        # But here updates affect all nodes in the subtree below that edge.
        # Consider an edge (u,v). Suppose u is parent of v. Then updating weight of that edge changes distance from root to all nodes in subtree of v by delta = new_w - old_w.
        # So we need to quickly add delta to all nodes in a subtree. That's range update on Euler tour.
        # So we can do: 
        # - Root the tree at 1.
        # - Compute parent, depth, and order of nodes via DFS. Also compute tin and tout times for each node.
        # - For each node, store its distance from root initially.
        # - For updates: if we update edge (u,v), determine which node is child (the one deeper). Then add delta to all nodes in subtree of child.
        # - For query of distance to x: simply return dist_from_root[x] after updates.
        
        # Step 1: DFS to compute parent, depth, tin, tout, and initial distances.
        tin = [0] * (n+1)
        tout = [0] * (n+1)
        timer = 0
        
        stack = [(1, 0, 0)]  # node, parent, distance from root so far
        while stack:
            u, p, d = stack.pop()
            if u > 0:
                # first visit
                timer += 1
                tin[u] = timer
                parent[u] = p
                dist_from_root[u] = d
                depth[u] = depth[p] + 1 if p != 0 else 0
                for v, w, idx in adj[u]:
                    if v != p:
                        weight_to_parent[v] = w
                        stack.append((-v, u, d + w))  # negative for post-order?
                        stack.append((v, u, d + w))
            else:
                u = -u
                tout[u] = timer
        
        # Now we have Euler tour range [tin[u], tout[u]] is contiguous for subtree of u.
        # We need a data structure that supports range add and point query? Actually query is point query: distance of node x.
        # But we need range update on subtree. So Fenwick tree or segment tree can do range add and point query efficiently.
        # Let's use Fenwick tree for range updates and point queries: use BIT with difference array.
        bit_size = n + 5
        bit = [0] * bit_size
        
def bit_add(idx: int, val: int):
on    while idx < bit_size:
on    bit[idx] += valon    idx += idx & -idx
def bit_query(idx: int) -> int:
on    res = 0on    while idx > 0:
on    res += bit[idx]
on    idx -= idx & -idxon    return res
# Initially set BIT to represent initial distances? Actually we can store initial distances in an array and then BIT stores deltas.
on# We'll maintain dist_from_root as initial distances. Then when we update an edge by delta,
on# we add delta to BIT over range [tin[child], tout[child]]. Then query for node x: dist_from_root[x] + bit_query(tin[x]).
on# So initialize BIT with zeros.
on# But wait: initial distances are already computed in dist_from_root. So we don't need to set BIT initially.
on# However we need to map edges to child node. For each edge (u,v), we know which is child (the one deeper). Let's compute child_of_edge array.
onchild_of_edge = {}  # maps edge index -> child node id
for i,(u,v,w) in enumerate(edges):
onif depth[u] > depth[v]:
onchild_of_edge[i]=uonelse:
onchild_of_edge[i]=v   
on# Now process queries:
onanswer=[]for q in queries:
onif q[0]==2:
onx=q[1]
dist=dist_from_root[x]+bit_query(tin[x])answer.append(dist)else:
type,u,v,w_new=q[0],q[1],q[2],q[3]
ekey=(min(u,v),max(u,v))
gold_w,eidx=edge_map[ekey]# determine childch=child_of_edge[eidx]
delta=w_new-gold_wif delta!=0:# update BIT over subtree of chbit_add(tin[ch],delta)bit_add(tout[ch]+1,-delta)# update stored weight in adjacency? Not needed as long as we have gold_w updated in edge_map.edge_map[ekey]=(w_new,eidx)# Also update weight_to_parent? Not necessary because we don't use it after initial dist. But future updates rely on old_w from edge_map; we already updated that.return answer