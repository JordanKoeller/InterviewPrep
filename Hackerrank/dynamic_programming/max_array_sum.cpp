#include <bits/stdc++.h>

using namespace std;

/**
 * 
 * Given an array of integers, find the subset of non-adjacent elements with the maximum sum.
 * Calculate the sum of that subset. It is possible that the maximum sum is 0,
 * the case when all elements are negative.
 * 
 * note: array can be up to 10^5 elements.
 * 
 * */

struct counter_t {
  int value;
  bool has_last;
  int prev_sum;
  // vector<int> added;
};

vector<string> split_string(string);

void increment_counter(counter_t &counter, int elem) {
  if (counter.has_last) {
    if (counter.prev_sum + elem > counter.value) {
      int tmp = counter.prev_sum;
      counter.prev_sum = counter.value;
      counter.value = tmp + elem;
      counter.has_last = true;
    } else {
      counter.has_last = false;
    }
  } else if (counter.value + elem > counter.value) {
    counter.prev_sum = counter.value;
    counter.value = counter.value + elem;
    counter.has_last = true;
  } else {
    counter.has_last = false;
  }
}

// Complete the maxSubsetSum function below.
// Memo
// Problem broken into smaller problems.

// Obvious smaller problem: maxSubsetSums of smaller sets of data.
int maxSubsetSum(vector<int> arr) {
  counter_t counter {0, false};
  for (int i=0; i < arr.size(); i++) {
    increment_counter(counter, arr[i]);
  }

  int ret = counter.value;
  // cout << "I found " << ret << endl;
  // if (ret == counter_1.value) {
  //   cout << "Solution from counter 1 with";
  //   for (auto e: counter_1.added) {
  //     cout << ", " << e;
  //   }
  //   cout << endl;
  // }
  // if (ret == counter_2.value) {
  //   cout << "Solution from counter 2 with";
  //   for (auto e: counter_2.added) {
  //     cout << ", " << e;
  //   }
  //   cout << endl;
  // }
  return ret;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    string arr_temp_temp;
    getline(cin, arr_temp_temp);

    vector<string> arr_temp = split_string(arr_temp_temp);

    vector<int> arr(n);

    for (int i = 0; i < n; i++) {
        int arr_item = stoi(arr_temp[i]);

        arr[i] = arr_item;
    }

    int res = maxSubsetSum(arr);

    fout << res << "\n";

    fout.close();

    return 0;
}

vector<string> split_string(string input_string) {
    string::iterator new_end = unique(input_string.begin(), input_string.end(), [] (const char &x, const char &y) {
        return x == y and x == ' ';
    });

    input_string.erase(new_end, input_string.end());

    while (input_string[input_string.length() - 1] == ' ') {
        input_string.pop_back();
    }

    vector<string> splits;
    char delimiter = ' ';

    size_t i = 0;
    size_t pos = input_string.find(delimiter);

    while (pos != string::npos) {
        splits.push_back(input_string.substr(i, pos - i));

        i = pos + 1;
        pos = input_string.find(delimiter, i);
    }

    splits.push_back(input_string.substr(i, min(pos, input_string.length()) - i + 1));

    return splits;
}
