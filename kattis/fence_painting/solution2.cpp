#include <iostream>
using namespace std;

/**
 * Fase Solution
 * area = (b - a) + (d - c) - intersection([a,b], [c,d])
 * if a <= x, c <= x, x < b, x < d,
 * an interval [x, x+1] is contained within both [a,b] and [c,d].
 * this is equivalent max(a, c) <= x < min(b, d)
 * therefore, the length of the intersection is min(b,d) - max(a,c)
 */
int main() {
  freopen("paint.in", "r", stdin);
  freopen("paint.out", "w", stdout);

  int a, b, c, d;
  cin >> a >> b >> c >> d;

  int total = (b - a) + (d - c);  // the sum of the two intervals
  int intersection =
      max(min(b, d) - max(a, c), 0);  // subtract the intersection
  int ans = total - intersection;

  cout << ans << "\n";
}