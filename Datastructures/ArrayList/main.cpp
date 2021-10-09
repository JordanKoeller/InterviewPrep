#include <iostream>

#include "ArrayList.hpp"

int main(void) {
  ArrayList<int> array;
  std::cout << "ArrayList is constructed \n";
  array.print();
  array.push_back(12);
  array.push_back(4);
  array.push_back(8);
  array.push_back(6);
  array.push_back(7);
  array.push_back(5);
  array.push_back(3);
  array.push_back(0);
  array.push_back(9);

  std::cout << "Size is now " << array.size() << std::endl;

  array[5] = 5;
  array[4] = 4;
  array[3] = 3;
  array[2] = 2;
  array[1] = 1;

  array.print_elems();

  for (auto iter=array.begin(); iter != array.end(); iter++) {
    std::cout << "Array value " << *iter << std::endl;
  }
}
