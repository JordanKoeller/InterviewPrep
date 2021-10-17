package Round1Prep;

import java.util.Random;

import Round1Prep.Maps.BSTMap;
import Round1Prep.Maps.BalancedBSTMap;
import Round1Prep.Maps.HashMap;
import Round1Prep.Maps.Hasher;

class QuickStart {
  public static void main(String[] args) {
    System.out.println("Hello, World.");
    stresstest();
    // testAVLTree();
    // testArrayBuffer();
    // testBinaryTree();
    // testHashMap();
    System.out.println("Tests Finished");
  }

  public static void stresstest() {
    var avl = new BalancedBSTMap<Integer, String>();
    var bst = new BSTMap<Integer, String>();
    int maxNum = 10000000;
    System.out.println("Starting AVL");
    for (int i=0; i < maxNum; i++) {
      avl.add(i, "This is a string" + i);
    }
    for (int i=0; i < maxNum / 100; i++) {
      avl.hasKey(i);
    }
    System.out.println("Done. Starting BST");
    for (int i=0; i < maxNum; i++) {
      bst.add(i, "This is a string" + i);
    }
    for (int i=0; i < maxNum / 100; i++) {
      bst.hasKey(i);
    }
    System.out.println("Done");
  }

  public static void testAVLTree() {
    var map = new BalancedBSTMap<Integer, String>();
    assertEqual(map.size(), 0);
    assertTrue(map.add(0, "At key 0"));
    assertTrue(map.add(1000, "At key 1000"));
    assertTrue(!map.hasKey(3));
    assertTrue(map.hasKey(1000));
    assertEqual(map.size(), 2);
    // map.debug();
    assertEqual(map.get(1000), "At key 1000");
    assertEqual(map.get(0), "At key 0");

    for (int i = 1000; i >= 0; i--) {
      map.add(i * 7, "This is a string " + i * 7);
    }

    // assertInOrderBalanced(map);

    for (int i = 1000; i >= 0; i--) {
      assertTrue(map.hasKey(i * 7));
      assertEqual(map.get(i * 7), "This is a string " + i * 7);
    }

    for (int i = 1000; i >= 0; i--) {
      if (i % 3 == 0) {
        assertEqual(map.deleteValue(i * 7), "This is a string " + i * 7);
      }
    }
    // assertInOrderBalanced(map);

    for (int i = 1000; i >= 0; i--) {
      if (i % 3 == 0) {
        // System.out.println("Deleting" + i * 7);
        assertTrue(!map.hasKey(i * 7));
      } else {
        assertTrue(map.hasKey(i * 7));
      }
    }
    // assertInOrderBalanced(map);

    var rng = new Random();
    for (int i = 0; i < 5000; i++) {
      var randMap = new BalancedBSTMap<Integer, String>();
      for (int j=0; j < 100; j++) {
        int num = rng.nextInt(500);
        randMap.add(num, "String" + num);
      }
      // assertInOrderBalanced(randMap);
    }
  }


  public static void testBinaryTree() {
    var map = new BSTMap<Integer, String>();
    assertEqual(map.size(), 0);
    assertTrue(map.add(0, "At key 0"));
    assertTrue(map.add(1000, "At key 1000"));
    assertTrue(!map.hasKey(3));
    assertTrue(map.hasKey(1000));
    assertEqual(map.size(), 2);
    // map.debug();
    assertEqual(map.get(1000), "At key 1000");
    assertEqual(map.get(0), "At key 0");

    for (int i = 1000; i >= 0; i--) {
      map.add(i * 7, "This is a string " + i * 7);
    }

    // assertInOrder(map);

    for (int i = 1000; i >= 0; i--) {
      assertTrue(map.hasKey(i * 7));
      assertEqual(map.get(i * 7), "This is a string " + i * 7);
    }

    for (int i = 1000; i >= 0; i--) {
      if (i % 3 == 0) {
        assertEqual(map.deleteValue(i * 7), "This is a string " + i * 7);
      }
    }
    // assertInOrder(map);

    for (int i = 1000; i >= 0; i--) {
      if (i % 3 == 0) {
        // System.out.println("Deleting" + i * 7);
        assertTrue(!map.hasKey(i * 7));
      } else {
        assertTrue(map.hasKey(i * 7));
      }
    }
    // assertInOrder(map);

    var rng = new Random();
    for (int i = 0; i < 5000; i++) {
      var randMap = new BSTMap<Integer, String>();
      for (int j=0; j < 100; j++) {
        int num = rng.nextInt(500);
        randMap.add(num, "String" + num);
      }
      // assertInOrder(randMap);
    }
  }


// 
  public static void testArrayBuffer() {
    ArrayBuffer<Integer> buff = new ArrayBuffer<>();
    assertEqual(buff.size(), 0);
    buff.push(5);
    buff.push(4);
    buff.push(3);
    assertEqual(buff.size(), 3);
    assertEqual(buff.get(0), 5);
    assertEqual(buff.get(1), 4);
    assertEqual(buff.get(2), 3);
    assertEqual(buff.pop(), 3);
    assertEqual(buff.size(), 2);
  }

  public static void testHashMap() {
    final var hasher = new IntHasher();
    HashMap<Integer, String> map = new HashMap<>(hasher);
    assertEqual(map.size(), 0);
    assertTrue(map.add(0, "At key 0"));
    assertTrue(map.add(1000, "At key 1000"));
    assertTrue(!map.hasKey(3));
    assertTrue(map.hasKey(1000));
    assertEqual(map.size(), 2);
    // map.debug();
    assertEqual(map.get(1000), "At key 1000");
    assertEqual(map.get(0), "At key 0");

    for (int i = 1000; i >= 0; i--) {
      map.add(i * 7, "This is a string " + i * 7);
    }

    for (int i = 1000; i >= 0; i--) {
      assertTrue(map.hasKey(i * 7));
      assertEqual(map.get(i * 7), "This is a string " + i * 7);
    }
    for (int i = 1000; i >= 0; i--) {
      if (i % 3 == 0) {
        assertEqual(map.deleteValue(i * 7), "This is a string " + i * 7);
      }
    }

    for (int i = 1000; i >= 0; i--) {
      if (i % 3 == 0) {
        assertTrue(!map.hasKey(i * 7));
      } else {
        assertTrue(map.hasKey(i * 7));
      }
    }
  }

  static <T> void assertEqual(T a, T b) {
    try {
      if (a == b || a.equals(b)) {
        // System.out.println("PASS " + a.toString() + " == " + b.toString());
      } else {
        throw new AssertionError(a.toString() + " != " + b.toString());
      }
    } catch (Exception e) {
      System.out.println("Caught exception when checking " + a.toString() + " == " + b.toString());
      System.out.println(e.toString());
      throw e;
    }
  }

  static <T> void assertTrue(boolean v) {
    if (!v) {
      throw new AssertionError("Value was not true");
    } else {
      // System.out.println("Asserted True");
    }
  }
}

class IntHasher implements Hasher<Integer> {
  public int hash(Integer i) {
    return i;
  }
}