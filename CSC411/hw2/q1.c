#include <stdint.h>
#include <inttypes.h>
#include <stdio.h>


uint8_t get_upper_byte(uint16_t x) {
    // TODO
    return (x >> 8) & 0xFF;
}


int main(int argc, char* argv[]) {
    uint16_t x;
    scanf("%" SCNu16, &x);
    printf("%" PRIu8 "\n", get_upper_byte(x));

}
//gcc -o q1 q1.c && ./q1