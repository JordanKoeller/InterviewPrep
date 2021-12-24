use std::hash::{Hash, Hasher};
use std::collections::hash_map::DefaultHasher;

fn main() {
    println!("Hello, world!");
}

struct CountMinSketch<T: Hash + Sized + 'static> {
  matrix: Vec<Vec<u64>>,
  heap: Vec<Option<(u64, T)>>,
}

// Public methods
impl<T: Hash + Sized + 'static> CountMinSketch<T> {
  pub fn new(num_elems: u32, accuracy: f64, k: u32) -> Self {
    let num_hashers = Self::get_num_hashers(num_elems, accuracy);
    let hash_space = Self::get_hash_space(num_elems, accuracy);
    let mut matrix = Vec::new();
    for i in 0..num_hashers {
      matrix.append(Vec::new());
      for j in 0..hash_space {
        matrix[matrix.len() - 1].append(0);
      }
    }
    let mut heap = Vec::new();
    for i in 0..k {
      heap.append(None);
    }
    Self {
      matrix,
      heap
    }
  }

  pub fn add(&mut self, elem: T) {
    let mut min_count = u64::MAX_VALUE;
    for i in 0..self.matrix.len() {
      let mut hasher = DefaultHasher::new();
      hasher.write(&i);
      elem.hash(&mut hasher);
      let hash_val = hasher.finish();
      self.matrix[i][hash_val] += 1;
      if self.matrix[i][hash_val] < min_count {
        min_count = self.matrix[i][hash_val];
      }
    }
    self.maintain_heap(min_count, elem);
  }

  pub fn get_top_k(&self): Vec<T> {
    let mut heap = self.heap.to_vec();
    let mut ret = Vec::new();
    while heap[0].is_some() {
      ret.append(heap[0].unwrap()[1].clone());
      let mut i = 0;
      while i < heap.len() && heap[i].is_some() {
        if heap[i * 2 + 1].is_some() && heap[i * 2 + 2].is_some() {
          if heap[i * 2 + 1].unwarp()[0] > heap[i * 2 + 2].unwrap()[0] {
            heap[i] = heap[i * 2 + 1].clone();
            i = i * 2 + 1;
          } else {
            heap[i] = heap[i * 2 + 2].clone();
            i = i * 2 + 2;
          }
        } else {
          heap[i] = heap[i * 2 + 1].clone();
          i = i * 2 + 1;
        }
      }
    }
  }
}


impl<T: Hash + Sized + 'static> CountMinSketch<T> {
  fn get_num_hashers(num_elems: u32, accuracy: f64) -> u32 {
    10
  }

  fn get_hash_space(num_elems: u32, accuracy: f64) -> u32 {
    10000
  }

  fn maintain_heap(&mut self, count: u64, elem: T) {
    let mut i = 0;
    let mut rover = (count.clone(), elem);
    if self.heap[0].is_none() {
      self.heap[0] = rover;
      return
    }
    while i < self.heap.len() {
      let c_1 = i * 2 + 1;
      let c_2 = i * 2 + 2;
      let top_count = self.heap[i][0];
      if count <= top_count {
        if self.heap[c_1].is_none() {
          self.heap[c_1] = Some(rover);
          return
        }
        if self.heap[c_2].is_none() {
          self.heap[c_2] = Some(rover);
          return
        }
      } else {
        if self.heap[c_2].unwrap()[0] <= count {
          let tmp = self.heap[c_2].unwrap().clone();
          self.heap[c_2] = rover;
          rover = tmp;
          i = c_2;
        } else {
          let tmp = self.heap[c_1].unwrap().clone();
          self.heap[c_1] = rover;
          rover = tmp;
          i = c_1;
        }
      }
    }
  }
}
