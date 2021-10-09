#include <iostream>
#include <string>

using std::cout;
using std::endl;

template<typename T>

class DoublyLinkedList {
private:
  struct Node {
    T data;
    Node* next;
    Node* prev;
  };

  Node* head;
  size_t sz;

  void print_node(Node* p) {
    cout << "Printing Node" << p << endl;
    if (p != nullptr) {
      cout << "{prev: " << p->prev << ", data: " << p->data << ", next: " << p->next << " }" << endl;
    }
  }

public:
  DoublyLinkedList<T>() : head{ nullptr }, sz{ 0 } {}
  ~DoublyLinkedList<T>() {
    if (sz == 0) {
      return; // No cleanup to do. Nothing is allocated.
    }
    if (sz == 1) {
      delete head;
      return;
    }
    Node* start = head;
    Node* rover = head->next;
    while (rover->next != start) {
      rover = rover->next;
      delete rover->prev;
    }
    delete start;
  }

  size_t size() {
    return sz;
  }

  size_t push_back(T elem) {
    Node* myNode = new Node;
    myNode->data = elem;
    if (head == nullptr) {
      myNode->next = myNode;
      myNode->prev = myNode;
      head = myNode;
    } else {
      myNode->next = head;
      myNode->prev = head->prev;
      head->prev->next = myNode;
      head->prev = myNode;
    }
    sz++;
    return sz;
  }

  size_t push_front(T elem) {
    auto ret = push_back(elem);
    head = head->prev;
    return ret;
  }

  size_t pop_front() {
    if (head != nullptr) {
      head = head->next;
      pop_node(head->prev);
      sz--;
    }
    if (sz == 0) {
      head = nullptr;
    }
    return sz;
  }

  size_t pop_back() {
    if (head != nullptr) {
      pop_node(head->prev);
      sz--;
    }
    if (sz == 0) {
      head = nullptr;
    }
    return sz;
  }

private:
  bool pop_node(Node* node) {
    if (node == nullptr) {
      return false;
    }
    node->prev->next = node->next;
    node->next->prev = node->prev;
    delete node;
    return true;
  }


public:

  void print() {
    print_node(head);
    Node* rover = head;
    cout << "[ " << rover->data;
    rover = rover->next;
    while (rover != head) {
      cout << ", " << rover->data;
      rover = rover->next;
    }
    cout << " ]" << endl;
  }

  // Iterator follows:
  class iterator {
  private:
    Node* head;
    Node* elem;
  public:
    iterator() = default;
    iterator(Node* p) : head{ p }, elem{ p } {}
    iterator(Node* s, Node* e) : head{ s }, elem{ e } {}
    iterator operator++() {
      if (elem->next == head) {
        elem = nullptr;
        return iterator(head, nullptr);
      }
      auto ret = iterator(head, elem->next);
      elem = elem->next;
      return ret;
    }
    iterator operator--() {
      if (elem == head) {
        elem = nullptr;
        return iterator(head, nullptr);
      }
      auto ret = iterator(head, elem->prev);
      elem = elem->prev;
      return ret;
    }
    iterator operator++(int) {
      if (elem->next == head) {
        elem = nullptr;
        return iterator(head, nullptr);
      }
      auto ret = iterator(head, elem->next);
      elem = elem->next;
      return ret;
    }
    iterator operator--(int) {
      if (elem == head) {
        elem = nullptr;
        return iterator(head, nullptr);
      }
      auto ret = iterator(head, elem->prev);
      elem = elem->prev;
      return ret;
    }
    bool operator==(const iterator& other) {
      return elem == other.elem;
    }
    bool operator!=(const iterator& other) {
      return !((*this) == other);
    }
    T& operator*() {
      return elem->data;
    }
    friend class DoublyLinkedList;
  };

  iterator begin() {
    return iterator(head, head);
  }

  iterator end() {
    return iterator(head, nullptr);
  }

};