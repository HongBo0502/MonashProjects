ALL: A1_Serial A1_Parallel A1_Parallel2

A1_Serial: A1.c
	gcc -Wall A1.c -o A1

A1_Parallel: A1_parallel.c 
	gcc -Wall A1_parallel.c -o A1_p -fopenmp

A1_Parallel2: A1_parallel2.c
	gcc -Wall A1_parallel2.c -o A1_p2 -fopenmp

run:
	./A1
	./A1_p
	./A1_p2
clean :
	/bin/rm -f ./A1 *.o
	/bin/rm -f ./A1_p *.o
	/bin/rm -f ./A1_p2 *.o