#include <stdio.h>
#include <math.h>

double calculateCompoundInterest(double principal, double rate, int time, int n) {
    return principal * pow((1 + rate / (n * 100)), n * time);
}

int main() {
    double principal, rate, amount;
    int time, n;
    printf("Enter the principal amount: ");
    scanf("%lf", &principal);
    printf("Enter the annual interest rate (in percentage): ");
    scanf("%lf", &rate);
    printf("Enter the time (in years): ");
    scanf("%d", &time);
    printf("Enter the number of times interest is compounded per year: ");
    scanf("%d", &n);
    amount = calculateCompoundInterest(principal, rate, time, n);
    printf("The compound interest is: %.2lf\n", amount - principal);
    printf("The total amount after %d years is: %.2lf\n", time, amount);
    return 0;
}