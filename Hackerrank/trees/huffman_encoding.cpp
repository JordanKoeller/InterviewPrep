#include <string>
#include <iostream>

using std::string;
using std::cout;
using std::endl;

typedef struct node
{
    int freq;
    char data;
    node * left;
    node * right;
    
}node;


void decode_huff(node * root, string s) {
  node * rover = root;
  string buffer;
  for (int i=0; i < s.size(); i++) {
    if (s[i] == '0' && rover->left != nullptr) {
      rover = rover->left;
    } else if (s[i] == '1' && rover->right != nullptr) {
      rover == rover->right;
    }
    if (rover->left == nullptr && rover->right == nullptr) {
      buffer.push_back(rover->data);
      rover = root;
    }
  }
  std::cout << buffer << std::endl;
}