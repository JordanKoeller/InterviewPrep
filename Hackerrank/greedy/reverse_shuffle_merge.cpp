// s = aabbccdd
// char <- a = {d, c, b, a}
// lexMin = abcd
// reverse(A) = abcd
// A = dcba
// s has a LCS(reverse(A), s) = reverse(A)

/**
 *  Steps:
 *   1. Count repetions of characters. divide by 2
 *      to get the number of each character in A
 *   2. Construct the lexographically maximal substring from s
 *      that uses the characters in A
 *   3. Reverse it to get the lexographically minimal string.
 */

#include <bits/stdc++.h>

using namespace std;

/*
 * Complete the 'reverseShuffleMerge' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING s as parameter.
 */

struct iter_state_t {
  int i;
  vector<int> chars_to_consume;
  vector<int> num_remaining_skips;
  int focused_char;
};



string reverseShuffleMerge(string s) {
  vector<int> skippable_chars (26, 0);
  for (auto c: s) skippable_chars[c - 'a']++;
  for (size_t i=0; i < 26; i++) {
    skippable_chars[i] = skippable_chars[i] / 2;
  }
  vector<int> consumable_chars {skippable_chars.begin(), skippable_chars.end()};
  deque<int> ret_stack;

  for (auto iter=s.rbegin(); iter != s.rend(); iter++) {
    int index = *iter - 'a';
    if (consumable_chars[index] > 0) {
      while (ret_stack.size() > 0 && ret_stack.back() > index && skippable_chars[ret_stack.back()] > 0) {
        int skipped = ret_stack.back();
        ret_stack.pop_back();
        consumable_chars[skipped] += 1;
        skippable_chars[skipped] -= 1;
      }
      ret_stack.push_back(index);
      consumable_chars[index] -= 1;
    } else {
      skippable_chars[index] -= 1;
    }
  }
  string ret;
  ret.reserve(ret_stack.size());
  for (size_t i=0; i < ret_stack.size(); i++) {
    ret.push_back('a' + (char) ret_stack[i]);
  }

  // Find the lexigraph. Min subsequence of s containing all
    // the necessary characters.
  return ret;

}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s;
    getline(cin, s);
    // string s = "djjcddjggbiigjhfghehhbgdigjicafgjcehhfgifadihiajgciagicdahcbajjbhifjiaajigdgdfhdiijjgaiejgegbbiigida";

    string result = reverseShuffleMerge(s);

    // cout << "Returned " << result << endl;

    fout << result << "\n";

    fout.close();

    return 0;
}
