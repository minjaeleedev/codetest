#include <iostream>
using namespace std;

int main() {
  string scores;
  cin >> scores;

  int a = 0;
  int b = 0;
  for (int i = 0; i < scores.length(); i += 2) {
    if (scores[i] == 'A') {
      a += scores[i + 1] - '0';
    } else {
      b += scores[i + 1] - '0';
    }
  }

  if (a > b) {
    cout << "A" << endl;
  } else {
    cout << "B" << endl;
  }

  return 0;
}
