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
    /**
     * Helper function to check if the linked list starting from 'head' matches
     * a downward path in the binary tree starting from 'node'.
     */
    bool checkPath(ListNode* head, TreeNode* node) {
        // If we reached the end of the linked list, all nodes matched.
        if (head == nullptr) return true;
        // If we reached a leaf in the tree but the list is not finished, no match.
        if (node == nullptr) return false;
        // If values don't match, this path is invalid.
        if (node->val != head->val) return false;
        
        // Continue checking the next list node in both left and right directions.
        return checkPath(head->next, node->left) || checkPath(head->next, node->right);
    }

    bool isSubPath(ListNode* head, TreeNode* root) {
        if (root == nullptr) return false;
        
        // Check if the path starts at the current root, or in the left/right subtrees.
        return checkPath(head, root) || isSubPath(head, root->left) || isSubPath(head, root->right);
    }
};
# @lc code=end