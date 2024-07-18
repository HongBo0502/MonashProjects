//serial matrix multiplcation 
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(){
    int i,j,k;
    int n = 1000;
    int **A = (int **)malloc(n * sizeof(int *));
    for (i=0; i<n; i++)
         A[i] = (int *)malloc(n * sizeof(int));
    int **B = (int **)malloc(n * sizeof(int *));
    for (i=0; i<n; i++)
         B[i] = (int *)malloc(n * sizeof(int));
    int **C = (int **)malloc(n * sizeof(int *));
    for (i=0; i<n; i++)
         C[i] = (int *)malloc(n * sizeof(int));
    for(i=0;i<n;i++){
        for(j=0;j<n;j++){
            A[i][j] = i;
            B[i][j] = j;
        }
    }
    struct timespec start, end;
    clock_gettime(CLOCK_MONOTONIC, &start);
    for(i=0;i<n;i++){
        for(j=0;j<n;j++){
            C[i][j] = 0;
            for(k=0;k<n;k++){
                C[i][j] += A[i][k]*B[k][j];
            }
        }
    }
    clock_gettime(CLOCK_MONOTONIC, &end);
    double time_spent = (end.tv_nsec - start.tv_nsec) / 1000000000.0 + (end.tv_sec  - start.tv_sec);
    printf("Time taken: %f\n",time_spent);
    FILE *fp;  
    fp = fopen ("serial.txt", "w+");
    for(i=0;i<n;i++){
        for(j=0;j<n;j++){
            fprintf(fp,"%d ",C[i][j]);
        }
        fprintf(fp,"\n");
    } 
    return 0;

}