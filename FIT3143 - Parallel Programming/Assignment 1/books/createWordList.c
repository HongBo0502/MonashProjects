#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_WORD_COUNT 100
int main(){
    FILE *fp;
    char file[100]="";
    printf("Enter file name: ");
    scanf("%s", file);
    

    fp = fopen(file, "r");
    if(fp == NULL){
        printf("Error in opening file");
        exit(1);
    }
    //loop through the whole file and read each word and put it in a file called wordList.txt
    char word[MAX_WORD_COUNT];
    char fileName[100]="WL";
    strcat(fileName, file);
    while(fscanf(fp, "%s", word) != EOF){
        FILE *fp2;
        
        
        fp2 = fopen(fileName, "a");
        fprintf(fp2, "%s\n", word);
        fclose(fp2);
    }
    fclose(fp);
    return 0;
    
    
    

}