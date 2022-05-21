#include <stdlib.h>
#include <stdio.h>

long compute(long* abundant_array, int abundant_size, int* sum_array, int sum_size){
    long s = 0;
    for (int i = 0; i < sum_size; i++) sum_array[i] = 0;

    for (int i = 0; i < abundant_size; i++) {
        for (int j = i; j < abundant_size; j++) {
            s = abundant_array[i] + abundant_array[j];
            if (s >= sum_size) break;
            sum_array[s] = 1;
        }
    }

    long sum = 0;
    for (int i = 0; i < sum_size; i++) {
        if (sum_array[i] == 0) sum += i;
    }
    return sum;
}