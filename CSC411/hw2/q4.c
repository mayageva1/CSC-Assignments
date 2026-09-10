#include <stdint.h>
#include <inttypes.h>
#include <stdio.h>


uint16_t multiply_by_16(uint8_t x) {
    // TODO
    return uint16_t(x << 4);

}


int main(int argc, char* argv[]) {
    uint8_t x;
    scanf("%" SCNu8, &x);
    printf("%" PRIu16 "\n", multiply_by_16(x));
}
