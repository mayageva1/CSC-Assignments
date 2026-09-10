#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

u_int32_t str_len(const char *s) {
    u_int32_t len = 0;
    while(s[len] != '\0') {
        len ++;
    }
    return len;
}

void str_reverse(const char *src, char *tgt, uint32_t n) {
    u_int32_t start = 0;
    u_int32_t end = n - 1;

    while(end >= 0) {
        tgt[end] = src[start];
        end --;
        start ++;
    }

    tgt[start] = '\0';
}

int main() {
    char str[] = "C for System Programming";
    char *reversed;
    u_int32_t len = str_len(str);

    reversed = malloc(len + 1);
    str_reverse(str, reversed, len);

    printf("%s\n", reversed);
    
    free(reversed); 
    return 0;
}