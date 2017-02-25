#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    char c[1001];

    scanf("%s", c);
    int counts[26];
    int i;
    for (i = 0; i < 26; ++i) counts[i] = 0;
    for (i = 0; i < n; ++i) {
        ++counts[c[i]-'a'];
    }
    char besta = 'a';
    int best = 0;
    for (i = 0; i < 26; ++i) {
        if (counts[i] > best) {

            best = counts[i];
            besta = i+'a';
        }
    }
    printf("%c %d\n", besta, best);
}
