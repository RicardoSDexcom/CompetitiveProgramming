#include <stdio.h>

int main() {
    printf("%s\n", ({ const char *result = "1"; result; }));
    return 0;
}
