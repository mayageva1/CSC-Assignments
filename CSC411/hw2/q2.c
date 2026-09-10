#include <stdint.h>
#include <inttypes.h>
#include <stdio.h>


uint8_t is_power_of_two(uint64_t x) {
    // TODO
    
    return x > 0 && ((x & (x - 1)) == 0);
}
void test_is_power_of_two() {
    uint64_t test_cases[] = {
        0, 1, 2, 3, 4, 5, 6, 7, 8, 16, 31, 32, 64, 127, 128, UINT64_MAX,
        1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576,
        999999, 1000000, 1000001, 2147483647, 2147483648, 4294967295, 4294967296
    };
    uint8_t expected_results[] = {
        0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        0, 0, 0, 0, 1, 0, 1
    };

    for (int i = 0; i < sizeof(test_cases) / sizeof(test_cases[0]); i++) {
        uint8_t result = is_power_of_two(test_cases[i]);
        printf("Test case %" PRIu64 ": expected %d, got %d\n",
               test_cases[i], expected_results[i], result);
    }
}

int main(int argc, char* argv[]) {
    //uint64_t x;
    //scanf("%" SCNu64, &x);
    //printf("%" PRIu8 "\n", is_power_of_two(x));
    test_is_power_of_two();
}
