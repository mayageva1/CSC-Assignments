#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

void convertDecimalToBinary(int decimal, int numBits, char *binary){
    for(int i=0; i<numBits; i++){
        binary[numBits-i-1] = (decimal & (1 << i)) ? '1' : '0';
    }
    binary[numBits]= '\0';
}
void label(char *binary, int numExpBits, int numFracBits){
    int expBias = (1 << (numExpBits - 1)) - 1;
    int exponent = strtol(binary + 1, NULL, 2);  // Convert exponent to decimal
    int fractionValue = strtol(binary + 1 + numExpBits, NULL, 2); // Convert fraction to decimal
    char sign = (binary[0] == '1') ? '-' : '+';

    // Check for special cases
    if (exponent == (1 << numExpBits) - 1) { // All exponent bits = 1
        if (fractionValue == 0) { //fraction is all 0, exp is all 1
            printf(" %sinf", sign);
        } else {
            printf(" nan");  //fraction is nonzero, exp is all 1
        }
        return;
    }

    // Denormalized numbers (exponent = 0)
    if (exponent == 0) {
        double fractionDecimal = 0.0;
        for (int i = 0; i < numFracBits; i++) {
            if (binary[1 + numExpBits + i] == '1') {
                fractionDecimal += pow(2, -(i + 1));
            }
        }
        printf(" %.2f\n", pow(-1, binary[0] - '0') * fractionDecimal);
        return;
    }

    // Normalized numbers
    double fractionDecimal = 0.0;
    for (int i = 0; i < numFracBits; i++) {
        if (binary[1 + numExpBits + i] == '1') {
            fractionDecimal += pow(2, -(i + 1));
        }
    }

    double value = pow(-1, binary[0] - '0') * (1 + fractionDecimal) * pow(2, exponent - expBias);
    printf(" %.2f\n", value);
}

void displaySpecial(int numExpBits, int numFracBits){
    //list of binary numbers and their corresponding floating point values
    for (int i = 0; i <= 1; i++) {
        for (int j = 0; j < (1 << numFracBits); j++) {
            printf("%d", i);
            for (int x = 0; x < numExpBits; x++) {
                printf("%d", 1);
            }
            //int binary = convertDecimalToBinary(j);
            //printf("%d", binary);
            char str[16] = {0};
            convertDecimalToBinary(j, numFracBits, str);
            printf("%s", str);  
            printf("\n"); 
            //label(str, numExpBits, numFracBits);
        }
    }
}

void displayDenorm(int numExpBits, int numFracBits){
    for (int i = 0; i <= 1; i++) {
        for (int j = 0; j < (1 << numFracBits); j++) {
            printf("%d", i);
            for (int x = 0; x < numExpBits; x++) {
                printf("%d", 0);
            }
            //int binary = convertDecimalToBinary(j);
            //printf("%d", binary);
            char str[16] = {0};
            convertDecimalToBinary(j, numFracBits, str);
            printf("%s", str);
            label(str, numExpBits, numFracBits);
            printf("\n");
        }
    }
}   

void displayNorm(int numExpBits, int numFracBits){
    int totalBits = 1 + numExpBits + numFracBits;
    char binary[totalBits + 1];

    for (int sign = 0; sign <= 1; sign++) {
        for (int frac = 0; frac < (1 << numFracBits); frac++) {
            binary[0] = sign ? '1' : '0';
            memset(&binary[1], '0', numExpBits);
            convertDecimalToBinary(frac, numFracBits, binary + 1 + numExpBits);
            printf("%s", binary);
            label(binary, numExpBits, numFracBits);
        }
    }
}
void displayAll(int numExpBits, int numFracBits){
    int totalBits = 1 + numExpBits + numFracBits;
    char binary[totalBits + 1];

    for (int sign = 0; sign <= 1; sign++) {
        for (int exp = 1; exp < (1 << numExpBits) - 1; exp++) {  // Exponent 1 to max-1
            for (int frac = 0; frac < (1 << numFracBits); frac++) {
                binary[0] = sign ? '1' : '0';
                convertDecimalToBinary(exp, numExpBits, binary + 1);
                convertDecimalToBinary(frac, numFracBits, binary + 1 + numExpBits);
                printf("%s", binary);
                label(binary, numExpBits, numFracBits);
            }
        }
    }
}



int main(int argc, char* argv[]) {
    int numExpBits = atoi(argv[1]);
    int numFracBits = atoi(argv[2]);
    char mode = argv[3][0];
    if (argc != 4) {
        fputs("Usage: <numExpBits> <numFracBits> <mode>\n", stdout);
        return 1;
    }
    switch (mode) {
        case 's': // Special values
            displaySpecial(numExpBits, numFracBits);
            break;
        case 'd': // Denormalized values
            displayDenorm(numExpBits, numFracBits);
            break;
        case 'n': // Normalized values
            displayNorm(numExpBits, numFracBits);
            break;
        case 'a': // All values
            displayAll(numExpBits, numFracBits);
            break;
        default:
            printf("Invalid mode. Use 's', 'd', 'n', or 'a'.\n");
    }
    return 0;
}


//gcc hw4.c -o hw4  && ./hw4 3 4 s