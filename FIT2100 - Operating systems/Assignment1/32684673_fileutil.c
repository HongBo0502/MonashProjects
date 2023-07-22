/*	Name: Kang Hong Bo   		Student ID:32684673
 	Start Date: 18 Aug 2022 	Last Modified:24 AUG 2022
 	
 	
 	This default program use to read first 10 words from sample.txt.
	This program can take in 3 type of arguments which is 
	sourcefile: read the text from
	-a destfile : append to 
	-n numword : read how many words
 */
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/file.h> 
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include<stdio.h>
int main(int argc, char *argv[])
{
  struct stat dir;// create a struct to save the directory
  int i=1, x=1,outfile,exc=1,res;
  char c;
  int count=0;
  int number=10;
  int infile,y;
  
  	if(argv[1]!="-a"&&argv[1]!="-n"&&open(argv[1],O_RDONLY)>0){ //checking if the first argument is a directory 
  		if ((outfile = open(argv[1], O_RDONLY)) < 0) { //checking file exists or not
  			write(2,"File doesn't exists.\n",22);
  	 	 	exit(1);
  	 	 	}
  		}
  	else{
    		if ((outfile = open("sample.txt", O_RDONLY)) < 0) { //use the sample.txt if exists
 		write(2,"File doesn't exists.\n",22);
   	exit(1);
 		}
  	}
  	for(y=1;y<argc;y++){ //looping through arguments
  		if(strcmp(argv[y],"-a")==0){ //compare if the arguments is -a
  			stat(argv[y+1],&dir); //add destination file to the struct
  			if (S_ISDIR(dir.st_mode)) {//check if the directory IS A DIRECTORY
  				write(2,"Invalid argument.\n",20);
    			exit(1);
  				}
  			else{
  		 		if((infile = open(argv[y+1], O_RDWR | O_CREAT,0666)) < 0) { //if the file exist open else create
  		 			exit(1);
  					}
  			}
  		}
	  	if(strcmp(argv[y],"-n")==0){//check if the argument is -n
	  		if((atoi(argv[y+1]))>0){// check if the next argument is a number
	  			number=atoi(argv[y+1]);
	  		}
	  	}
  	}
	while (count<number && exc!=0){// do a loop which check if it get the specific number or 10 words was readed
		lseek(outfile,x,SEEK_SET);
		exc=read(outfile,&c,i);
		x++;
		if(c==' '){
			count++;
			}
		}
	int buf[x+1];
	buf[x+1]='\0';
	lseek(outfile,0,SEEK_SET);
	res=read(outfile,buf,x);//read 10 words since x will be the bytes where the count is exact same as the number/10.
	if(infile>0){ // check if infile exist else skip this step.
		lseek(infile,0,SEEK_END);
		write(infile,buf,res);
		close(infile);
		}
	else{
		write(1,buf,res);
		}

  	close(outfile);
 
  	exit(0);
}
