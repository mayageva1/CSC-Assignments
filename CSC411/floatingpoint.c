#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
void convertDecimalToBinary(int decimal, int numBits, char *binary){
    for(int i=0; i<numBits; i++){
        binary[numBits-i-1] = (decimal & (1 << i)) ? '1' : '0';
    }
    binary[numBits]= '\0';//terminate the string

}
void displayNumber(char *binary, int numExpBits, int numFracBits, char mode, int sign) {
    int exponentValue = 0; // Convert exponent to decimal
    for(int i = 0; i < numExpBits; i++) {
        exponentValue = (exponentValue << 1) | (binary[i + 1] - '0');
    }

    int fractionValue = 0; // Convert fraction to decimal
    for(int i = 0; i < numFracBits; i++) {
        fractionValue = (fractionValue << 1) | (binary[i + 1 + numExpBits] - '0');
    }
    int bias = ((1 << (numExpBits - 1)) - 1)/2;


    //special values, exponent all 1s
    if (mode == 's' && exponentValue == (1 << numExpBits) - 1) {
        printf("%s", binary);
        if(fractionValue != 0) {
            printf(" nan");
        } else {
            printf("%sinf", sign ? " -" : " ");
        }
        printf("\n");
    }

    //denormalized values, exponent all 0s, nonzero fraction
    if (mode == 'd' && exponentValue == 0) {
        //printf("%s", binary);
        int sign = binary[0] - '0';
        int bias = ((1 << (numExpBits - 1)) - 1);

        double fraction = (double)fractionValue / (1 << numFracBits); // fraction / 2^numFracBits
        double value = pow(-1, sign) * fraction * pow(2, 1 - bias);   // Apply exponent shift
        if (fractionValue == 0 && sign == 1) {
            printf("%s -0.0", binary);

        }
        else if (fractionValue == 0 && sign == 0) {
            printf("%s 0.0", binary);
        }
        else{
            printf("%s %g", binary, value); // Prints denormalized decimal value
        }
        printf("\n");
    }

    //normalized values, xponent is not all 0s or all 1s
    if (mode == 'n' && exponentValue != 0 && exponentValue != (1 << numExpBits) - 1) {
        int sign = binary[0] - '0';
        int bias = ((1 << (numExpBits - 1)) - 1); //(2^(numExpBits-1) - 1)

        double fraction = 1.0 + (double)fractionValue / (1 << numFracBits); // fraction / 2^numFracBits
        double exponent = exponentValue - bias;
        double value = pow(-1, sign) * fraction * pow(2, exponent);   // Apply exponent shift

        printf("%s %.17g", binary, value); // Prints denormalized decimal value
        printf("\n");
    }
    // All values
    if (mode == 'a') {
        printf("%s ", binary);
        //special cases
        if (exponentValue == (1 << numExpBits) - 1) {
            if(fractionValue != 0) {
                printf("nan");
            } else {
                printf("%sinf", sign ? "-" : "");
            }
        } 
        //zeroes
        else if(exponentValue == 0 && fractionValue == 0) {
            printf("0.0", sign ? " -" : "");
        }
        //denorm values
        else if(exponentValue == 0) {
            
            int sign = binary[0] - '0';
            int bias = ((1 << (numExpBits - 1)) - 1);
            double fraction = (double)fractionValue / (1 << numFracBits); // fraction / 2^numFracBits
            double value = pow(-1, sign) * fraction * pow(2, 1 - bias);   // Apply exponent shift
            if(value == 1 || value == -1){
                printf("%s", sign ? "-1.0" : "1.0");
            }
            else{
                printf(" %f", value); 
            }
        }
        //normalized values
        else {
            int bias = (1 << (numExpBits - 1)) - 1;  // Compute bias
            double fraction = 1.0 + (double)fractionValue / (1 << numFracBits); // Add implicit 1
            double value = pow(-1, sign) * fraction * pow(2, exponentValue - bias);
            printf(" %.17g", value);
            
        }
        printf("\n");
    }
}

int main(int argc, char* argv[]) {
    if (argc != 4) {
        fputs("Usage: <numExpBits> <numFracBits> <mode>\n", stdout);
        return 1;
    }
    //parse the command line arguments
    int numExpBits = atoi(argv[1]);
    int numFracBits = atoi(argv[2]);
    char mode = argv[3][0];
    
    int totalBits = 1 + numExpBits + numFracBits;
    char binary[totalBits + 1];

    //generate all possible floating point values, only print the ones that match the mode
    for (int sign = 0; sign <= 1; sign++) {
        for (int exp = 0; exp < (1 << numExpBits); exp++) {  // Exponent 1 to max-1
            for (int frac = 0; frac < (1 << numFracBits); frac++) {
               binary[0] = sign ? '1' : '0';
                convertDecimalToBinary(exp, numExpBits, binary + 1); //convert exponent
                convertDecimalToBinary(frac, numFracBits, binary + 1 + numExpBits); //convert fraction
                binary[totalBits] = '\0'; //terminate the string
                displayNumber(binary, numExpBits, numFracBits, mode, sign);
                }
            }
        }
    return 0;
}
