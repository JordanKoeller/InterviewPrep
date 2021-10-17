package Round1Prep;


public class ArrayBuffer<T> {
  Object[] data;
  int sz;

  public ArrayBuffer() {
    data = new Object[16];
    sz = 0;
  }

  public int size() {
    return sz;
  }

  public void push(T elem) {
    if (sz == data.length) expand();
    data[sz] = elem;
    sz++;
  }

  @SuppressWarnings("unchecked")
  public T pop() {
    T ret = (T) data[sz-1];
    sz--;
    return ret;
  }
  
  @SuppressWarnings("unchecked")
  public T get(int index) {
    checkBounds(index);
    return (T) data[index];
  }
  
  public void set(T value, int index) {
    checkBounds(index);
    data[index] = value;
  }
  
  public void insert(T value, int index) {
    if (index == sz) {
      push(value);
      return;
    }
    checkBounds(index);
    if (sz == data.length) expand();
    for (int i = sz; index <= sz; i--) {
      data[i+1] = data[i];
    }
    data[index] = value;
    sz++;
  }
  
  @SuppressWarnings("unchecked")
  public T remove(int index) {
    checkBounds(index);
    T ret = (T) data[index];
    for (int i=index; i < sz-1; i++) {
      data[i] = data[i+1];
    }
    sz--;
    return ret;
  }

  private void checkBounds(int index) {
    if (!(index >= 0 && index < sz)) throw new IndexOutOfBoundsException();
  }


  private void expand() {
    Object[] newData = new Object[data.length * 2];
    for (int i=0; i < data.length; i++) newData[i] = data[i];
    data = newData;
  }
}