#include <iostream>

#include "DoublyLinkedList.hpp"

int main(void) {
  DoublyLinkedList<int> array;
  std::cout << "DoublyLinkedList is constructed \n";

  array.push_back(2);
  array.push_back(3);
  array.push_back(4);
  array.push_back(5);
  array.push_front(144);
  array.print();

  array.pop_back();
  array.pop_front();

  array.print();
  // array.push_back(12);
  // array.push_back(4);
  // array.push_back(8);
  // array.push_back(6);
  // array.push_back(7);
  // array.push_back(5);
  // array.push_back(3);
  // array.push_back(0);
  // array.push_back(9);

  std::cout << "Size is now " << array.size() << std::endl;


  for (auto iter=array.begin(); iter != array.end(); iter++) {
    std::cout << "Array value " << *iter << std::endl;
  }
}
