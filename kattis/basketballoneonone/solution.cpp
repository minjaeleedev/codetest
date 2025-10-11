#include <iostream>
using namespace std;

int main() {
  string scores;
  cin >> scores;
  // 어차피 기록 상 마지막 득점자가 승리자임
  cout << scores[scores.size() - 2];
}
