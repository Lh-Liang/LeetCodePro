#
# @lc app=leetcode id=1367 lang=cpp
#
# [1367] Linked List in Binary Tree
#

# @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isSubPath(ListNode* head, TreeNode* root) {
        if (!root) return false;
        // Try starting the path from the current root, or look in subtrees
        return checkPath(head, root) || isSubPath(head, root->left) || isSubPath(head, root->right);
    }

private:
    bool checkPath(ListNode* head, TreeNode* node) {
        // If we reached the end of the list, the path is fully matched
        if (!head) return true;
        // If we reached a leaf in the tree before the list, match failed
        if (!node) return false;
        // Value mismatch
        if (head->val != node->val) return false;
        
        // Continue matching the next list node in the child nodes
        return checkPath(head->next, node->left) || checkPath(head->next, node->right);
    }
};
# @lc code=end