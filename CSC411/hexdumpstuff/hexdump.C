#include <stdio.h>
#include <stdlib.h>

// Function to print buffer in specified base
void printBuffer(unsigned char *buffer, long size, int bytesPerRow, char base) {
    for (long i = 0; i < size; i++) {
        if (i % bytesPerRow == 0) {
            fprintf(stdout, "\n%08lx: ", i);
        }
        if (base == 'x') {
            fprintf(stdout, "%02x ", buffer[i]);
        } else if (base == 'd') {
            fprintf(stdout, "%03d ", buffer[i]);
        }
    }
    fprintf(stdout, "\n");
}

int main(int argc, char *argv[]) {
    if (argc != 4) {
        fputs("Usage: <file> <bytes per row> <base>\n", stdout);
        return 1;
    }

    char *fileName = argv[1];
    int bytesPerRow = atoi(argv[2]);
    char base = argv[3][0];

    // Pointers for variables
    FILE *file;
    long lSize;
    unsigned char *buffer;
    size_t result;

    // Read binary file
    file = fopen(fileName, "rb");
    if (file == NULL) {
        fputs("File error\n", stdout);
        return 1;
    }

    // Get file size
    fseek(file, 0, SEEK_END);
    lSize = ftell(file);
    rewind(file);

    // Allocate memory
    buffer = (unsigned char *)malloc(sizeof(unsigned char) * lSize);
    if (buffer == NULL) {
        fputs("Memory error\n", stdout);
        fclose(file);
        return 2;
    }

    // Read file into buffer
    result = fread(buffer, 1, lSize, file);
    if (result != lSize) {
        fputs("Reading error\n", stdout);
        free(buffer);
        fclose(file);
        return 3;
    }

    // Print buffer
    printBuffer(buffer, lSize, bytesPerRow, base);

    // Terminate
    fclose(file);
    free(buffer);
    return 0;
}