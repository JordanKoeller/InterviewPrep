#include <iostream>

#include <string>

template <typename T>
class ArrayList {
private:
  size_t sz;
  size_t capacity;
  T* data;

public:
  ArrayList<T>() {
    sz = 0;
    capacity = 4;
    data = new T[4];
  }

  ~ArrayList<T>() {
    delete[] data;
  }

  void print() {
    std::cout << "ArrayList size = " << sz << ", capacity = " << capacity << std::endl;
  }

  void print_elems() {
    std::cout << "[ ";
    for (size_t i = 0; i < size() - 1; i++)
      std::cout << data[i] << ", ";
    std::cout << data[size() - 1] << " ]" << std::endl;
  }

  T& operator[](size_t index) {
    if (index >= 0 && index < sz) {
      return data[index];
    }     else {
      throw std::invalid_argument("Index {} out of bounds for ArrayList of size {}");
    }
  }

  size_t push_back(T v) {
    if (sz == capacity) {
      growArray();
    }
    data[sz++] = v;
    return sz;
  }

  size_t size() {
    return sz;
  }

  class iterator {
    private:
      T * ptr;
    public:
    iterator() = default;
    iterator(T * p): ptr{p} {}
      iterator operator++() {
        this->ptr++;
        return iterator(this->ptr);
      }
      iterator operator--() {
        this->ptr--;
        return iterator(this->ptr);
      }
      iterator operator++(int) {
        this->ptr++;
        return iterator(this->ptr);
      }
      iterator operator--(int) {
        this->ptr--;
        return iterator(this->ptr);
      }
      bool operator==(const iterator & other) {
        return ptr == other.ptr;
      }
      bool operator!=(const iterator & other) {
        return ptr != other.ptr;
      }
      T& operator*() {
        return *ptr;
      }
      friend class ArrayList;
  };

  iterator begin() {
    return iterator(data);
  }

  iterator end() {
    return iterator(data+size());
  }

private:
  void growArray() {
    T* newData = new T[capacity * 2];
    for (size_t i = 0; i < capacity; i++)
      newData[i] = data[i];
    delete[] data;
    data = newData;
    capacity *= 2;
  }
};
