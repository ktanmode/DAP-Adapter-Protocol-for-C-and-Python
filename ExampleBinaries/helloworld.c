#include <stdio.h>
#include <string.h>
#include <ctype.h>



int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("No Input\n");
        return 2;
    }
    char* hello = argv[1];
    printf("The input is: %s\n", hello);

    for (int i = 0; hello[i] != '\0'; i++) {
        if (isalpha(hello[i]) == 0 && isspace(hello[i]) == 0) {
            printf("Incorrect input: %c\n", hello[i]);
            return 3;  // Code for  incorrect symbol
        }
    }

    char* expected = "Hello World";

    if (strcmp(hello, expected) == 0) {
        printf("Hello World!\n");
        return 0;
    } else if (strlen(hello) < strlen(expected)) {
        printf("Unfinished Input\n");
        return -1;
    } else {
        printf("Finished, but incorrect\n");
        return 1;
    }
}
