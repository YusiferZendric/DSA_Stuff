#include <stdio.h>

const char* leapOrNot(int year){
    if ((year%4==0&&year%100!=0)||(year%400==0)){
        return "Leap";
    } else {
        return "not a Leap";
    }
}

int main(){
    int num;
    printf("Enter year: ");
    scanf("%d",&num);
    const char* res = leapOrNot(num);
    printf("%d is %s Year", num,res);
}

