#include <stdio.h>

const char* oddeve(int num){
    if (num%2==0){
        return "even";
    } else{
        return "odd";
    }
}

int main(){
    int number;
    printf("Enter your number: ");
    scanf("%d",&number);
    const char* a = oddeve(number);
    printf("%s",a);
    return 0;
}