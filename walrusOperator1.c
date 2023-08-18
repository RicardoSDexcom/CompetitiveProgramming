#include <stdio.h>
#include <stdlib.h>

int main() {
    char input[100];  // Buffer to store the input line
    int number;

    printf("Enter a number: ");
    
    const char *result = ((number = atoi(fgets(input, sizeof(input), stdin))) == 2) ? "Number is equal to 2.\n" : "Number is not equal to 2.\n";
    
    printf("%s\n", result);


    return 0;
}
