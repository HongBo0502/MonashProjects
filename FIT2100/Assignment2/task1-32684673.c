/*	Name: Kang Hong Bo   		Student ID:32684673
 	Start Date: 5 OCT 2022 	Last Modified:8 OCT 2022
 	
 	A program that take in a default or sourcefile to read the process and 	
 	excute a First Come First Serve schedule then output the scheduling and 
 	save the waitTime turnaroundTime and deadlineMet in a new text file. 
 	
	This program can take in 1 type of arguments which is 
	
	sourcefile: read the processs from
	
 */
 
/* Special enumerated data type for process state */
typedef enum{
	READY,RUNNING,EXIT,NOTREADY
}process_state_t;

/* C data stucture used as process control block. The cheduler should create *  one instance per running process in the system.
*/
typedef struct {
	char process_name[11];// A string that identifies the process
	
	/* Times are measured in seconds. */
	int entryTime; // The time process entered system
	int serviceTime; // The total CPU time required by the process
	int remainingTime; // Remaining service time until completion.
	int deadLine; // The dead line of the processes

	process_state_t state; // current process state (e.g Ready).
}pcb_t;
typedef struct {
	/* Times are measured in seconds. */
	int waitTime; // The diffrence time of the service time and the finished time
	int turnaroundTime; // Total time to finish the process from the arrival time of the process
	int deadlineMet; // Be 1 when the finished time is lesser or equal to the deadline
}pcb_e;
#include <sys/file.h> 
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>
int main (int argc, char *argv[])
{	process_state_t READY=0,RUNNING=1,EXIT=2,NOTREADY=3;//set int to the enum to compare
	pcb_t pr[100];//having a process not more then 100 (*specification)
	int infile,readfile,exc=1,x=0,count=0,spc=0;
	int i=1,ptr=0;
	char c;
	//open a file if it has and argument else the default file will be opened
	if(open(argv[1],O_RDONLY)>0){
		if ((readfile = open(argv[1], O_RDONLY)) < 0) {
			write(2,"File doesn't exists.\n",22);
			exit(1);
		}
	}
	else{
		if ((readfile = open("processes.txt", O_RDONLY)) < 0) { 
 		write(2,"File doesn't exists.\n",22);
   	exit(1);
 		}
  	}
  	//saving the char in the file to the struct
  	while (exc != 0){
		lseek(readfile,x,SEEK_SET);
		exc=read(readfile,&c,1);

		if(c==' '){
			spc++;
			if(spc==1){
				char s[x-ptr];
				lseek(readfile,ptr,SEEK_SET);
				read(readfile,pr[count].process_name,x-ptr);
				ptr=x+1;



			}
			if(spc==2){
				char s[x-ptr];

				lseek(readfile,ptr,SEEK_SET);
				read(readfile,s,x-ptr);
				ptr=x+1;
				pr[count].entryTime=atoi(s);

				
			}
			if(spc==3){
				char s[x-ptr];
				int a;
				lseek(readfile,ptr,SEEK_SET);
				read(readfile,s,x-ptr);
				ptr=x+1;
				pr[count].serviceTime=atoi(s);
				pr[count].remainingTime=atoi(s)+1;
			}
		}
			if(c=='\n'&&exc!=0){
				char s[x-ptr];
				int a;
				lseek(readfile,ptr,SEEK_SET);
				read(readfile,s,x-ptr);
				ptr=x+1;
				pr[count].deadLine=atoi(s);
				pr[count].state=NOTREADY;
				count++;
				spc=0;
			}
		x++;
		}
		pcb_e pe[count];//create the total space of the process for saving the results
		int time=0;
	//if the last process doesn't exit it will continue runs
	while(pr[count-1].state!=EXIT){
		int p=0;
		for(p;p<count;p++){// loop through the process 
			if(pr[p].entryTime==time){
			//if the process is entered at the time then will print the string 
			//and change the state to READY 
				
				printf("Time %d: %s has entered the system.\n",time,pr[p].process_name);
				pr[p].state = READY;

				}
				
				if  (pr[p].state==READY&&(pr[p].remainingTime>0 && pr[p-1].remainingTime==0)){
				// check the state if the state is READY
				//if the remaining time of the previous process is  0 and the current is more than 0 the process will runs 
					printf("Time %d: %s is in the running state.\n",time,pr[p].process_name);
					pr[p].state=RUNNING;
					
				}
			// if the state is running will only decrement the remaining time
			if (pr[p].remainingTime>0 && pr[p].state==RUNNING){
				pr[p].remainingTime-=1;
				}
			// if the remaining time is equals zero, it will print the string and 
			//change the state of the process to exit.
			//the results will save at this statement.
			if(pr[p].state!=EXIT && pr[p].remainingTime==0){
				
				
				printf("Time %d: %s has exit the system.\n",time,pr[p].process_name);
				pr[p].state=EXIT;
			
				pe[p].turnaroundTime=time-pr[p].entryTime;
				pe[p].waitTime=pe[p].turnaroundTime-pr[p].serviceTime;
				if(pr[p].deadLine>=pe[p].turnaroundTime){
				pe[p].deadlineMet=1;
				}
				else{
				pe[p].deadlineMet=0;
				}
			}
		}
		time++;
	}
	//open a file if it doesnt exist it will create one and each time the file
	//will start the pointer at the beginning of the files.
	if((infile=open("results-1.txt",O_RDWR | O_TRUNC|O_CREAT,0666))<0){
		exit(1);
		}
	// loop through the results file.
	for(int p=0; p<count;p++){
		//create a string to store the results.
		char* outputString = (char*)malloc(13 *sizeof(char));
		sprintf(outputString, "%s %d %d %d\n",pr[p].process_name,pe[p].waitTime,pe[p].turnaroundTime,pe[p].deadlineMet);
		write(infile,outputString,strlen(outputString));
	}
	close(readfile);
	close(infile);
	exit(0);
}
	
