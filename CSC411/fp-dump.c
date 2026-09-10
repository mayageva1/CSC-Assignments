#include <stdint.h>
#include <inttypes.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int bitLength(int exp, int frac){
    int totalBits = 1 + exp + frac; //the plus one is for the sign!!
    return totalBits;
}
void printBinaryString(int num, int length) {
    for (int i = length - 1; i >= 0; i--) {
        printf("%d", (num >> i) & 1);
    }
}

void specialNums(int signBit, int expBit, int fracBit, int exp, int bitString, int bitLength){
    if((expBit == (1 << exp) - 1) && fracBit == 0){  //if exp is all 1's and frac is all 0's
        if(signBit == 0){ //if sign is 0
            printBinaryString(bitString, bitLength);
            printf(" inf\n");
        } else {
            printBinaryString(bitString, bitLength);
            printf(" -inf\n");
        }
    } 
    else if ((expBit == (1 << exp) - 1) && fracBit != 0) { //if exp is all 1's and frac is not all 0's, meaning nan
        printBinaryString(bitString, bitLength);
        printf(" nan\n");
    }
}
void denormalized(int signBit, int expBit, int fracBit, int exp, int bitString, int bitLength){
    if(expBit == 0){ //if exp is all 0's
        printBinaryString(bitString, bitLength);
        int bias = ((1 << (exp - 1)) - 1); // compute de bias
        double fraction = (double)fracBit / (1 << (bitLength - 1 - exp)); // fraction / 2^numFracBits (shift the fraction to the right by the number of frac bits)
        double value = pow(-1, signBit) * fraction * pow(2, 1 - bias);   // exponent shiftaroli
        if (fracBit == 0 && signBit == 1) {
            printf(" -0.0");
        }
        else if (fracBit == 0 && signBit == 0) {
            printf(" 0.0");
        }
        else{
            printf(" %g", value); // Prints denormalized decimal value
        }
        printf("\n");
    }
}
void normalized(int signBit, int expBit, int fracBit, int exp, int bitString, int bitLength){
    if(expBit != 0 && expBit != (1 << exp) - 1){ //if the exp is not all 0's or all 1's
        printBinaryString(bitString, bitLength);
        printf(" ");
        int bias = ((1 << (exp - 1)) - 1); // compute de bias
        double fraction = 1.0 + (double)fracBit / (1 << (bitLength - 1 - exp)); // fraction / 2^numFracBits
        double exponent = expBit - bias; 
        double value = pow(-1, signBit) * fraction * pow(2, exponent);   // Apply exponent shift
        printf("%.17g", value); // Prints normalized decimal value
        printf("\n");
    }
}
void allValues(int signBit, int expBit, int fracBit, int exp, int bitString, int bitLength){
    printBinaryString(bitString, bitLength);
    printf(" ");
    if (expBit == (1 << exp) - 1) {
        if (fracBit != 0) {
            printf("nan");
        } else {
            printf("%sinf", signBit ? "-" : "");
        }
    } 
    else if (expBit == 0 && fracBit == 0) {
        printf("0.0");
    } 
    else if (expBit == 0) {
        double fracDecimal = 0.0;
        for (int i = 0; i < bitLength - 1 - exp; i++) {
            if ((bitString >> i) & 1) {
                fracDecimal += pow(2, -(i + 1));
            }
        }
        int bias = (1 << (exp - 1)) - 1;
        double value = pow(-1, signBit) * fracDecimal * pow(2, 1 - bias);
        printf(" %.2f", value);
    } 
    else {
        double fracDecimal = 1.0;
        for (int i = 0; i < bitLength - 1 - exp; i++) {
            if ((bitString >> i) & 1) {
                fracDecimal += pow(2, -(i + 1));
            }
        }
        int bias = (1 << (exp - 1)) - 1;
        double value = pow(-1, signBit) * fracDecimal * pow(2, expBit - bias);
        printf(" %.17g", value);
    }
    printf("\n");
}

int main(int argc, char* argv[]){
    //accept command line arguments
    int expNumy = atoi(argv[1]);
    int fracNumy = atoi(argv[2]);
    char output = argv[3][0];

    //Get the total length of bits
    int bitBoi = bitLength(expNumy, fracNumy);
    //printf("bitBoi length is %d", bitBoi);

    //loop through all possible bit combo's of totalBits
    for(int stringy = 0; stringy < (1 << bitBoi); stringy++){ //stringy being the bit string, 1 << bitBoi is the total number of possible bit strings

        //extract the sign, exp, and frac
        int signBits = (stringy >> (bitBoi - 1)) & 1; //right shift the sign bit to be in the lsb position, & 1 isolates and just checks that position
        int expBits = (stringy >> fracNumy) & ((1 << expNumy) - 1); //right shift to get just the expBits at the end of the string, create a bit mask of the explength, & to isolate just the exp
        int fracBits = stringy & ((1 << fracNumy) - 1); // create a bitmask of fraclength, & to isolate just the frac

        if(output == 's'){
            specialNums(signBits, expBits, fracBits, expNumy, stringy, bitBoi);
        }
        else if(output == 'd'){
            denormalized(signBits, expBits, fracBits, expNumy, stringy, bitBoi);
        }
        else if(output == 'n'){
            normalized(signBits, expBits, fracBits, expNumy, stringy, bitBoi);
        }
        else if(output == 'a'){
            allValues(signBits, expBits, fracBits, expNumy, stringy, bitBoi);
        }
    }
    return 0; //exit program
}

// gcc fp-dump.c -o bitBoithang && ./bitBoiThang 4 3 s