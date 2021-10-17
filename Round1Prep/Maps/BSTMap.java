package Round1Prep.Maps;

import java.util.ArrayList;

public class BSTMap<K extends Comparable<K>, V> implements IMap<K,V> {
  class Node implements Comparable<Node> {
    K key;
    V value;
    Node left;
    Node right;
    public Node(K k, V v) {
      this.key = k;
      this.value = v;
      left = null;
      right = null;
    }
    public int compareTo(Node that) {
      return this.key.compareTo(that.key);
    }
    public boolean isLeaf() {
      return left == null && right == null;
    }

    public boolean oneChild() {
      return (left == null && right != null) || (right == null && left != null);
    }

    public Node getSingleChild() {
      if (left != null) return left;
      return right;
    }

    public void inOrderAppend(ArrayList<K> elems) {
      if (left != null) left.inOrderAppend(elems);
      elems.add(key);
      if (right != null) right.inOrderAppend(elems);
    }
  }

  private Node root;
  private int sz;

  public BSTMap() {
    root = null;
    sz = 0;
  }

  public boolean add(K key, V value) {
    Node addingNode = new Node(key, value);
    if (root == null) {
      root = addingNode;
      sz++;
      return true;
    }
    boolean added = addChildHelper(addingNode, root);
    if (added) sz++;
    return added;
  }

  public V get(K key) {
    Node node = findNode(key);
    if (node != null) return node.value;
    throw new IndexOutOfBoundsException("Could not find key in tree");
  }

  public int size() {
    return sz;
  }

  public boolean hasKey(K key) {
    return findNode(key) != null;
  }

  public V deleteValue(K key) {
    if (root == null) throw new IndexOutOfBoundsException("Tried to delete from empty tree");
    if (root.key.equals(key)) {
      Node deletingNode = root;
      if (root.isLeaf()) root = null;
      else if (root.oneChild()) root = root.getSingleChild();
      else {
        root = deletingNode.right;
        addChildHelper(deletingNode.left, root);
      }
      sz--;
      return deletingNode.value;
    }
    Node searchNode = new Node(key, null);
    Node parent = findParent(searchNode, root);
    int comp = searchNode.compareTo(parent);
    if (comp < 0) {
      if (parent.left == null) throw new IndexOutOfBoundsException("Node not found");
      Node deletingNode = parent.left;
      if (deletingNode.isLeaf()) {
        parent.left = null;
      } else if (deletingNode.oneChild()) {
        parent.left = deletingNode.getSingleChild();
      } else {
        parent.left = deletingNode.right;
        addChildHelper(deletingNode.left, parent);
      }
      sz --;
      return deletingNode.value;
    } else {
      if (parent.right == null) throw new IndexOutOfBoundsException("Nod not found");
      Node deletingNode = parent.right;
      if (deletingNode.isLeaf()) {
        parent.right = null;
      } else if (deletingNode.oneChild()) {
        parent.right = deletingNode.getSingleChild();
      } else {
        parent.right = deletingNode.left;
        addChildHelper(deletingNode.right, parent);
      }
      sz--;
      return deletingNode.value;
    }
  }

  public ArrayList<K> inOrderTraverse() {
    ArrayList<K> elems = new ArrayList<K>();
    if (root == null) return elems;
    root.inOrderAppend(elems);
    return elems;
  }

  private boolean addChildHelper(Node n, Node parent) {
    Node rover = parent;
    while (true) {
      int comp = n.compareTo(rover);
      if (comp == 0) {
        rover.value = n.value;
        return false;
      }
      if (comp < 0) {
        if (rover.left == null) {
          rover.left = n;
          return true;
        } else {
          rover = rover.left;
        }
      } else {
        if (rover.right == null) {
          rover.right = n;
          return true;
        } else {
          rover = rover.right;
        }
      }
    }
  }


  private Node findParent(Node n, Node startingPoint) {
    var rover = startingPoint;
    while (true) {
      int comp = n.compareTo(rover);
      if (comp == 0) throw new IndexOutOfBoundsException("Found node in findParent");
      if (comp < 0) {
        if (rover.left == null) {
          return rover;
        } else {
          if (rover.left.key.equals(n.key)) return rover;
          rover = rover.left;
        }
      } else {
        if (rover.right == null) {
          return rover;
        } else {
          if (rover.right.key.equals(n.key)) return rover;
          rover = rover.right;
        }
      }
    }
  }

  private Node findNode(K key) {
    if (root == null || root.key.equals(key)) return root;
    Node searchNode = new Node(key, null);
    Node node = findParent(searchNode, root);
    int comp = searchNode.compareTo(node);
    if (comp < 0) return node.left;
    return node.right;
  }
  
}
