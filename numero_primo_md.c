#include <stdio.h>

int ser_primo(int y)
{
    if((y == 0)||(y == 1))
    {
        printf("Não é primo\n");
        return 0;
    }
    else if((y== 2)||(y == 3)||(y == 5)||(y == 7))
    {
        printf("É primo\n");
        return 0;
    }
    else if((y % 2 == 0)||(y % 3 == 0))
    {
        printf("Não é primo\n");
        return 0;
    }
    else if((y % 5 == 0)||(y % 7 == 0))
    {
        printf("Não é primo\n");
        return 0;
    }
    else
    {
        printf("É primo\n");
        return 0;
    }
    
    return ser_primo(y);
}
int main()
{
    int n;
    scanf("%d", &n);
    ser_primo(n);
    return 0;
}