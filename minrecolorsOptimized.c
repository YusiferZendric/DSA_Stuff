#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <limits.h>
int minimumRecolors(char* s, int k){
    int i=0,j=0,curr=0;
    int ans = INT_MAX;
    int n = strlen(s);
    while(j<n){
        if (s[j]=='W'){
            curr++;
        }
        if (j-i+1<k){
            j++;
        } else {
            if (ans>curr){
                ans = curr;
            }
            j++;
            if (s[i] == 'W'){
                curr--;
            }
            i++;

        }
    }
    return ans;    
}


int main(){
    int K;
    char S[1001];
    printf("Enter your String: ");
    scanf("%1000s",S);
    printf("Enter the streak: ");
    scanf("%d",&K);
    int res;
    res = minimumRecolors(S,K);
    printf("Output: %d",res);

    return 0;
}