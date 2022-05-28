#include <stdio.h>
long fact(long n){
    if (n==0)return 1;
    return n*fact(n-1);
}

long compute(){
    char buffer[10];
    long solution =0;
    for(long n=3;n<10000000;n++){
        long fact_sum = 0;
        int ret = snprintf(buffer, sizeof(buffer), "%ld", n);
        int i = 0;
        while(buffer[i] != '\0'){
            fact_sum += fact( (long)(buffer[i] - '0'));
            i++;
        }
        if (fact_sum == n) solution += n ;
    }
    return solution;
}