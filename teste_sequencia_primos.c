#include <stdio.h>
#include <time.h>
int primo(int y)
{
     if((y == 0)||(y == 1))
     {
     }
     else if((y == 2)||(y == 3)||(y == 5)||(y == 7))
     {
         printf("%d\n", y);    
     }
     else if((y % 2 == 0)||(y % 3 == 0))
     {   
     }
     else if((y % 5 == 0)||(y % 7 == 0))
     {    
     }
    else 
     {
         printf("%d\n", y);
     }

    primo(y + 1);
}

void teste()
{
    int y;
    int menor_um_minuto = 1;
    time_t inicio, atual;
    double duracao;
 
    time(&inicio);


    while (menor_um_minuto)
    {
        primo(y);
        time(&atual);
        
        duracao = difftime(atual, inicio);
        

        if (duracao >= 60)
        {
            menor_um_minuto = 0;
        }
    }
}

int main ()
{
  int x;
  teste();
  return 0;
}