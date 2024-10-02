#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int randomnum, guess, chances = 10;
    srand(time(0));
    randomnum = rand() % 1000 + 1;
    printf("Guess the number (hint: number is between 1 to 1000):\n");
    while (chances > 0) {
        printf("Enter your guess: ");
        scanf("%d", &guess);
        if (guess == randomnum) {
            printf("You won! Correct Guess: %d\n", randomnum);
            break;
        } else if (guess > randomnum) {
            chances--;
            printf("Your guess is bigger, try again (chances left: %d)\n", chances);
        } else {
            chances--;
            printf("Your guess is smaller, try again (chances left: %d)\n", chances);
        }
        if (chances == 0) {
            printf("You've run out of chances! The correct number was %d\n", randomnum);
        }
    }
    return 0;
}