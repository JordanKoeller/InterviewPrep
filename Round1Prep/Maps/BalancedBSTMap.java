package Round1Prep.Maps;

import java.util.Stack;

public class BalancedBSTMap<K extends Comparable<K>, V> implements IMap<K, V> {
  class Node implements Comparable<K>{
    K key;
    V value;
    int height;
    Node left;
    Node right;
    public Node(K k, V v) {
      this.key = k;
      this.value = v;
      left = null;
      right = null;
      height = 0;
    }
    public int compareTo(K that) {
      return this.key.compareTo(that);
    }
    public boolean isLeaf() {
      return left == null && right == null;
    }

    public boolean oneChild() {
      return (left == null && right != null) || (right == null && left != null);
    }

    public boolean isBalancedHelper() {
      if (isLeaf()) return true;
      if (oneChild() && height == 1) return true;
      boolean isGood = !needsRotation();
      return isGood && left.isBalancedHelper() && right.isBalancedHelper();
    }

    public Node getSingleChild() {
      if (left != null) return left;
      return right;
    }

    public int getHeavySide() {
      int leftHeight = left == null ? -1 : left.height;
      int rightHeight = right == null ? -1 : right.height;
      return rightHeight - leftHeight;
    }

    public boolean needsRotation() {
      if (isLeaf()) return false;
      if (oneChild()) return height > 1;
      return height - left.height > 2 || height - right.height > 2; 
    }

    public void computeHeight() {
      int leftHeight = left == null ? 0 : left.height + 1;
      int rightHeight = right == null ? 0 : right.height + 1;
      height = Math.max(leftHeight, rightHeight);
    }

  }
  Node root = null;
  int sz = 0;
  int[] didRotate = {0, 0, 0, 0};

  public V deleteValue(K key) {
    if (root == null) throw new IndexOutOfBoundsException("Cannot delete from an empty list");
    Stack<Node> tail = dfsToKey(key);
    if (!tail.peek().key.equals(key)) throw new IndexOutOfBoundsException("Could not find key, so cannot delete it");
    Node nodeToDelete = tail.pop();
    V ret = nodeToDelete.value;
    if (nodeToDelete.isLeaf()) {
      if (nodeToDelete == tail.peek().left) tail.peek().left = null;
      else tail.peek().right = null;
    } else if (nodeToDelete.oneChild()) {
      if (nodeToDelete == tail.peek().left) tail.peek().left = nodeToDelete.getSingleChild();
      else tail.peek().right = nodeToDelete.getSingleChild();
    } else {
      tail.push(nodeToDelete);
      tail.push(nodeToDelete.right);
      while (tail.peek().left != null) {
        tail.push(tail.peek().left);
      }
      Node nextInOrder = tail.pop();
      nodeToDelete.key = nextInOrder.key;
      nodeToDelete.value = nextInOrder.value;
      if (tail.peek().left == nextInOrder) tail.peek().left = nextInOrder.right;
      else tail.peek().right = nextInOrder.right;
      rotateStack(tail);
    }
    sz--;
    return ret;
  }
  public V get(K key) {
    Node elem = findNodeWithkey(key);
    if (elem == null) return null;
    return elem.value;
  }
  public int size() {
    return sz;
  }
  public boolean hasKey(K key) {
    return findNodeWithkey(key) != null;
  }

  public boolean add(K key, V value) {
    if (root == null) {
      root = new Node(key, value);
      sz++;
      return true;
    } else if (root.key.equals(key)) {
      root.value = value;
      return false;
    }
    boolean ret = addHelper(new Node(key, value));
    if (ret) sz++;
    return ret;
  }

  private boolean addHelper(Node nodeToAdd) {
    Stack<Node> tail = dfsToKey(nodeToAdd.key);
    if (tail.size() == 0) {
      root = nodeToAdd;
      return true;
    }
    boolean alreadyInMap = tail.peek().key.equals(nodeToAdd.key);
    if (!alreadyInMap) {
      int comp = nodeToAdd.key.compareTo(tail.peek().key);
      if (comp < 0) tail.peek().left = nodeToAdd;
      else tail.peek().right = nodeToAdd;
      tail.push(nodeToAdd);
    } else {
      tail.peek().value = nodeToAdd.value;
    }
    if (!alreadyInMap) {
      rotateStack(tail);
    }
    return !alreadyInMap;
  }

  private Stack<Node> dfsToKey(K key) {
    Stack<Node> tail = new Stack<>();
    if (root == null) return tail;
    tail.push(root);
    while (true) {
      int comp = key.compareTo(tail.peek().key);
      if (comp == 0) {
        return tail;
      }
       else if (comp > 0) {
        if (tail.peek().right != null) {
          tail.push(tail.peek().right);
        } else {
        return tail;
        }
      } else {
        if (tail.peek().left != null) {
          tail.push(tail.peek().left);
        } else {
          return tail;
        }
      }
    }
  }


  private void rotateStack(Stack<Node> tail) {
    while (tail.size() > 0) {
      Node parent = tail.pop();
      parent.computeHeight();
      boolean needsRotation = parent.needsRotation();
      if (needsRotation) {
        // Left child is too tall
        if (tail.size() == 0) {
          root = fixSubtreeHelper(parent);
        } else {
          fixSubtrees(tail.peek(), parent);
        }
      }
    }
  }

  private Node findNodeWithkey(K key) {
    if (root == null) return null;
    if (root.key.equals(key)) return root;
    var rover = root;
    while (rover != null && !rover.key.equals(key)) {
      int comp = key.compareTo(rover.key);
      if (comp == 0) return rover;
      if (comp < 0) {
        rover = rover.left;
      }
      if (comp > 0) {
        rover = rover.right;
      }
    }
    return rover;
  }

  private void fixSubtrees(Node superParent, Node parent) {
    if (superParent.left == parent) superParent.left = fixSubtreeHelper(parent);
    else superParent.right = fixSubtreeHelper(parent);
  }

  private Node fixSubtreeHelper(Node parent) {
    //parent.printTree();
    int rotationDirection = parent.getHeavySide();
    if (rotationDirection < 0){
      // Need to rotate right.
      int childRotationDirection = parent.left.getHeavySide();
      if (childRotationDirection < 0) return rotateRight(parent);
      else return rotateRightZigzag(parent);
    } else if (rotationDirection > 0) {
      int childRotationDirection = parent.right.getHeavySide();
      if (childRotationDirection > 0) return rotateLeft(parent);
      else return rotateLeftZigzag(parent);
    } else {
      throw new NullPointerException("Somehow called fixSubtreeHelper with no rotation direction");
    }
  }

  private Node rotateRight(Node parent) {
    Node newParent = parent.left;
    parent.left = newParent.right;
    newParent.right = parent;
    parent.computeHeight();
    newParent.computeHeight();
    return newParent;
  }

  private Node rotateLeft(Node parent) {
    Node newParent = parent.right;
    parent.right = newParent.left;
    newParent.left = parent;
    parent.computeHeight();
    newParent.computeHeight();
    return newParent; 
  }

  private Node rotateRightZigzag(Node parent) {
    parent.left = rotateLeft(parent.left);
    parent.left.computeHeight();
    parent.computeHeight();
    return rotateRight(parent);
  }

  private Node rotateLeftZigzag(Node parent) {
    parent.right = rotateRight(parent.right);
    parent.right.computeHeight();
    parent.computeHeight();
    return rotateLeft(parent);
  }

}
