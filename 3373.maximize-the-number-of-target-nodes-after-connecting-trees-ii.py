#
# @lc app=leetcode id=3373 lang=python3
#
# [3373] Maximize the Number of Target Nodes After Connecting Trees II
#

from typing import List
from collections import defaultdict, deque

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        # First, build adjacency lists for both trees.
        n = len(edges1) + 1
        m = len(edges2) + 1
        
        adj1 = defaultdict(list)
        for u, v in edges1:
            adj1[u].append(v)
            adj1[v].append(u)
        
        adj2 = defaultdict(list)
        for u, v in edges2:
            adj2[u].append(v)
            adj2[v].append(u)
        
        # We need to compute for each node in tree2 the number of nodes that are at even distance from it.
        # Actually, we need to know for each node in tree2: count of nodes in tree2 that are target (even distance) to it.
        # But note: after connecting a node i from tree1 to a node j from tree2, the total target nodes for i becomes:
        #   (number of nodes in tree1 that are target to i) + (number of nodes in tree2 that are target to j)
        # Because the path from i to any node in tree2 goes through the added edge (i-j). The parity of the path length is:
        #   distance(i, x) [in tree1] + 1 (for edge i-j) + distance(j, y) [in tree2]
        # For node y in tree2 to be target to i, we need this sum to be even.
        # Since distance(i,x) parity is known (if x is target to i within tree1), but we are adding a whole new set of nodes from tree2.
        # Actually, we can think: after connecting i to j, the set of target nodes for i includes all nodes y in tree2 such that:
        #   (dist_tree1(i,i)=0) + 1 + dist_tree2(j,y) is even => 1 + dist_tree2(j,y) even => dist_tree2(j,y) odd.
        # Wait: but note that a node is target to itself. So for node i itself, it's always target. But when we consider nodes in tree2,
        # we have to consider the path from i to y. That path includes edge (i-j). So parity condition: dist(i,i)=0 + 1 + dist(j,y) = 1+dist(j,y) must be even => dist(j,y) must be odd.
        # Therefore, for each node j in tree2, the number of nodes y in tree2 such that dist(j,y) is odd is the number of nodes from tree2 that become target to i when connecting i to j.
        # However, there is also the nodes in tree1 that remain target? Actually, after adding edge, the distances within tree1 remain same. So nodes x in tree1 are target if dist_tree1(i,x) is even. That's independent of j.
        # So total target nodes for i when connecting to j = count_even_dist_tree1(i) + count_odd_dist_tree2(j).
        # But note: we also have node i itself? It's already counted in count_even_dist_tree1(i). And node j? Node j is not necessarily target because dist(i,j)=1 (odd), so not target unless dist_tree2(j,j)=0 => total parity = 0+1+0=1 odd -> not target. So j is not target. But other nodes in tree2 might be.
        # Therefore, we need two precomputations:
        # For each node i in tree1: cnt_even[i] = number of nodes x in tree1 such that distance(i,x) is even (including itself).
        # For each node j in tree2: cnt_odd[j] = number of nodes y in tree2 such that distance(j,y) is odd.
        # Then answer[i] = cnt_even[i] + max_{j in [0,m-1]} cnt_odd[j]
        # But wait: Is it always optimal to choose j that maximizes cnt_odd? Since cnt_odd[j] is independent of i. So indeed we can precompute max_cnt_odd across all j and add it to each cnt_even[i].
        # However, check example 1: n=5,m=8. Let's compute manually? The answer given: [8,7,7,8,8]. If our formula holds:
        # We need cnt_even for each node in tree1 and max cnt_odd from tree2.
        # Let's compute quickly? Might match.

        # But wait: There might be a nuance: When connecting i to j, the path from i to a node x in tree1 still goes only within tree1; no change. So yes.

        # However, there is also possibility that connecting might affect distances between nodes within tree1? No because only one edge added between trees; it doesn't create cycles because trees are separate; adding one edge connects them into a single tree but distances within original trees remain same because any path between two nodes both in tree1 will never use the new edge because using it would go into tree2 and back which would be longer and not used as shortest path? Actually shortest path might go through new edge if it provides shorter route between two nodes both in tree1? But original graph was a complete tree; adding an edge creates exactly one cycle. The shortest path between two nodes both in original tree could possibly go through new edge if it reduces number of edges? However since original graph was already connected as a tree (unique simple path), adding an extra edge creates exactly one cycle; then shortest path might be shorter via new edge? But consider two nodes deep within same branch; going through new edge would require going out to connection point and back; likely longer than direct path unless connection point lies on their direct path? Actually if you connect an arbitrary pair across trees, the new edge adds a bridge between two trees; any two vertices within same original component still have their original unique simple path without using new edge; but now there might be an alternative path using new edge and going through other component and back; but since all edges are unweighted and positive length (each edge length 1), using extra edges will never make a shorter path than original direct unique simple path because you have extra edges. So distances within each original component remain unchanged after adding bridge. Therefore our assumption holds.

        # Thus answer reduces to computing cnt_even[i] for each node i and max_cnt_odd over second graph.

        # How compute cnt_even[i] efficiently? For a given root r, distances parity can be computed via BFS/DFS. Let's root arbitrarily at 0.

        def compute_even_counts(adj, N):
            """returns list even_count where even_count[u] = number of vertices v such that dist(u,v) is even"""
            if N == 0:
                return []
            parent = [-1]*N
            depth = [0]*N
            stack = [0]
            parent[0] = -2  # mark visited differently
            order = []
            while stack:
                u = stack.pop()                order.append(u)                for v in adj[u]:                    if parent[v]==-1:                        parent[v]=u                        depth[v]=depth[u]+1                        stack.append(v)                        subtree_size=[0]*N            even_subtree=[0]*N            odd_subtree=[0]*N                        for u in reversed(order):                subtree_size[u]=even_subtree[u]+odd_subtree[u]+(depth[u]%2==0? ??? ) Wait better approach.                Actually we want total counts per node across whole graph not just subtree.                                We can use re-rooting DP. Let dp_even[u] be number of vertices v such that dist(u,v) even (including u). Similarly dp_odd[u]. Then dp_even[root]=number_of_nodes_at_even_depth_from_root?? Not exactly because distance parity between root and any vertex equals depth parity. So dp_even[root]=count_of_nodes_with_depth%2==depth[root]%2? Actually root depth=0 (even). So all vertices with even depth are at even distance from root; those with odd depth are odd distance. So dp_even[root]=num_even_depth_nodes where depth%2==0; dp_odd[root]=num_odd_depth_nodes where depth%2==1.                Then when moving from parent p to child c via an edge (p,c), what happens?                For dp_even[c]: consider all vertices v. If v == c -> distance 0 -> even so contribute 1.                For any other vertex v:                  - If v lies inside subtree rooted at c (including c), then distance(c,v)=distance(p,v)-edge(p,c)? Not exactly; because moving down adds one extra edge compared to p->v if v is descendant; else moving up adds one extra edge compared p->v if v outside subtree?                  Actually standard re-rooting DP for sum distances works differently; but here we only care parity changes per edge crossing.                  A known property: flipping parity across an edge because adding one changes parity. So when moving from p->c across an edge:                    For all vertices w inside subtree rooted at c (including c), distance(c,w)=distance(p,w)-edge(p,c)=distance(p,w)-1 => parity flips compared to distance(p,w).                    For all vertices w outside subtree rooted at c (i.e., rest of graph), distance(c,w)=distance(p,w)+edge(p,c)=distance(p,w)+ => also flips parity compared to distance(p,w)? Wait careful: If w outside subtree rooted at c means w not descendant of c but could be anywhere else including ancestors or other branches. The shortest path from c->w goes through p then from p->w without going back into subtree again because no cycles. So indeed distance(c,w)=distance(p,w)+edge(p,c). Thus parity flips as well because adding one flips parity! Therefore crossing any single edge flips parity relative to parent?                  Thus dp_even[c] should equal dp_odd[p]?? Not exactly because total counts change due to inclusion/exclusion?                  Let's derive properly:                  Let S_c_in denote set of vertices inside subtree rooted at c (including c). Let S_c_out denote rest vertices outside subtree rooted at c (including p and others). Then:                  For any vertex v_in ∈ S_c_in : dist(c,v_in)=dist(p,v_in)-edge(p,c)=dist(p,v_in)- => parity opposite relative to dist(p,v_in).                  For any vertex v_out ∈ S_c_out : dist(c,v_out)=dist(p,v_out)+edge(p,c)=dist(p,v_out)+ => also opposite relative to dist(p,v_out).                  Therefore overall every vertex's parity relative changes when moving across an edge! That means dp_even[c]=dp_odd[p]. Because all vertices' distances flip parity when moving from p->c by exactly one unit change (+/- same effect?). Indeed since every vertex either gets + or - but modulo 2 both operations flip parity! Therefore yes!                  However note that dp_even[p] includes vertex p itself with distance zero which is even; then moving to child c makes distance(c,p)=edge(c,p)=which has odd length so p becomes odd relative c; similarly all other vertices flip.                  Therefore dp_even[c]=dp_odd[p]; similarly dp_odd[c]=dp_even[p]. This seems too trivial! Let's test with small linear chain root at end: Tree with three vertices A-B-C where A root depth0(even), B depth(odd), C depth(even). Then dp_even[A]: distances A-A(0), A-C(?) Actually A-C via B length 2 ->even -> includes A,C => count=2 ; dp_odd[A]=count B=> count= . Now move from A->B child . According formula dp_even[B]=dp_odd[A]= which should equal ? Compute manually distances B-B(0), B-A(?),B-C(?); B-A length ; B-C length . Distances B-A= ,B-C= . Both length ? . Actually B-A= ,B-C= ; both odd lengths? Wait A-B length , B-C length ; so B-A length ,B-C length . Both odd lengths! So only B itself has even distance zero -> thus dp_even[B]= . That matches dp_odd[A]= . Good!                                Therefore re-rooting DP works simply by swapping counts per child! Great!                                Steps:                 - Choose arbitrary root r , compute initial depth parities via DFS/BFS.                 - Count num_nodes_with_depth% == ; let total_nodes=N                 - Set root counts: dp_even[r]=count_of_nodes_with_depth%==depth[r]%== ? Since depth[r]== , so count_of_nodes_with_depth%== . Similarly dp_odd[r]=total-dp_even[r].                 - Then perform DFS re-rooting where when moving from parent p with counts(e_p,e_o_p?) Wait need both counts for parent before transition?                   We have computed initial counts only at root using depths parities based on root r . To propagate children counts correctly using relation above we need both e_p and o_p known before computing child counts. Starting with root known values e_r , o_r . Then for child c adjacent parent p , we set e_c=o_p , o_c=e_p . Because every vertex flips parity relative parent due crossing single edge as argued above regardless whether inside or outside subtree!                   This holds irrespective orientation because adjacency undirected relation symmetrical but directed as parent-child relationship defined by DFS spanning TREE rooted r . Since the underlying graph is a TREE indeed this holds globally! Because there exists unique simple paths between any two vertices and crossing one particular directed parent-child branch will affect all paths equally flipping parity due added/removed unit as argued earlier for entire set! Good!                   Therefore we can compute e_c based on e_p and o_p without needing subtree sizes etc!
r                 - Implementation: first run DFS/BFS starting root r get adjacency order with parents list & children list etc.; then compute initial e_r & o_r based on depths parities relative r ; then perform second DFS passing down e_parent & o_parent recursively computing children's values using above swap rule!
r                 
r                 Complexity O(N+M)"
r            """
r            N=len(adj)
r            if N== : return []
r            visited=[False]*N            parent=[- ]*N            depth=[ ]*N            stack=[ ]   choose as root visited[ ]=True while stack not empty... let's use iterative DFS simpler with adjacency list already built.
r Instead let’s use deque BFS ensure depths correct quickly but also need children ordering later re-rooting could use same order reversed etc.. Let’s do BFS first get depths & parents array plus build children lists maybe not needed since we just need pass down values once along edges direction defined by parent relationship anyway recursively propagate using adjacency while skipping parent id avoid revisiting back up during second pass easily done via recursion or stack again using knowledge who parent was earlier recorded during first traversal whichever easier implement Python recursion may exceed recursion limit given up-to ^5 maybe okay default recursion limit ^4 too small might cause RecursionError safer use iterative stacks indeed.. Okay plan steps more concretely later implement now code accordingly.."""