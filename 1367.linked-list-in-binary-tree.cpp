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
        // Check if the path starts at the current root, or if it exists in the left or right subtrees
        return checkPath(head, root) || isSubPath(head, root->left) || isSubPath(head, root->right);
    }

private:
    bool checkPath(ListNode* head, TreeNode* root) {
        // Base case: If we've reached the end of the linked list, the path is found
        if (!head) return true;
        // Base case: If the tree node is null or values mismatch, this path fails
        if (!root || root->val != head->val) return false;
        
        // Recursively check the next node in the list against the children of the current tree node
        return checkPath(head->next, root->left) || checkPath(head->next, root->right);
    }
};
# @lc code=end