#include iostream;

int apple[2];  /* integer array of size 2 */
apple[0] = 0;
apple[1] = 2;
foo(apple[0],apple[apple[0]]);
std::cout << (apple[0]) << std::endl;
std::cout << (apple[1]) << std::endl;

void foo(int a, int b) {
  a = 1;
  b = 3;
}
