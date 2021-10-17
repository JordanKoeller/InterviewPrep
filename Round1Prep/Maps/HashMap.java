package Round1Prep.Maps;


public class HashMap<K, V> implements IMap<K, V> {

  private class KeyValuePair {
    private K key;
    public V value;

    public KeyValuePair nextPair;

    public KeyValuePair(K k, V v) {
      key = k;
      value = v;
      nextPair = null;
    }

    public K getKey() {return key;}
    public V getValue() { return value;}
  }

  private Object[] data;
  private int sz;
  private Hasher<K> hasher;
  
  public HashMap(Hasher<K> hashMethod) {
    data = new Object[32];
    sz = 0;
    hasher = hashMethod;
  }

  public boolean add(K key, V value) {
    if (data.length / (sz + 1) < 2) expand();
    boolean added = addPair(new KeyValuePair(key, value));
    if (added) sz++;
    return added;
  }

  @SuppressWarnings("unchecked")
  public V deleteValue(K key) {
    int idx = getTableIndex(key);
    var rover = (KeyValuePair) data[idx];
    if (rover == null) throw new IndexOutOfBoundsException();
    if (rover.key.equals(key)) {
      sz--;
      data[idx] = rover.nextPair;
      return rover.value;
    }
    while(rover.nextPair != null && !rover.nextPair.key.equals(key))
      rover = rover.nextPair;
    if (rover.nextPair != null && rover.nextPair.key.equals(key)) {
      V ret = rover.nextPair.value;
      rover.nextPair = rover.nextPair.nextPair;
      sz--;
      return ret;
    } else {
      throw new IndexOutOfBoundsException();
    }
  }

  public V get(K key) {
    var node = getNode(key);
    if (node != null && node.key.equals(key)) {
      return node.value;
    }
    throw new IndexOutOfBoundsException();
  }

  public boolean hasKey(K key) {
    var node = getNode(key);
    return node != null && node.key.equals(key);
  }

  public int size() {
    return sz;
  }


  private int getTableIndex(K key) {
    return hasher.hash(key) % data.length;
  }

  @SuppressWarnings("unchecked")
  private KeyValuePair getNode(K key) {
    int idx = getTableIndex(key);
    var rover = (KeyValuePair) data[idx];
    while (rover != null && !rover.key.equals(key)) {
      rover = rover.nextPair;
    }
    return rover;
  }

  @SuppressWarnings("unchecked")
  private boolean addPair(KeyValuePair kv) {
    int idx = getTableIndex(kv.getKey());
    if (data[idx] == null) {
      data[idx] = kv;
      return true;
    }
    var rover = (KeyValuePair) data[idx];
    while (rover.getKey() != kv.getKey() && rover.nextPair != null) rover = rover.nextPair;
    if (rover.getKey().equals(kv.getKey())) {
      rover.value = kv.getValue();
      return false;
    } else {
      rover.nextPair = kv;
      sz++;
      return true;
    }
  }

  @SuppressWarnings("unchecked")
  private void expand() {
    Object[] newBuffer = new Object[data.length * 2];
    Object[] oldBuffer = data;
    data = newBuffer;
    for (int i=0; i < oldBuffer.length; i++) {
      if (oldBuffer[i] != null) {
        var rover = (KeyValuePair) oldBuffer[i];
        while (rover != null) {
          addPair(new KeyValuePair(rover.key, rover.value));
          rover = rover.nextPair;
        }
      }
    }
  }
}
