#include <bits/stdc++.h>

using namespace std;

/**
 * A string is said to be a child of a another string if it can be formed
 * by deleting 0 or more characters from the other string. Letters cannot
 * be rearranged. Given two strings of equal length, what's the longest
 * string that can be constructed such that it is a child of both?
 * Example
 *   s1 = ABCD
 *   s2 = ABDC
 * 
 * These strings have two children with maximum length 3, ABC and ABD.
 * They can be formed by eliminating either the D or C from
 * both strings. Return 3.
 */

/*
 * Complete the 'commonChild' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. STRING s1
 *  2. STRING s2
 */

typedef unsigned long ind;



int commonChild(string s1, string s2)
{

  unsigned long n = s1.size() + 1;
  unsigned long m = s2.size() + 1;

  vector<vector<int>> memo(n, vector<int>(m, 0));

  // Construct a
  for (ind i = 0; i < s1.size(); i++)
  {
    for (ind j = 0; j < s2.size(); j++)
    {
      if (s1[i] == s2[j]) {
        memo[i+1][j+1] = memo[i][j] + 1;
      } else {
        memo[i+1][j+1] = max(memo[i+1][j], memo[i][j+1]);
      }
    }
  }
  // cout << "Finished constructing hashmap " << memo[s1.size()][s2.size()] << endl;

  return memo[s1.size()][s2.size()];
}

int main()
{
  ofstream fout(getenv("OUTPUT_PATH"));

  string s1;
  getline(cin, s1);

  string s2;
  getline(cin, s2);

  int result = commonChild(s1, s2);

  fout << result << "\n";

  fout.close();

  return 0;
}
