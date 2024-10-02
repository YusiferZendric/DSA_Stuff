#include <stdio.h>
#include <stdlib.h>
#include <strings.h>
#include <limits.h>

int minimumRecolors(char* blocks, int k) {
    int n = strlen(blocks);
    int* streaks = (int*)malloc(n * sizeof(int));
    int streaks_len = 0;

    for (int i = 0; i < n; i++) {
        if (blocks[i] == 'W') {
            streaks[streaks_len++] = 0;
        } else if (blocks[i] == 'B') {
            if (i > 0 && streaks_len > 0 && streaks[streaks_len - 1] != 0) {
                streaks[streaks_len - 1]++;
            } else {
                streaks[streaks_len++] = 1;
            }
        }
    }

    for (int i = 0; i < streaks_len; i++) {
        if (streaks[i] > k) {
            free(streaks);
            return 0;
        }
    }

    int minval = INT_MAX;

    for (int t = 0; t < streaks_len; t++) {
        int total_sum = 0;
        int changed = 0;
        for (int i = t; i < streaks_len; i++) {
            if (total_sum >= k) {
                break;
            }
            if (streaks[i] == 0) {
                total_sum++;
                changed++;
            } else {
                total_sum += streaks[i];
            }
        }
        if (total_sum >= k) {
            if (changed < minval) {
                minval = changed;
            }
        }
    }

    free(streaks);
    return minval;
}
