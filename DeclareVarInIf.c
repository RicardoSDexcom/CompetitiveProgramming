#include <stdio.h>
    
int main()
{
    if (({int a = 1;a;}))
        printf("Hello World: TRUE");
    else
        printf("Hello World: FALSE");

    return 0;
}
