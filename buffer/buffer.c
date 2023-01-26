#include <stdio.h>

int get_nth_value(int n) {
    int data[10] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    return data[n];
}

int main () {
    printf("first item: %d\n", get_nth_value(0));
    printf("last item: %d\n", get_nth_value(9));
    printf("after data end: %d\n", get_nth_value(10));
    printf("after buffer end: %d\n", get_nth_value(65536));
    printf("before buffer start: %d\n", get_nth_value(-1));

    return 0;
}