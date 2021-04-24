#include <math.h>
#include <stdio.h>

long compute(){
	long result = 0;
	char number_str[10];
	for (int n=10; n<1000000;n++){

		sprintf(number_str, "%i", n);
		int i = 0;
		int number_sum = 0;
		while (number_str[i] != '\0') {
			char c = number_str[i];
			long l = c - '0';
			number_sum += l * l * l * l * l;
			i++;
		}
		if (number_sum == n) result += n;
	}
	return result;
}