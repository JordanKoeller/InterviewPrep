#include <vector>
#include <unordered_set>

struct Node {
  int data;
  Node* left;
  Node* right;
};

using std::vector;
using std::unordered_set;


void helper(Node * node, vector<int> & buffer, unordered_set<int> &unique) {
  if (node->left != nullptr) helper(node->left, buffer, unique);
  buffer.push_back(node->data);
  unique.insert(node->data);
  if (node->right != nullptr) helper(node->right, buffer, unique);
}

bool checkBST(Node* root) {
  vector<int> buffer;  
  unordered_set<int> values;
  helper(root, buffer, values);
  if (buffer.size() != values.size()) return false;
  for (int i=1; i < buffer.size(); i++) {
    if (buffer[i-1] >= buffer[i]) {
      return false;
    }
  }
  return true;
}