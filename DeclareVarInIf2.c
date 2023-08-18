#include <stdio.h>

int main() {
    printf("%s\n", ({ const char *result = ({int a = 1;a;}) ? "Hello World: TRUE" : "Hello World: FALSE"; result; }));
    return 0;
}
