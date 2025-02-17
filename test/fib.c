// fib.c

#include <stdio.h>

int fib(int n) {
    if (n == 0) {
        return 0;
    } else if (n == 1) {
        return 1;
    } else {
        return fib(n - 1) + fib(n - 2);
    }
}

int main() {
    int n = 10;
    printf("fib(%d) = %d\n", n, fib(n));
    return 0;
}