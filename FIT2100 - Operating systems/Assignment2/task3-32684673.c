/*	Name: Kang Hong Bo   		Student ID:32684673
 	Start Date: 6 OCT 2022 	Last Modified:8 OCT 2022
 	
 	A program that take in a default or sourcefile to read the process and 	
 	excute a shortest remaining service time schedule then output the  
 	scheduling and save the waitTime turnaroundTime and deadlineMet in a 
 	new text file. 
 	
	This program can take in 1 type of arguments which is 
	
	sourcefile: read the processs from

 */
/* Special enumerated data type for process state */
typedef enum{
	READY,RUNNING,EXIT,NOTREADY,WAITS,QUEUE
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
	int timeSlice;// the counter for the process

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
{	process_state_t READY=0,RUNNING=1,EXIT=2,NOTREADY=3,WAITS=4,QUEUE=5;
	//set int to the enum to compare
	pcb_t pr[100];
	//having a process not more then 100 (*specification)
	int infile,readfile,exc=1,x=0,count=0,spc=0;
	//open a file if it has and argument else the default file will be opened
	int i=1,ptr=0;
	char c;
	const int time_q=2;
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
				lseek(readfile,ptr,SEEK_SET);
				read(readfile,s,x-ptr);
				ptr=x+1;
				pr[count].serviceTime=atoi(s);
				pr[count].remainingTime=atoi(s);
			}
		}
			if(c=='\n'&&exc!=0){
				char s[x-ptr];
				lseek(readfile,ptr,SEEK_SET);
				read(readfile,s,x-ptr);
				ptr=x+1;
				pr[count].deadLine=atoi(s);
				pr[count].timeSlice=time_q;
				pr[count].state=NOTREADY;
				count++;
				spc=0;
			}
		x++;

		}
	pcb_e pe[count];
	//create the total space of the process for saving the results


	int time=0;
	int queue[count];
	int chk=0; 
	// check the total exit of the process
	//pr[max_service_pr].state!=EXIT
	while(chk!=count){
		int p = 1;
		int plc=0;
		for(p;p<=count;p++){
		
			if(pr[p-1].state==NOTREADY&& pr[p-1].entryTime<=time){
			//if the process is entered at the time then will print the string 
			//and change the state to READY
				printf("Time %d: %s has entered the system.\n",time,pr[p-1].process_name);
				pr[p-1].state=READY;
				}
			if(pr[p-1].state==READY){
			//put the process to queue 
				pr[p-1].state=QUEUE;
			for(plc;plc<count;plc++){
				if(queue[plc]<=0 || queue[plc]>count){
					//put it in if the current place is not a process
					queue[plc]=p;
					break;
				}
			}	
			}
			}
		plc=0;
		p = 1;
		int flag=0;
		int pr_min_r;
		int temp;

			for(p;p<=count;p++){
			//check from the second onwards index of the array and compare 	
			//with the first index change the smallest remainning time to 
			//the first index 
				if( queue[p]>0&&queue[p]<=count ){
				if(pr[queue[0]-1].remainingTime>pr[queue[p]-1].remainingTime){
				temp=queue[0];
				queue[0]=queue[p];
				queue[p]=temp;
				}
				else if (pr[queue[0]-1].remainingTime==pr[queue[p]-1].remainingTime){
				// if the remainning time is the same will choose the
				// smallest the smallest difference of the deadline 
				// or when the first index
					if(pr[queue[0]-1].deadLine-time>pr[queue[p]-1].deadLine-time||pr[queue[0]-1].deadLine-time<=0){
					temp=queue[0];
					queue[0]=queue[p];
					queue[p]=temp;
					}else{
						break;
					}
					
				}
			}else{
				
				break;
			}
		}

	
	pr_min_r=queue[0];
	//check if it is running then will just minus the remaining time
	if(pr[pr_min_r-1].state==RUNNING){
		pr[pr_min_r-1].remainingTime--;
	
	}
	//if is not running then the process will turn in running state and 
	// print the output string 
	if(pr[pr_min_r-1].state!=RUNNING){
		pr[pr_min_r-1].state=RUNNING;
		pr[pr_min_r-1].remainingTime--;
		printf("Time %d: %s is in the running state.\n",time,pr[pr_min_r-1].process_name);
	}
	//if the remaining time is zero it will print exit output
	//change the state of the process to exit.
	//the results will save at this statement.
	if(pr[pr_min_r-1].remainingTime==0){
		printf("Time %d: %s has exited the system.\n",time+1,pr[pr_min_r-1].process_name);
		pr[pr_min_r-1].state=EXIT;
		chk++;
		pe[pr_min_r-1].turnaroundTime=time+1-pr[pr_min_r-1].entryTime;
		pe[pr_min_r-1].waitTime=pe[pr_min_r-1].turnaroundTime-pr[pr_min_r-1].serviceTime;
		if(pr[pr_min_r-1].deadLine>=pe[pr_min_r-1].turnaroundTime){
					pe[pr_min_r-1].deadlineMet=1;
				}
				else{
					pe[pr_min_r-1].deadlineMet=0;
				}
			//move the queue one index forward
			for(int x=0;x<count-1;x++){
						queue[x]=queue[x+1];
					}
					queue[-1]=0;
	}
	time++;
	}
	//open a file if it doesnt exist it will create one and each time the file
	//will start the pointer at the beginning of the files.
	if((infile=open("results-3.txt",O_RDWR | O_TRUNC|O_CREAT,0666))<0){
		exit(1);
		}
	// loop through the results file.
	for(int p=0; p<count;p++){
		//create a string to store the results.
		char* outputString = (char*)malloc(2*sizeof(char));
		sprintf(outputString, "%s %d %d %d\n",pr[p].process_name,pe[p].waitTime,pe[p].turnaroundTime,pe[p].deadlineMet);
		write(infile,outputString,strlen(outputString));
	}
	close(readfile);
	close(infile);
	exit(0);

	}
