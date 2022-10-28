#include <stdio.h>

int mdc(int x, int y)
{
    if(y == 0)
    {
        return x;
    }
    else 
    {
        int z = y;
        y = x % y;
        x = z;
    }

    return mdc(x, y);
}
int main()
{
    int n1, n2;
    scanf("%d %d", &n1, &n2);
    int z = mdc(n1, n2);
    printf("%d\n", z);

    return 0;
}