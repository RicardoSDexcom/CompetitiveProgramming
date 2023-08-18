#include <stdio.h>
#include <stdlib.h>

int main() {
    char input[100];  // Buffer to store the input line
    int number;

    printf("Enter a number: ");
    fgets(input, sizeof(input), stdin);
    

    if ((number = atoi(input)) == 2) {
        printf("Number is equal to 2.\n");
    } else {
        printf("Number is not equal to 2.\n");
    }

    return 0;
}
