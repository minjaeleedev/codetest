#include <cstdio>
#include <iostream>
using namespace std;

int main() {
  freopen("paint.in", "r", stdin);
  freopen("paint.out", "w", stdout);

  int a, b;
  int c, d;
  cin >> a >> b;
  cin >> c >> d;
  int res = b - a;
  if (c > b || d < a) {
    res += d - c;
  } else {
    res += c < a ? a - c : 0;
    res += d > b ? d - b : 0;
  }

  cout << res;
}