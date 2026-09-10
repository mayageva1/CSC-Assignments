#include <stdint.h>
#include <inttypes.h>
#include <stdio.h>


uint8_t is_negative(int16_t x) {
    // TODO
    return (x >> 15) & 1;
}


int main(int argc, char* argv[]) {
    int16_t x;
    scanf("%" SCNi16, &x);
    printf("%" PRIu8 "\n", is_negative(x));
}
