#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <mpi.h>
#include <pthread.h>
#include <unistd.h>
#include <math.h>
#define Seed 35
#define MPI_End 1
#define MPI_Report 2
#define MPI_Check 3
#define MPI_Report_Check 4
#define MPI_Check_Neighbour 5
#define MPI_None_Report 6
#define SHIFT_ROW 0
#define SHIFT_COL 1
#define DISP 1
int end=0;
int station_rank;
int flag=0;
int flag2=0;
int base;
int* charging_port;
int n_charging_station;
int num_charging_port;
int neighbor_station;
int* lv2_neighbor_station;
int* station_report_state;
int row, col;
int cycle=0;
int num_check;
int base_station(MPI_Comm world_comm, MPI_Comm comm);
int charging_station(MPI_Comm world_comm, MPI_Comm comm);
void* base_station_thread(void* arg);
void* charging_port_thread(void* arg);
void* check_neighbor_thread(void* arg);
int main(int argc, char* argv[]){
    int rank, size, provided;
    
    MPI_Comm new_comm;
    MPI_Init_thread(&argc, &argv, MPI_THREAD_MULTIPLE, &provided);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);
    MPI_Comm_split(MPI_COMM_WORLD, rank==size -1, rank, &new_comm);
    if(argc == 3){
        row=atoi(argv[1]);
        col=atoi(argv[2]);
        num_charging_port=3;
        cycle=12;
    }
    else if (argc==4){
        row=atoi(argv[1]);
        col=atoi(argv[2]);
        num_charging_port=atoi(argv[3]);
        cycle=12;
    }
    else if (argc==5){
        row=atoi(argv[1]);
        col=atoi(argv[2]);
        num_charging_port=atoi(argv[3]);
        cycle=atoi(argv[4]);
    }
    else {
         if (size-1<4){
            /* error */
            printf("Error: Number of charging station must be greater than 4\n");
            MPI_Finalize();
            exit(0);
         }
         else{
            row=col=sqrt(size-1);
            num_charging_port=3;
            cycle=12;
         }
    }

    if(rank == size -1){
        base=rank;
        base_station(MPI_COMM_WORLD, new_comm);
    }else{
        charging_station(MPI_COMM_WORLD, new_comm);
    }
    MPI_Finalize();
    return 0;

}
/*Base station*/
int base_station(MPI_Comm world_comm, MPI_Comm comm){
    int size,time=0;
    MPI_Comm_size(world_comm, &size);
    n_charging_station= size -1;
    pthread_t tid;
    pthread_create(&tid, 0, base_station_thread, &n_charging_station);
    /*base log*/
   
    while (time<cycle){
        printf("Time: %d\n", time+1);
        num_check=0;
        station_report_state=(int*)malloc(n_charging_station*sizeof(int));
        for (int i=0; i<n_charging_station; i++){
            station_report_state[i]=0;
        }
        
        sleep(2);
        // for (int i=0; i<n_charging_station; i++){
        //     printf("station_report_state[%d]: %d\n", i, station_report_state[i]);
        // }
        
        time++;
    }
    end=1;
    pthread_join(tid, 0);
    
    for (int i=0; i<n_charging_station; i++){
        // printf("I am sending end to %d\n", i);
        MPI_Send(&end, 1, MPI_INT, i, MPI_End, MPI_COMM_WORLD);
    }
    
    return 0;
}

void* base_station_thread(void* arg){
    // int* n_charging_station=(int*)arg;
    MPI_Status status;
    FILE *fp;
    char buffer[100];
    MPI_Request Send_Request[4];
    MPI_Request Recv_Request[4];
    MPI_Status Send_Status[4];
    MPI_Status Recv_Status[4];
    int flag=0;
    sprintf(buffer, "log_base.txt");
    fp=fopen(buffer, "w");
    if (fp==NULL){
        printf("Error opening file!\n");
        exit(1);
    }
    while(!end && !flag){
        MPI_Iprobe(MPI_ANY_SOURCE, MPI_Report, MPI_COMM_WORLD, &flag, &status);
        if (flag){
            // printf("flag: %d\n", flag);
            int rank=0;

            int time=0;

            int *neighbor;
            neighbor=(int*)malloc(4*sizeof(int));
            
            int count=0;
            // printf("BASE +++ Number of charging station: %d\n", n_charging_station);

            switch(status.MPI_TAG){
                case MPI_Report:
                    int **neighbor_rank;
                    neighbor_rank=(int**)malloc(n_charging_station*sizeof(int*));
                    for (int i=0; i<n_charging_station; i++){
                        neighbor_rank[i]=(int*)malloc(4*sizeof(int));
                    }
                    for (int i=0; i<n_charging_station; i++){
                        for (int j=0; j<4; j++){
                            neighbor_rank[i][j]=-2;
                        }
                    }
                    int **neighbor_available_port;
                    neighbor_available_port=(int**)malloc(n_charging_station*sizeof(int*));
                    for (int i=0; i<n_charging_station; i++){
                        neighbor_available_port[i]=(int*)malloc(4*sizeof(int));
                    }
                    for (int i=0; i<n_charging_station; i++){
                        for (int j=0; j<4; j++){
                            neighbor_available_port[i][j]=-2;
                     
                       }
                    }
                    MPI_Recv(&rank, 1, MPI_INT, MPI_ANY_SOURCE, MPI_Report, MPI_COMM_WORLD, &status);
                    MPI_Recv(&time, 1, MPI_INT, rank, MPI_Report, MPI_COMM_WORLD, &status);
                    MPI_Recv(neighbor, 4, MPI_INT, rank, MPI_Report, MPI_COMM_WORLD, &status);
                    fprintf(fp, "_____________________________________________________\n");
                        station_report_state[rank]=1;
                        fprintf(fp, "Report from station %d at time %d\n", rank, time+1);
                        fflush(fp);
                        // printf("Report from station %d at time %d\n", rank, time+1);
                    for (int i=0; i<4; i++){
                        fprintf(fp, "Neighbor %d: %d\n", i, neighbor[i]);
                    
                        
                        fflush(fp);
                    }
                    for (int i=0; i<n_charging_station; i++){
                        fprintf(fp, "station_report_state[%d]: %d\n", i, station_report_state[i]);
                        fflush(fp);
                    }
                    for (int i=0; i<4; i++){
                        if (neighbor[i]!=-2 && station_report_state[neighbor[i]]==0){
                            fprintf(fp, "Station %d is checking for station %d\n", rank, neighbor[i]);
                            MPI_Isend(&base, 1, MPI_INT, neighbor[i], MPI_Check_Neighbour, MPI_COMM_WORLD, &Send_Request[count]);
                            // MPI_Irecv(&neighbor_rank, 1, MPI_INT, neighbor[i], MPI_Check_Neighbour, MPI_COMM_WORLD, &Recv_Request[count]);
                            MPI_Irecv(neighbor_rank[neighbor[i]], 4, MPI_INT, neighbor[i], MPI_Check_Neighbour, MPI_COMM_WORLD, &Recv_Request[count]);
                            MPI_Irecv(neighbor_available_port[neighbor[i]], 4, MPI_INT, neighbor[i], MPI_Check_Neighbour, MPI_COMM_WORLD, &Recv_Request[count]);
                            count++;
                            
                        }
                        else if(station_report_state[neighbor[i]]==1){
                            fprintf(fp, "Station %d has reported \n", neighbor[i]);
                        }
                        

                    }
                    // fprintf(fp, "Count: %d at time %d\n", count, time);
                    fflush(fp);
                    MPI_Waitall(count, Send_Request, Send_Status);
                    MPI_Waitall(count, Recv_Request, Recv_Status);
                    int cnt=0;
                    for (int i=0; i<n_charging_station; i++){
                        for (int j=0; j<4; j++){
                        // fprintf(fp, "Neighbor rank: %d and Available port: %d\n", neighbor_rank[i][j], neighbor_available_port[i][j]);
                        if (neighbor_rank[i][j]!=-2 && neighbor_available_port[i][j]>0 && neighbor_rank[i][j]!=rank){
                            cnt++;
                            fprintf(fp, "Report from station %d --- Neighbor rank: %d has %d available ports\n", i ,neighbor_rank[i][j], neighbor_available_port[i][j]);
                            fflush(fp);
                        }  
                        }}
                    if (cnt==0){
                        fprintf(fp, "No available ports\n");
                        fflush(fp);
                    }
                    // Calculate the total size of data to be packed
                    int pack_size, position = 0;
                    MPI_Pack_size(n_charging_station * 4 * 2, MPI_INT, MPI_COMM_WORLD, &pack_size);
                    
                    // Allocate a buffer for packing
                    char *buffer = (char*)malloc(pack_size);
                    for (int i=0;i<n_charging_station;i++){
                        MPI_Pack(neighbor_rank[i], 4, MPI_INT, buffer, pack_size, &position, MPI_COMM_WORLD);
                        MPI_Pack(neighbor_available_port[i], 4, MPI_INT, buffer, pack_size, &position, MPI_COMM_WORLD);
                    }
                    // Send the packed data to the destination
                    MPI_Send(buffer, position, MPI_PACKED, rank, MPI_Report_Check, MPI_COMM_WORLD);
                    for (int i=0; i<4; i++){
                        neighbor[i]=-2;
                    }
                    
                    break;

            }
            
        }
        
        flag=0;
        
    }
    // printf("Base station is closed\n");
    
    return 0;
}


/*Charging station*/
int charging_station(MPI_Comm world_comm, MPI_Comm comm){
    
    int ndims=2, size, rank, reorder, my_cart_rank, ierr,base_station_size;
    
    int dims[ndims], coord[ndims];
    int wrap_around[ndims];
    int nbr_i_lo, nbr_i_hi;
    int nbr_j_lo, nbr_j_hi;
    MPI_Comm comm2D;
    FILE *fp;
    
    MPI_Comm_size(world_comm, &base_station_size);
    MPI_Comm_size(comm, &size);
    MPI_Comm_rank(comm, &rank);
    n_charging_station=size;
    dims[0]=row;
    dims[1]=col;
    MPI_Request send_request[size];
    MPI_Request recv_request[size];
    MPI_Status send_status[size];
    MPI_Status recv_status[size];
    MPI_Dims_create(size, ndims, dims);
    // if(rank == 0){
    //     printf("Charging Station: %d. Comm Szie: %d: Grid Dimension = [%dx%d]\n", rank, size, dims[0], dims[1]);
    // }
    /*create cartesian topology for processes*/
    wrap_around[0]=wrap_around[1]=0; /*periodic shift is false*/
    reorder=1;
    ierr=MPI_Cart_create(comm, ndims, dims, wrap_around, reorder, &comm2D);
    if(ierr !=0) printf("ERROR[%d] creating CART\n", ierr);
    /*find my coordinates in the cartesian communicator group*/
    MPI_Cart_coords(comm2D, rank, ndims, coord);
    /*use my cartesian coordinates to find my rank in cartesian group*/
    MPI_Cart_rank(comm2D, coord, &my_cart_rank);
    
    /*Neighbor rank*/
    MPI_Cart_shift(comm2D, SHIFT_ROW, DISP, &nbr_i_lo, &nbr_i_hi);
    MPI_Cart_shift(comm2D, SHIFT_COL, DISP, &nbr_j_lo, &nbr_j_hi);
    int neighbor[4]= {nbr_i_lo, nbr_i_hi, nbr_j_lo, nbr_j_hi};
    lv2_neighbor_station=(int*)malloc(4*sizeof(int));
    for (int i=0; i<4; i++){
        lv2_neighbor_station[i]=neighbor[i];
    }
    /*print neighbor out*/
    // for (int i=0; i<4; i++){
    //     printf("Charging Station: %d. Comm Szie: %d: My Neighbor[%d] = %d\n", rank, size, i, neighbor[i]);
    // }
    // printf("Charging Station: %d. Comm Szie: %d: My Cart Rank = %d. My Coord = (%d, %d)\n", rank, size, my_cart_rank, coord[0], coord[1]);
    fflush(stdout);
    /*create charging port*/
    //create a array of size 5 all to be 0
    
    charging_port=(int*)malloc(num_charging_port*sizeof(int));
    pthread_t tid[num_charging_port];
    pthread_t tid2;
    station_rank=my_cart_rank;
    //int available_port_count=0;
    MPI_Status status;
    /*assign random 1 and 0 to charging port*/
    srand(Seed+my_cart_rank);
    for (int i=0; i<num_charging_port; i++){
        charging_port[i]=rand()%2;
    }
    //print out the array
    
    for (int i=0; i<num_charging_port; i++){
        int *id=(int*)malloc(sizeof(int));
        *id=i;
        pthread_create(&tid[i], 0, charging_port_thread, id);    
    }
    pthread_create(&tid2, 0, check_neighbor_thread, &comm2D);
    int flag=0,flag2=0;
    int value;
    char buffer[100];
    struct timespec s,e,bs,be;
    double timespent;
    
    sprintf(buffer, "log_station_%d.txt", rank);

    fp=fopen(buffer, "w");
    if (fp==NULL){
        printf("Error opening file!\n");

        exit(1);
    }
    int iter=0;
    while(!end && !flag2 && !flag){
        
        
        //update log file
        int available_port_count=0;
        
        
        MPI_Iprobe(MPI_ANY_SOURCE, MPI_ANY_TAG, world_comm, &flag, &status);
    
        
        if (flag){
            MPI_Recv(&value, 1, MPI_INT, MPI_ANY_SOURCE, MPI_ANY_TAG, world_comm, &status);
           
        
        switch(status.MPI_TAG){
                
                case MPI_End:
                    end=1;
                    // printf("Charging station %d is closed\n", rank);
                    break;
                    
                
                

        }
        flag=0;
        }
        
        else{    
            // printf("Time: %d\n", time);
        
        available_port_count=0;
        fprintf(fp, "\nStation %d iteration %d\n", rank, iter);
        fprintf(fp, "Time: %d\n", iter+1);
        for (int i=0; i<num_charging_port; i++){
            fprintf(fp, "Port %d:%d\n",i, charging_port[i]);
        }
        fflush(fp);    
        for (int i=0; i<num_charging_port; i++){
            if (charging_port[i]==0){
                available_port_count++;
            }
        }
        
        fprintf(fp, "Station %d has %d available ports\n", rank, available_port_count);
        fflush(fp);
        // for (int i=0; i<n; i++){
        // printf("Port %d:%d\n",i, charging_port[i]);
        // }
        // printf("Station %d has %d available ports\n", rank, available_port_count);
        
        int value_arr[size];
        for (int i=0; i<size; i++){
            value_arr[i]=-2;
        }
        // printf("Station %d has %d available ports\n", rank, available_port_count);
        int threshold=0;
        threshold=ceil((float)num_charging_port*20/100);
        // printf("Threshold: %d\n", threshold);
        if (available_port_count<=threshold){
            num_check++;
            /*check neighbor*/
            int count=0;
            clock_gettime(CLOCK_MONOTONIC, &s);
            for(int i=0; i<4; i++){
                if (neighbor[i]!=-2){
                    // printf("Count: %d\n", count);
                    // printf("Station_rank: %d\n", station_rank);
                    fprintf(fp, "Station %d is checking neighbor %d\n", rank, neighbor[i]);
                    fflush(fp);
                    MPI_Isend(&station_rank, 1, MPI_INT, neighbor[i], MPI_Check, comm2D, &send_request[count]);
        
                    MPI_Irecv(&value_arr[i], 1, MPI_INT, neighbor[i], MPI_Report_Check, comm2D, &recv_request[count]);
                    
                    printf("Neighbor %d is checking\n", neighbor[i]);
                    count++;
                }   
            }
            
            // printf("count: %d\n", count);
            MPI_Waitall(count, send_request, send_status);
            MPI_Waitall(count, recv_request, recv_status);
            
            
            // printf("Stastion %d received from neighbor\n", rank);
            // for (int i=0; i<size; i++){
            //     // printf("value_arr[%d]: %d\n", i, value_arr[i]);
            // }
            int neighbor_availibility=0;
            for (int i=0; i<size; i++){
                if (value_arr[i]>threshold){
                    neighbor_availibility++;
                    fprintf(fp, "From Station %d has %d available ports\n", neighbor[i], value_arr[i]);
                    fflush(fp);
                }

            }
            clock_gettime(CLOCK_MONOTONIC, &e);
            timespent= (e.tv_nsec-s.tv_nsec)/1000000000.0;
            printf("Station %d - Time spent for checking neighbor: %f\n", rank, timespent);
            fprintf(fp, "Station %d - Time spent for checking neighbor: %f\n", rank, timespent);
            int** lv2_neighbor_rank;
            int** lv2_neighbor_availibility;
            lv2_neighbor_rank=(int**)malloc(n_charging_station*sizeof(int*));
            for (int i=0; i<n_charging_station; i++){
                lv2_neighbor_rank[i]=(int*)malloc(4*sizeof(int));
            }
            for (int i=0; i<n_charging_station; i++){
                for (int j=0; j<4; j++){
                    lv2_neighbor_rank[i][j]=-2;
                }
            }
            lv2_neighbor_availibility=(int**)malloc(n_charging_station*sizeof(int*));
            for (int i=0; i<n_charging_station; i++){
                lv2_neighbor_availibility[i]=(int*)malloc(4*sizeof(int));
            }
            for (int i=0; i<n_charging_station; i++){
                for (int j=0; j<4; j++){
                    lv2_neighbor_availibility[i][j]=-2;
                }
            }
            clock_gettime(CLOCK_MONOTONIC, &bs);
            if(neighbor_availibility==0){
                // for(int i=0;i<4;i++){
                //     fprintf(fp, "Sending my neighbor %d to base station\n", neighbor[i]);
                //     fflush(fp);
                // }
                fprintf(fp, "Iter %d - Station %d neighbours has no available ports\n", iter, rank);
                fprintf(fp, "Sending my rank %d iter %d to base station\n", rank, iter);
                fflush(fp);

            
            MPI_Send(&rank, 1, MPI_INT,base_station_size-1, MPI_Report, world_comm);
            MPI_Send(&iter,1,MPI_INT,base_station_size-1,MPI_Report,world_comm);
            //send neighbor
            MPI_Send(lv2_neighbor_station,4,MPI_INT,base_station_size-1,MPI_Report,world_comm);
            
            
            
            int recv_position=0;
            int recv_buffer_size=0;
            MPI_Pack_size(n_charging_station * 4 * 2, MPI_INT, MPI_COMM_WORLD, &recv_buffer_size);
            char *recv_buffer = (char*)malloc(recv_buffer_size);
            MPI_Recv(recv_buffer, recv_buffer_size, MPI_PACKED, base_station_size-1, MPI_Report_Check, MPI_COMM_WORLD, &status);
            fprintf(fp, "Station %d received from base station\n", rank);
            fflush(fp);

            // printf("unpacking\n");
            for(int i=0;i<n_charging_station;i++){
                MPI_Unpack(recv_buffer,recv_buffer_size,&recv_position,lv2_neighbor_rank[i],4,MPI_INT,MPI_COMM_WORLD);
                MPI_Unpack(recv_buffer,recv_buffer_size,&recv_position,lv2_neighbor_availibility[i],4,MPI_INT,MPI_COMM_WORLD);
            }
            // printf("Num of charging station: %d\n", n_charging_station);
            int count_lv2=0;
            int lv2_result[n_charging_station];
            for (int i=0; i<n_charging_station; i++){
                lv2_result[i]=-2;
            }
            for(int i=0;i<n_charging_station;i++){
                for(int j=0;j<4;j++){
                    if(lv2_neighbor_rank[i][j]!=-2 && lv2_neighbor_availibility[i][j]>threshold && lv2_neighbor_rank[i][j]!=rank && lv2_result[lv2_neighbor_rank[i][j]]==-2){
                        count_lv2++;
                        lv2_result[lv2_neighbor_rank[i][j]]=lv2_neighbor_rank[i][j];
                        fprintf(fp, "Station %d has %d available ports\n", lv2_neighbor_rank[i][j], lv2_neighbor_availibility[i][j]);
                        fflush(fp);
                    }
                }
            }
            // for(int i=0;i<n_charging_station;i++){
            //     for(int j=0;j<4;j++){
                    
            //         //fprintf(fp, "Station %d has %d available ports\n", lv2_neighbor_rank[i][j], lv2_neighbor_availibility[i][j]);
            //         if(lv2_neighbor_rank[i][j]!=-2 && lv2_neighbor_availibility[i][j]>0){
            //             count_lv2++;
            //             fprintf(fp, "Station %d has %d available ports\n", lv2_neighbor_rank[i][j], lv2_neighbor_availibility[i][j]);
            //             fflush(fp);
            //         }
                    
            //     }
            // }
            if (count_lv2==0){
                fprintf(fp, "Station %d has no available ports\n", rank);
                fflush(fp);
            }
            clock_gettime(CLOCK_MONOTONIC, &be);
            timespent= (be.tv_nsec-bs.tv_nsec)/1000000000.0;
            printf("Station %d - Time spent for checking lv2 neighbor: %f\n", rank, timespent);
            fprintf(fp, "Station %d - Time spent for checking lv2 neighbor: %f\n", rank, timespent);
            }
            else{
                fprintf(fp, "Station %d neighbours has available ports\n", rank);
                fflush(fp);
            
            }



        
        
        }
        
        
        // time++;
        }
        
        sleep(2);
        iter++;
    }
    
    

    
    for (int i=0; i<num_charging_port; i++){
        pthread_join(tid[i], 0);
        
    } 
    pthread_join(tid2, 0);
    // printf("Thread is closed for station %d\n", rank);
    fclose(fp); 
    // printf("TT Charging station %d is closed\n", rank);
    
    return 0;
}
void *check_neighbor_thread(void*arg){
    MPI_Comm* comm2D=(MPI_Comm*)arg;
    MPI_Status status;
    int rank;
    int availability=-1;
    while (!end){
        MPI_Iprobe(MPI_ANY_SOURCE, MPI_Check, *comm2D, &flag, &status);
        MPI_Iprobe(MPI_ANY_SOURCE, MPI_Check_Neighbour, MPI_COMM_WORLD, &flag2, &status);
        if (flag){
            
            MPI_Recv(&neighbor_station, 1, MPI_INT, MPI_ANY_SOURCE, MPI_Check, *comm2D, &status);

            // printf("Station %d is checking for station %d\n", station_rank, neighbor_station);
            switch(status.MPI_TAG){
                case MPI_Check:
                    int available_port_count=0;
                    for (int i=0; i<num_charging_port; i++){
                        if (charging_port[i]==0){
                            available_port_count++;
                        }
                            
                    }
                    // printf("Station %d has %d available ports for refference\n", station_rank, available_port_count);
                    if (available_port_count>0){
                        MPI_Send(&available_port_count, 1, MPI_INT, neighbor_station, MPI_Report_Check, *comm2D);
                    }
                    else{
                        availability=0;
                        MPI_Send(&availability, 1, MPI_INT, neighbor_station, MPI_Report_Check, *comm2D);
                    }
                    

                    
                   
                    break;
            }
        }
        if (flag2){
            // int available_port_count=0;
            int *lv2_neighbor_available_port;
            lv2_neighbor_available_port=(int*)malloc(4*sizeof(int));
            for (int i=0; i<4; i++){
                lv2_neighbor_available_port[i]=-2;
            }
            MPI_Recv(&rank,1,MPI_INT,MPI_ANY_SOURCE,MPI_Check_Neighbour,MPI_COMM_WORLD,&status);
            // for (int i =0;i<4;i++){
            //     printf("LV2 neighbor station %d\n",lv2_neighbor_station[i]);
            // }
            /*check my neighbour*/
            for (int i=0; i<4;i++){
                if (lv2_neighbor_station[i]!=-2){
                    // printf("lv2 Station %d is checking for station %d\n", station_rank, lv2_neighbor_station[i]);
                    MPI_Send(&station_rank,1,MPI_INT,lv2_neighbor_station[i],MPI_Check,*comm2D);
                    MPI_Recv(&lv2_neighbor_available_port[i],1,MPI_INT,lv2_neighbor_station[i],MPI_Report_Check,*comm2D,&status);
                    // printf("Lv2 Station %d - its neighbour %d has %d available ports for refference\n", station_rank, lv2_neighbor_station[i], lv2_neighbor_available_port[i]);
                    

                }
            
            }
            for (int i=0; i<4; i++){
                // printf("\n\nStastion rank: %d Lv2 neighbor station %d has %d available ports\n", station_rank, lv2_neighbor_station[i], lv2_neighbor_available_port[i]);
            }
            MPI_Send(lv2_neighbor_station,4,MPI_INT,rank,MPI_Check_Neighbour,MPI_COMM_WORLD);
            MPI_Send(lv2_neighbor_available_port,4,MPI_INT,rank,MPI_Check_Neighbour,MPI_COMM_WORLD);
           
        }
        flag=0;
        flag2=0;
    
    }
    // printf("Neighbor thread is closed\n");
    return 0;
}
void *charging_port_thread(void* arg){
    
    int id=*(int*)arg;
    
    while (!end){
        srand(Seed+station_rank+id+time(NULL));
        charging_port[id]=rand()%2;
        sleep(1);

    }
    // printf("Charging port thread is closed\n");
    return 0;

}
