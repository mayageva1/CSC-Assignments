#include <stdint.h>
#include <inttypes.h>
#include <stdio.h>


uint16_t remove_element(uint16_t set, uint16_t id) {
    // TODO
    return set & ~(1 << id);
}


int main(int argc, char* argv[]) {
    uint16_t set;
    scanf("%" SCNu16, &set);
    uint16_t id;
    scanf("%" SCNu16, &id);
    printf("%" PRIu16 "\n", remove_element(set, id));
}
