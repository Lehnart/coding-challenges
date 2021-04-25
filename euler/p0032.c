#include <string.h>
#include <stdlib.h>
#include <stdio.h>
int compute(char permutation_array[10]){
    char a_str[10];
    char b_str[10];
    char c_str[10];
    int a, b, c;

	for (int i=5; i<=7;i++){
        for(int j = 1; j<i;j++){
            memcpy( a_str, permutation_array, j );
            a_str[j] = '\0';
            memcpy( b_str, &permutation_array[j], i-j );
            b_str[i-j] = '\0';
            memcpy( c_str, &permutation_array[i], 10-i );
            c_str[10-i] = '\0';
            a = atoi(a_str);
            b = atoi(b_str);
            c = atoi(c_str);
            if (a*b == c) return c;
        }
	}
    return 0;
}
