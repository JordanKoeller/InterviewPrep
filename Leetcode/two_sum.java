package Leetcode;

import java.util.HashMap;
import java.util.ArrayList;
import java.util.List;
public class two_sum {
 public static void main(String[] args) {
   
 }


 public int[] twoSum(int[] nums, int target) {
  HashMap<Integer, Integer> encountered = new HashMap<>();
  for (int i = 0; i < nums.length; i++) {
    int lookingFor = target - nums[i];
    if (encountered.containsKey(lookingFor)) return new int[] {encountered.get(lookingFor), i};
    else encountered.put(nums[i], i);
  }
  throw new IndexOutOfBoundsException();
 }

}
