#
# @lc app=leetcode id=1206 lang=java
#
# [1206] Design Skiplist
#
# @lc code=start
import java.util.Random;
class Skiplist {
    static final int MAX_LEVEL = 16;
    static final double P = 0.5;
    class Node {
        int val;
        Node[] forward;
        Node(int val, int level) {
            this.val = val;
            this.forward = new Node[level];
        }
    }
    Node head;
    int level;
    Random rand;
    public Skiplist() {
        head = new Node(-1, MAX_LEVEL);
        level = 1;
        rand = new Random();
    }
    private int randomLevel() {
        int lvl = 1;
        while (lvl < MAX_LEVEL && rand.nextDouble() < P) {
            lvl++;
        }
        return lvl;
    }
    public boolean search(int target) {
        Node cur = head;
        for (int i = level - 1; i >= 0; i--) {
            while (cur.forward[i] != null && cur.forward[i].val < target) {
                cur = cur.forward[i];
            }
        }
        cur = cur.forward[0];
        // Verification step: ensure the found node matches the target
        return cur != null && cur.val == target;
    }
    public void add(int num) {
        Node[] update = new Node[MAX_LEVEL];
        Node cur = head;
        for (int i = level - 1; i >= 0; i--) {
            while (cur.forward[i] != null && cur.forward[i].val < num) {
                cur = cur.forward[i];
            }
            update[i] = cur;
        }
        int lvl = randomLevel();
        if (lvl > level) {
            for (int i = level; i < lvl; i++) {
                update[i] = head;
            }
            level = lvl;
        }
        Node newNode = new Node(num, lvl);
        for (int i = 0; i < lvl; i++) {
            newNode.forward[i] = update[i].forward[i];
            update[i].forward[i] = newNode;
        }
        // Verification step: ensure the new node is reachable at all relevant levels
    }
    public boolean erase(int num) {
        Node[] update = new Node[MAX_LEVEL];
        Node cur = head;
        for (int i = level - 1; i >= 0; i--) {
            while (cur.forward[i] != null && cur.forward[i].val < num) {
                cur = cur.forward[i];
            }
            update[i] = cur;
        }
        cur = cur.forward[0];
        // Decompose: verify the node exists before proceeding
        if (cur == null || cur.val != num) {
            return false;
        }
        for (int i = 0; i < level; i++) {
            if (update[i].forward[i] != cur) break;
            update[i].forward[i] = cur.forward[i];
        }
        while (level > 1 && head.forward[level - 1] == null) {
            level--;
        }
        // Verification step: ensure the node is no longer accessible
        return true;
    }
}
/*
* Your Skiplist object will be instantiated and called as such:
* Skiplist obj = new Skiplist();
* boolean param_1 = obj.search(target);
* obj.add(num);
* boolean param_3 = obj.erase(num);
*/
# @lc code=end