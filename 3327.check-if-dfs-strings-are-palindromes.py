#
# @lc app=leetcode id=3327 lang=python3
#
# [3327] Check if DFS Strings Are Palindromes
#

from typing import List

# @lc code=start
class Solution:
    def findAnswer(self, parent: List[int], s: str) -> List[bool]:
        n = len(parent)
        # Build adjacency list for children, sorted by child index (already increasing order)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            p = parent[i]
            children[p].append(i)
        # We can precompute the Euler tour of the tree (preorder and postorder) but need to generate dfs string for each root.
        # The dfs string for root i is the concatenation of characters of nodes in the subtree of i visited in postorder.
        # Actually, the description: iterate over each child in increasing order, then add s[x] at end.
        # So it's a postorder traversal: process all children recursively, then add current node's character.
        # Therefore, dfs(i) yields the characters of the subtree rooted at i in postorder.
        # So answer[i] is true if the postorder traversal string of subtree i is a palindrome.
        
        # We need to compute for each node the string of its subtree postorder and check palindrome.
        # Directly generating strings would be O(n^2) worst-case. Need efficient method.
        
        # Observation: The postorder string is palindrome if and only if for each pair of symmetric positions, characters match.
        # In postorder, the order is: leftmost subtree's postorder, then next subtree, ..., then root's char.
        # So we can think of the string as concatenation of subtrees' strings plus root char at end.
        # Let subtree size be sz[i]. Then dfsStr length = sz[i].
        # Palindrome condition: for k from 0 to sz[i]-1, dfsStr[k] == dfsStr[sz[i]-1-k].
        
        # We can use hashing to compare characters quickly? But we need to answer for each root individually.
        # Alternative: Use Euler tour to get order and then we can query substring hashes? But we need to generate different strings for each root (different subtrees).
        
        # Another idea: For each node, we can compute its contribution to palindrome checks. Since the string is built recursively, we can use a two-pointer-like approach using DFS order.
        
        # Let's define an array postorder which is the global postorder traversal starting from root 0 (but we need arbitrary roots). Actually, if we fix a global order (like DFS from root 0), then subtree of any node corresponds to a contiguous segment in that order? In postorder, yes: each subtree corresponds to a contiguous segment in the postorder array. However, that's only if we always use same traversal order (children sorted increasingly). For different roots, the traversal order changes because we start at different nodes but still follow same rule (children in increasing order). The relative order within a subtree might be same as global? Let's examine:
        # Suppose we have tree rooted at 0 with children sorted. The global postorder list (from dfs(0)) gives an ordering of all nodes. For any node i, its subtree's nodes appear as a contiguous block in that global postorder list? Actually yes: In DFS recursion, when you process subtree rooted at i, you recursively process its children and then add i. So all nodes in i's subtree are visited consecutively during recursion and appear consecutively in postorder list. Moreover, within that block, the order is exactly the postorder of subtree i. Therefore, if we compute global postorder from root 0 (children sorted), then for any node i, its dfs string when starting from i is exactly the substring of global postorder string corresponding to that contiguous block? Wait careful: The global dfs string from root 0 is built by calling dfs(0). That yields s[0] added after all children. That's not the same as starting from i. However, if we consider only the part corresponding to subtree i within that global traversal: When we call dfs(0), inside it calls dfs(i) as part of processing child i. During that call, it builds the string for subtree i exactly as defined (postorder). So indeed, when we run dfs(0), during its execution when it processes node i as a child somewhere, it calls dfs(i) which builds exactly the same string as if we called dfs(i) standalone. Therefore, there exists a global postorder traversal (starting from root 0) such that for each node i, its standalone dfs string appears as a contiguous substring of that global traversal string? Not exactly contiguous because when we call dfs(0), it interleaves other subtrees? Actually no: When processing child i of some parent p, we call dfs(i) and it processes entire subtree of i before returning and adding p's char later. So during that call to dfs(i), all characters from subtree i are appended consecutively without interruption from other nodes. So yes! If we run dfs(0) and record the order of appending characters (i.e., the sequence of characters as they are added), then for each node i, there is a contiguous segment corresponding to its standalone dfs(i) string. Because when you start dfs(i), you process its entire subtree before returning; no other node's character is added during that time (since recursion is depth-first). Therefore, if we compute one big string T by running dfs(0) (i.e., global postorder), then T can be partitioned into segments corresponding to each node's standalone dfs string? Not exactly partition because overlapping? Actually segments are nested: For node i and its descendant j, segment j is inside segment i. But they are contiguous substrings.

        # Therefore, we can compute an array pos_order where we store for each node its position in T (the index where its character appears). But T is built by appending characters; each node appears exactly once in T at position equal to its finishing time in DFS? Actually each node adds its character exactly once when it finishes processing children. So T length = n. And indeed T is just the postorder traversal sequence of characters when starting from root 0.

        # Now consider standalone dfs(i): It will produce a substring T_i which is exactly T[L_i:R_i] where L_i and R_i are some indices? Let’s denote start index and end index inclusive? Since T contains all nodes' characters once. The standalone dfs(i) will produce characters for all nodes in subtree of i in postorder; that set corresponds exactly to those nodes whose finishing times are within some range? Actually yes: In standard DFS numbering (post-order), finishing times define intervals where subtree nodes form contiguous interval in that numbering. If we assign each node an index 'tin' when entering and 'tout' when leaving (post-order time), then tout gives position in T where its character appears? Wait typical DFS timestamps: pre-order number when entering; post-order number when exiting after processing children. In our case character added after processing children so indeed adding character corresponds to assigning a post-order number incrementally. So let’s define an array order such that order[node] = position in T (starting from 0). Then for any node i, all nodes in its subtree have their order values forming a contiguous range [left[i], right[i]] where left[i] = min(order[j]) over j in subtree? Actually since it's depth-first and children processed increasingly; after processing entire subtree of i before adding s[i], all descendants' characters have been added already consecutively before adding s[i]. So indeed if we assign indices incrementally as we add characters during global DFS from root 0; let idx[node] be index where s[node] appears in T. Then for any node i with descendants set D_i; idx values for D_i are all less than idx[i] because they're added before s[i]; moreover they form consecutive integers because recursion processes whole subtrees without interruption; but careful: If there are multiple children of i; after processing first child's whole subtree you move onto second child; so indeed all descendants' indices are less than idx[i] but they may not be consecutive globally across different branches? Actually they are consecutive because you process one child completely before moving onto next; so indices allocated sequentially across entire recursion; thus set {idx[j] | j in subtree} forms a consecutive range [start_i+??]. Let’s define size_i = size_of_subtree(i). Then indices assigned to nodes in subtree form range [idx[i] - size_i + 1 , idx[i]] inclusive? Because last added character is s[i]; before adding s[i], you have added all descendants' characters sequentially; so total size_i-1 descendants added before adding s[i]; thus indices start at idx[i] - size_i +1 up to idx[i]. Indeed idx[i] is largest among them because s[i] last.

        # Proof by induction: When processing node i recursively:
            # For leaf: size=1 -> only idx[i]; range [idx[i],idx[i]] works.
            # For internal node with children c1,...,ck processed increasingly:
                # Recursively process children c1..ck sorted; after processing child cj you've appended size_cj characters; total sum sizes = size_i-1. Then append s[i]; so idx[i] = previous_index+1 where previous_index was index after last descendant added; thus indices assigned across whole subtree are consecutive block ending at idx[i]; start = idx[i] - size_i +1.

         # Therefore let pos[node] be index where s[node] appears in global T (post-order from root 0). Then standalone dfs(node) yields substring T[pos[node]-size[node]+1 : pos[node]+1 ] (Python slice inclusive start exclusive end). That substring length = size[node].

         # Now answer[node] asks whether this substring is palindrome.
         
         # So problem reduces to:
         # Compute sizes array using DFS from root 0 with children sorted increasingly.
         # Compute pos array (post-order index) during same DFS.
         # Build array A where A[pos[node]] = s[node]; so A is global T.
         # For each node query whether substring A[l..r] with l=pos-size+1 , r=pos is palindrome.
         		# We need efficient palindrome queries on static string A many times (up to n queries). Use rolling hash or Manacher?		
		# Since A length up to 100k and queries up to 100k , O(n log n) maybe okay but O(n^2) not okay.		
		# We can precompute prefix hashes forward and backward and answer queries O(1) per query using polynomial rolling hash with mod large prime(s). Use double hash for safety against collisions.		
		# Or use Manacher’s algorithm which finds longest palindrome centered at each position but not directly answering arbitrary substring palindrome queries unless substring length given?		
		# Rolling hash straightforward:		
		# Compute hash forward H_fwd such that H_fwd[r+1]-H_fwd[l]*p^(r-l+1) gives hash of substring l..r . Similarly compute reverse hash H_rev using same base but reversed direction . Then check equality.		
		# Use modulo large primes like MOD1=10**9+7 , MOD2=10**9+9 . Base random between large prime?		
         	base = random large integer . Choose base=131 or something . Use Python int without modulo but risk overflow ? Python big int fine . Use modulo two primes better .	
                	We'll implement double hash .		
                	Steps:		
                1. Build adjacency list children sorted .		
                2. Perform DFS from root 0 ; compute size[u], pos[u], also fill array A at pos[u]=s[u].		
                3. While DFS , maintain current index cur_idx starting 0 . After processing all children , assign pos[u]=cur_idx , increment cur_idx . This matches earlier reasoning because after processing children you add u's char ; so cur_idx starts at 0 ; first leaf gets pos=0 ; root gets last pos=n-1 . Wait careful : In our earlier reasoning , leaf gets smallest index because leaf processed first ? Actually depends on ordering . Let's simulate : Starting from root , go deep leftmost branch ; leaf gets processed first : leaf has no children ; so immediately add leaf char ; thus leaf gets index 0 . Then backtrack up ; parent adds after all children processed . So indeed leaf gets smallest index ; root gets largest index . Thus pos[u] increases as nodes finish . Hence substring for u : indices [pos[u]-size[u]+1 , pos[u]] inclusive . That matches earlier formula . But note pos[u]-size[u]+1 may be negative if size larger than pos ? No because size includes itself ; pos >= size-1 always true because descendants have smaller indices . Good .	
                	4.Compute prefix hashes forward on A : H_fwd[0]=0 ; H_fwd[i+1]=H_fwd[i]*base + ord(A[i]) mod MOD . Similarly reverse : B=A[::-1]; H_rev forward on B or directly compute backward prefix on original A with reversed direction easier : define H_rev_suffix maybe ? Better compute forward hash on reversed string R ; then substring l..r original corresponds to reversed indices n-1-r .. n-1-l on R ; compare hashes accordingly . We'll implement double hash both directions .	
                	5.For each node u : l=pos[u]-size[u]+1 ; r=pos[u]	Check palindrome : forward hash(l,r)==reverse_hash(l,r)	reverse_hash(l,r)=hash_rev(n-1-r,n-1-l)	where n length A=n . Use double modular arithmetic with two bases/modules maybe use tuple comparisons .	We'll define two bases b1,b2 random large primes or fixed like 131 ,137 ; mods m1,m2 large primes e.g.,10**9+7 ,10**9+9 . Precompute powers up to n .	Compute prefix arrays pref1 , pref2 forward ; pref_rev on reversed string similarly . Then query function get_hash(pref,l,r,pow_arr ) returns hash value mod m using formula h[r+1]-h[l]*pow_arr[r-l+1]	We'll implement helper class RollingHash maybe not necessary just functions within method due performance constraints?	Given n up to 100k okay O(n) memory O(n log n ) due pow precomputation but pow precomputation linear using iterative multiplication O(n). Fine.	Implement double rolling hash straightforwardly inside findAnswer method without class overhead but readability okay.	Return list bool results sized n initialized false fill true if palindrome detected else false etc."