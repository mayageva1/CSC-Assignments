#include <stdint.h>
#include <inttypes.h>
#include <stdio.h>


uint8_t swap(uint8_t x) {
        // Isolate the upper 4 bits and shift them to the lower 4 bits
        uint8_t upper = (x & 0xF0) >> 4;
        // Isolate the lower 4 bits and shift them to the upper 4 bits
        uint8_t lower = (x & 0x0F) << 4;
        // Combine the two nibbles
        return upper | lower;
}


int main(int argc, char* argv[]) {
    uint8_t x;
    scanf("%" SCNu8, &x);
    printf("%" PRIu8 "\n", swap(x));
}
