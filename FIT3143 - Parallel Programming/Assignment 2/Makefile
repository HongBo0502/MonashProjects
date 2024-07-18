ALL: a2

a2: a2.c
	mpicc -Wall a2.c -o a2 -lpthread -lm

run:
	mpirun -np 5 ./a2 2 2 

run1:
	mpirun -np 7 ./a2 2 3
clean :
	/bin/rm -f ./a2
	
	