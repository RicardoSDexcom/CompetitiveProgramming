#include <stdio.h>
    
int main()
{
    const char *result = ({int a = 1;a;}) ? "Hello World: TRUE" : "Hello World: FALSE";
    
    printf("%s\n", result);

    return 0;
}
