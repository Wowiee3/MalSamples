# include <stdio.h>
// # include <conio.h> Use conio.h for windows victims

int main(void) {
    FILE *stream;
    char buffer[80 + 1];
    int i, ch;

    stream = fopen("keylog.txt", "r");

    for (i = 0; (i < sizeof(buffer)-1) &&
             ((ch = fgetc(stream)) != EOF); i++)
    buffer[i] = '\0';

    if (fclose(stream))
        perror("fclose error");

    printf("line: %s\n", buffer);
}
