#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

/*
 * Complete the 'abbreviation' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts following parameters:
 *  1. STRING a
 *  2. STRING b
 * 
 * You can perform the following operations on the string, a:

      Capitalize zero or more of a's lowercase letters.
      Delete all of the remaining lowercase letters in a.

Given two strings, a and b, determine if it's possible to 
make a equal to b as described. If so, print YES on a new line. Otherwise, print NO.

For example, given a = AbcDE and b = ABDE, in  we can convert b to B and delete c to match b.
If a = AbcDE and b = AFDE, matching is not possible because letters may only be capitalized
or discarded, not changed.

Constraints:
  1 <= q <= 10, where q is the number of queries
  a <= |a|, |b| <= 1000
  string a consists of [A-Za-z]
  string b consists of [A-Z]
 */

/**
 * This is similar to the Longest Common Subsequence problem.
 * 
 * 1. We compute the LCS between the string to match and the string-to-modify converted to all caps.
 * 
 * 1. If the string to match can be matched, then the Longest Common Subsequence will equal the string to match.
 * 2. If the string to match can be matched, then there must exist a subsequence of substrings in the string to modify
 *    that includes ALL characters that were originally capitalized.
 * 
 * What this constraint effectively means is I can only allow skips where the original character was lowercase.
 * Building that in:
 *   I can only skip going horizontal through the table and only while characters are lowercase.
 */

bool is_upper(char &c) {
  return c == toupper(c);
}

string abbreviation(string a, string b) {

  // a = string to modify
  // b = string to match

  vector<vector<bool>> memo {a.size() + 1, vector<bool>(b.size() + 1, false)};
  for (int i=0; i <= a.size(); i++) {
    memo[i][0] = true;
  }
  // for (int i=0; i <= b.size(); i++) {
  //   memo[0][i] = true;
  // }
  // Rows first, then column
  // r <==> String to Modify
  // c <==> String to match
  for (int rI=1; rI <= a.size(); rI++) {
    for (int cI=1; cI <= b.size(); cI++) {
      if (is_upper(a[rI-1])) {
        if (a[rI-1] == b[cI-1]) {
          memo[rI][cI] = memo[rI - 1][cI - 1];
        } else {
          memo[rI][cI] = false;
        }
      } else {
        if (toupper(a[rI-1]) == b[cI-1]) {
          memo[rI][cI] = memo[rI - 1][cI - 1] || memo[rI - 1][cI];
        } else {
          memo[rI][cI] = memo[rI - 1][cI];
        }
      }
    }
  }
  // cout << "Printing Table:" << endl;
  // for (int cI=0; cI < b.size(); cI++) {
  //   cout << " | " << b[cI] << " |";
  // }
  // cout << endl;
  // for (int rI=0; rI < a.size(); rI++) {
  //   cout << a[rI];
  //   for (int cI=0; cI < b.size(); cI++) {
  //     cout << "| " << memo[rI+1][cI+1] << " |";
  //   }
  //   cout << endl;
  // }
  // cout << "Done\n";
  if (memo[a.size()][b.size()]) {
    return "YES";
  } else {
    return "NO";
  }
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string q_temp;
    getline(cin, q_temp);

    int q = stoi(ltrim(rtrim(q_temp)));

    for (int q_itr = 0; q_itr < q; q_itr++) {
        string a;
        getline(cin, a);

        string b;
        getline(cin, b);

        string result = abbreviation(a, b);

        fout << result << "\n";
        cout << result << endl;
    }

    fout.close();

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}
