package Round1Prep.Maps;

public interface IMap<K,V> {

  public V deleteValue(K key);
  public boolean add(K key, V value);
  public V get(K key);
  public int size();
  public boolean hasKey(K key);
}


/*
      5
    3
  2   4
1       

*/