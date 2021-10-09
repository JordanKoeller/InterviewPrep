#include <bits/stdc++.h>

/**
 * Problem description
 * A string is said to be a special string if either of two conditions is met:

All of the characters are the same, e.g. aaa.
All characters except the middle one are the same, e.g. aadaa.

A special substring is any substring of a string which meets one of those criteria.
Given a string, determine how many special substrings can be formed from it.

Example

 contains the following  special substrings: .
 */

using namespace std;

// delta_state == -1 => Incrementing
// delta_state == 0 => Top of the mountain
// delta_state == 1 => Decrementing

struct palindrome_t
{
  int char_code;
  int reps_length;
};

long countSingleCharSubstrings(string &s)
{
  long c = 0;
  int i = 0;
  int j = 0;
  while (i < s.size() && j < s.size())
  {
    i = j;
    while (s[j] == s[i] && j < s.size())
    {
      j++;
      c += (j - i); // To grab all the different overlapping substrings.
    }
  }
  return c;
}

long countMirroredCharSubstrings(string &s)
{
  long counter = 0;
  vector<palindrome_t> repetitions;
  repetitions.push_back(palindrome_t {s[0] - 'a', 1});
  for (int i=1; i < s.size(); i++) {
    if (s[i] - 'a' == repetitions[repetitions.size() - 1].char_code) {
      repetitions[repetitions.size() - 1].reps_length++;
    } else {
      repetitions.push_back(palindrome_t {s[i] - 'a', 1});
    }
  }
  for (int i=1; i < repetitions.size() - 1; i++) {
    if (repetitions[i].reps_length == 1) {
      // We have a pivot point
      if (repetitions[i - 1].char_code == repetitions[i + 1].char_code) {
        counter += min(repetitions[i-1].reps_length, repetitions[i+1].reps_length);
      }
    }
  }
  return counter;
}

// Complete the substrCount function below.
long substrCount(int n, string s)
{
  long c_reps = countSingleCharSubstrings(s);
  long c_pal = countMirroredCharSubstrings(s);
  // cout << "found " << c_reps << " repeaters and " << c_pal << " for total " << c_pal + c_reps << "\n";
  return c_reps + c_pal;
}

int main()
{
  ofstream fout(getenv("OUTPUT_PATH"));

  int n;
  cin >> n;
  cin.ignore(numeric_limits<streamsize>::max(), '\n');

  string s;
  getline(cin, s);

  long result = substrCount(n, s);

  fout << result << "\n";

  fout.close();

  return 0;
}
