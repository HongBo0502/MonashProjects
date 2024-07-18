#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>
#include<time.h>
#include<omp.h>
#define MAX_WORD_COUNT 100

//z-algorithm
void z_algorithm(char *s, int *z, int n) {
    int l = 0, r = 0;
    z[0] = n;
    for (int i = 1; i < n; i++) {
        if (i > r) {
            l = r = i;
            while (r < n && s[r - l] == s[r]) r++;
            z[i] = r - l;
            r--;
        } else {
            int k = i - l;
            if (z[k] < r - i + 1) {
                z[i] = z[k];
            } else {
                l = i;
                while (r < n && s[r - l] == s[r]) r++;
                z[i] = r - l;
                r--;
            }
        }
    }
}
int checkUnique(char* word,char** uwList,int length){
    for(int i=0;i<length;i++){
        //use z-algorithm to check if the word is unique
        int* z =malloc(sizeof(int) * (MAX_WORD_COUNT));
        char* s=malloc(sizeof(char) * (MAX_WORD_COUNT));
        strcpy(s,word);
        strcat(s,"$");
        strcat(s,uwList[i]);
        z_algorithm(s,z,strlen(s));
        int j=strlen(word)+1;
        if(z[j]==strlen(word)){
            free(z);
            free(s);
            return 0;
        }
        free(z);
        free(s);
    }
    
    return 1;
}
//read 3 text file 
void read_File(char* txtfileName,int fileLength){
    FILE *fp;
    fp = fopen(txtfileName, "r");
    if(fp == NULL){
        printf("Error in opening file");
        exit(1);
    }
    struct timespec s,e,e1,e2;
    double time_spent;
    char word[MAX_WORD_COUNT];
    char **wList=malloc(sizeof(char*) * fileLength);
    char **uwList=malloc(sizeof(char*) * fileLength);
    printf("Reading %s\n",txtfileName);
    clock_gettime(CLOCK_MONOTONIC, &s);
    for(int i=0;i<fileLength;i++){
        //read each word
        fscanf(fp, "%s", word);
        //put each word in a list
        wList[i]=strdup(word);
        
        }
    fclose(fp);
    clock_gettime(CLOCK_MONOTONIC, &e);
    time_spent = (e.tv_nsec - s.tv_nsec) / 1000000000.0 + (e.tv_sec  - s.tv_sec);
    printf("Time taken to read: %f\n",time_spent);
    //check if the word is unique

    int UL=0;
    for(int i=0;i<fileLength;i++){
        for(int j=0;j<strlen(wList[i]);j++){
            wList[i][j]=tolower(wList[i][j]);
        }
        

    
    }
    clock_gettime(CLOCK_MONOTONIC, &e2);
    time_spent = (e2.tv_nsec - e.tv_nsec) / 1000000000.0 + (e2.tv_sec  - e.tv_sec);
    printf("Time taken to lower: %f\n",time_spent);

    #pragma omp parallel for num_threads(4) reduction(+:UL) 
    for(int i=0;i<fileLength;i++){
    
    if(checkUnique(wList[i],uwList,UL)==1){
            uwList[UL]=wList[i];
            UL++;
        }
    }
    clock_gettime(CLOCK_MONOTONIC, &e1);   
    time_spent = (e1.tv_nsec - e.tv_nsec) / 1000000000.0 + (e1.tv_sec  - e.tv_sec);
    printf("Time taken to check unique: %f\n",time_spent);

    free(wList);
    free(uwList);
    printf("Number of unique words: %d\n\n",UL);
    
}


int main(){
    //Files
    char* txtfileName[3]={"books/WLDracula.txt","books/WLRomeo_and_Juliet.txt","books/WLThe_Odyssey.txt"};
    //each files length
    int fileLength[3]={164442,28982,132519};
    struct timespec start, end;
    double time_spent;
    
    
    //read 3 text file 
    clock_gettime(CLOCK_MONOTONIC, &start);
    for(int i=0;i<3;i++){
        read_File(txtfileName[i],fileLength[i]);
        
    }
    clock_gettime(CLOCK_MONOTONIC, &end);
    time_spent = (end.tv_nsec - start.tv_nsec) / 1000000000.0 + (end.tv_sec  - start.tv_sec);
    printf("Total time taken: %f\n",time_spent);

    return 0;
    
}


