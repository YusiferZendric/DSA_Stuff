#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int randint(int r1, int r2)
{
    int randnum;
    while (randnum < r1)
    {

        srand(time(0));
        int place_value = 1;

        while (r2 >= 10)
        {
            r2 /= 10;
            place_value *= 10;
        }
        printf("%d",place_value);
        randnum = rand() % place_value;
    }
    return randnum;
}
int main()
{
    int num = randint(10,100);
    printf("%d",num);
    return 0;
}
