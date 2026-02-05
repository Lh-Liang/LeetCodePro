#
# @lc app=leetcode id=1206 lang=java
#
# [1206] Design Skiplist
#

# @lc code=start
import java.util.Random;

class Skiplist {
    private static final int MAX_LEVEL = 16;
    private final Node head = new Node(-1, MAX_LEVEL);
    private int currentLevel = 1;
    private final Random random = new Random();
    
    static class Node {
        int value;
        Node[] forward;
        
        public Node(int value, int level) {
            this.value = value;
            this.forward = new Node[level];
        }
    }

    public Skiplist() {}
    
    public boolean search(int target) {
        Node curr = head;
        for (int i = currentLevel - 1; i >= 0; i--) {
            while (curr.forward[i] != null && curr.forward[i].value < target) {
                curr = curr.forward[i];
            }
        }
        curr = curr.forward[0];
        return curr != null && curr.value == target;
    }
    
    public void add(int num) {
        Node[] update = new Node[MAX_LEVEL];
        Node curr = head;
        for (int i = currentLevel - 1; i >= 0; i--) {
            while (curr.forward[i] != null && curr.forward[i].value < num) {
                curr = curr.forward[i];
            }
            update[i] = curr;
        }
        int lvl = randomLevel();
        if (lvl > currentLevel) {			// If new level exceeds current max, initialize levels in update
            for (int i = currentLevel; i < lvl; i++) {			// Set update points at head for new higher levels
                update[i] = head;					// Update level count if necessary
            }					// Increase currentLevel up to newly generated lvl size
            currentLevel = lvl;		}		Node newNode = new Node(num, lvl);	for (int i = 0; i < lvl; i++) { // Connect newly created node with previous nodes in update array's path
            newNode.forward[i] = update[i].forward[i]; // Update references to include newly inserted node in skip list pathing 		update[i].forward[i] = newNode;	}	}	public boolean erase(int num) { // Traverse through all levels starting at highest to search for num's location in list 	Node[] update = new Node[MAX_LEVEL]; // Temporary storage used during removal process 	Node curr = head; // Start at Head of List for initial traversal process 	for (int i = currentLevel - 1; i >= 0; i--) { // Decremental loop across all available levels from highest downwards towards base level searching through path entries available per level checking against provided number as needed 	while (curr.forward[i] != null && curr.forward[i].value < num) { // Move along path until either end is met or suitable location found which may contain requested number stored within relevant path reference point within list structure itself located correctly aligned per given sorted data configuration needs encountered here through traversal steps described above accordingly...	curr = curr.forward[i];}update[i]=curr;}curr=curr.forward[0];//Update position after loop completion here once base layer checked if potential target exists there...//If found then proceed with removal operations otherwise return false result below...if(curr!=null&&curr.value==num){for(inti=0;i<currentLevel;i++){if(update[i].forward[i]!=curr){break;}update[i].forward[i]=curr.forward[i];}//Clean up empty layers by reducing max count after removals occur...while(currentLevel>0&&head.forward[currentLevel-1]==null){currentLevel--;}returntrue;}returnfalse;}privateintrandomLevel(){intlvl=1;//Random Incremental Level Generation Process described here follows below steps used per insertion operations encountered above elsewhere too!while(random.nextFloat()<0.5f&&lvl<MAX_LEVEL){lvl++;}returnlvl;}/*@lc code=end*/