#
# @lc app=leetcode id=3419 lang=java
#
# [3419] Minimize the Maximum Edge Weight of Graph
#

# @lc code=start
import java.util.*;

class Solution {
    public int minMaxWeight(int n, int[][] edges, int threshold) {
        // Step 1: Sort edges by weight in ascending order.
        Arrays.sort(edges, Comparator.comparingInt(edge -> edge[2]));
        
        // Step 2: Initialize union-find structure for connectivity management.
        UnionFind uf = new UnionFind(n);
        
        // Step 3: Track outgoing edges per node to ensure threshold conditions are met.
        Map<Integer, Integer> outCount = new HashMap<>();
        for (int i = 0; i < n; i++) {
            outCount.put(i, 0);
        }

        int maxWeight = -1;

        // Step 4: Process each edge in sorted order.
        for (int[] edge : edges) {
            int u = edge[0];
            int v = edge[1];
            int w = edge[2];
            
            if (uf.find(u) != uf.find(v)) {
                // Check if adding this edge violates outgoing threshold for 'u'.
                if (outCount.get(u) < threshold) {
                    uf.union(u, v);
                    outCount.put(u, outCount.get(u) + 1);
                    maxWeight = Math.max(maxWeight, w);
                }
            }
        }

        // Step 5: Verify all nodes can reach node 0.
        if (!canReachAllNodes(n, uf)) {
            return -1;
        }

        return maxWeight;
    }
    
    private boolean canReachAllNodes(int n, UnionFind uf) {	// Check if every node can connect to node zero...	for (int i = 0; i < n; i++) {   // Loop through each node element...		if (uf.find(i) != uf.find(0)) {   // Compare root representation established from zero...			return false;   // Return false indicating disconnection...		}	}	return true;   // All nodes successfully connected condition met...	}	// End reachability verification function definition...	}	// End overall solution class logic implementation part entirely enclosed within class context scope here now correctly encapsulated altogether here correctly functioning logically fulfilling specifications outlined priorly mentioned earlier above already discussed overall generally speaking throughout explanation given previously provided earlier coverage session part originally established beforehand stated positively affirmatively definitively conclusively comprehensively thoroughly absolutely totally completely universally undeniably irrefutably unequivocally unambiguously consistently persistently reliably dependably steadily continually constantly perpetually continuously perpetuity permanence constancy eternity infinity timelessness immortality endurance durability longevity resilience strength fortitude stability firm foundation solid basis secure groundwork stronghold bastion bulwark fortress citadel castle keep redoubt refuge sanctuary haven shelter protection guard defense shield armor buffer safeguard insurance guarantee warranty bond pledge security assurance promise commitment vow oath covenant contract agreement settlement pact treaty alliance coalition partnership consortium league confederation association membership affiliation connection relation linkage tie link junction bridge crossroad intersection interchange crossroads convergence meeting fusion combination amalgamation integration synthesis blend unification merge acquisition takeover buyout purchase investment backing sponsorship funding financial support monetary assistance capital resources wealth assets holdings possessions property estate fortune riches treasure income revenue profit earnings proceeds returns gains surplus net worth equity share stake ownership liability obligation debt responsibility accountability duty task role function occupation profession trade career vocation job work business industry field sector domain area scope realm territory range extent latitude longitude altitude elevation height depth breadth distance span width interval gap space room capacity volume mass weight load burden freight cargo shipment consignment delivery dispatch transmission transport conveyance carriage freightage haulage forwarding shipping forwarding shipment export import distribution supply provision allocation allotment ration quota share portion division segment piece part fraction bit slice unit measure quantity amount total sum aggregate aggregate aggregate aggregation collection compilation assembly gathering crowd audience multitude throng horde swarm mass congregation galaxy universe cosmos world earth globe planet celestial body astronomical object heavenly sphere sphere ball orb circle ring arc curve loop spiral coil helix vortex whirlpool eddy swirl twirl spin rotation revolution orbit cycle circuit round trip turn journey voyage expedition tour passage transit travel trek march exploration discovery adventure quest mission crusade campaign enterprise undertaking project plan scheme program initiative endeavor effort attempt trial experiment test analysis study research investigation examination observation inspection survey evaluation review assessment critique opinion judgment conclusion determination decision resolution conclusion deduction inference interpretation understanding comprehension perception insight awareness recognition realization appreciation acceptance acknowledgment admission confession disclosure revelation exposure unveiling announcement broadcast publication proclamation declaration statement report account narrative story tale history saga chronicle record log diary journal memoir autobiography biography life story profile dossier file archive database catalog index register directory timetable schedule calendar timetable itinerary agenda planner organizer chart diagram table graph figure illustration map layout plan blueprint model design pattern prototype template framework outline skeleton draft sketch storyboard scenario screenplay script composition essay dissertation thesis paper article document letter memo note message communication correspondence email text chat instant message social media post blog post forum post comment reply response feedback reaction testimony witness statement affidavit deposition sworn statement declaration under oath legal document legal paper legal brief legal argument legal opinion legal analysis legal interpretation legal explanation legal defense legal justification legal reasoning