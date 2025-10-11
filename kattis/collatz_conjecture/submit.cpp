#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
  long long n;
  cin >> n;

  vector<long long> result;
  while (n != 1) {
    result.push_back(n);
    if (n % 2 == 0) {
      n /= 2;
    } else {
      n = 3 * n + 1;
    }
  }

  result.push_back(n);

  vector<long long>::iterator it;
  for (it = result.begin(); it != result.end(); it++) {
    cout << *it << " ";
  }
  cout << endl;
}