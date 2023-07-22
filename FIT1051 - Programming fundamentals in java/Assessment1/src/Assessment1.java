/*
 * Week 03 Assessment Solution (3%)
 *
 * Copyright (c) 2022  Monash University
 *
 * Written by  Jonny Low
 *
 *
 */

public class Assessment1 {

    public static void main(String[] args){

        Assessment1 a1 = new Assessment1();

        // Instruction: To run your respective task, uncomment below individually
//        a1.task1();
//        a1.task2();
//        a1.task3();
//        a1.task4();
//        a1.task5();

    }

    private void task1(){
        // code your task 1 here
        System.out.println(5); //print 5
        System.out.println(8); //print 8
        System.out.println(4); //print 4
        System.out.println(2); //print 2
        System.out.println(5+8+4+2); //print the sum of 5+8+4+2
        // setting the variable
        int a=5;
        int b=8;
        int c=4;
        int d=2;
        int e=a+b+c+d;
        //printing
        System.out.println(a);
        System.out.println(b);
        System.out.println(c);
        System.out.println(d);
        System.out.println(e);
        //setting the 2 variable
        int num=5;
        int sum=0;
        System.out.println(num);
        sum+=num;// adding the number in num into sum
        num=8;//resetting the number to the next number
        System.out.println(num);//printing the new num
        sum+=num;
        num=4;
        System.out.println(num);
        sum+=num;
        num=2;
        System.out.println(num);
        sum+=num;
        System.out.println(sum);
    }

    private void task2(){
        // code your task 2 here
        //setting variables
        int joggingspd=4;
        String lecturer= "Lim Mei Kuan";
        int capacity=50;
        int lendesk=90;
        String lightstate= "On";
        int numbook=200;
        int amtvacperperson=3;
        int currenttemp=27;
        int numofA=4;
        int memsize=1024;
        String tfstate="RED";
        //printing the string and concatenate the variables and units.
        System.out.println("Your jogging speed in miles per hour (mph):"+joggingspd+"mph");
        System.out.println("FIT1051 lecturer allocated to a workshop:"+ lecturer);
        System.out.println("The capacity of passengers in a train wagon:"+ capacity+" person");
        System.out.println("The length of a desk in millimetres:"+ lendesk+"cm");
        System.out.println("The state of a light switch:"+ lightstate);
        System.out.println("The number of book on a library shelf:"+ numbook);
        System.out.println("The amount of COVID vaccination a person can have so far:"+ amtvacperperson);
        System.out.println("The current temperature of the day:" + currenttemp +" celsius");
        System.out.println("The number of Ace in a deck of cards:"+ numofA);
        System.out.println("The memory size of a computer chip:"+ memsize+"mb");
        System.out.println("The state of a traffic light: "+tfstate);
    }

    private void task3(){
        // code your task 3 here
        float A=1.11f;
        int B=2;
        String C="Hi";
        double D=1.22;
        boolean E=true;

        float A1=B;
//        float A2=C;
        float A3=(float)D;
//        float A4=E;

//        int B1a=A;
        int B1b=(int)A;
//        int B2="Hi";
//        int B3a=D;
        int B3b=(int)D;
//        int B4=true;

//        String C1=1.11f;
//        String C2=2;
//        String C3=1.22;
//        String C4=true;

        double D1=1.11f;
        double D2=2;
//        double D3="Hi";
//        double D4=true;

//        boolean E1=1.11f;
//        boolean E2=2;
//        boolean E3="Hi";
//        boolean E4=1.22;

//     1. Integer to Float, Float to double, Integer to double, this three conversion will perform
//        automatically by Java
//     2. Java can cast double to float, double and float to integer which is narrowing conversion. The sides
//        effect which will cause the decimal will be taken away and the total space of the number will be decreased.


    }

    private void task4(){
        // code your task 4 here
        String line="           @@@@@@@@@@@@@@@@@@@@@@@         \n";
        String line2="        @@@@@@@@@@@@@@@@@@@@@@@@@@@@       \n";
        String line3="     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    \n";
        String line4="   @@@@@@@      @@@@@@@@@@@@     @@@@@@@   \n";
        String line5="  @@@@@@@        @@@@@@@@@@       @@@@@@@@ \n";
        String line6="@@@@@@@@@@      @@@@@@@@@@@      @@@@@@@@@@\n";
        String line7="@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n";
        String line8="  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ \n";
        String line9="   @@@@@@@@@@   @@@@@@@@@@@   @@@@@@@@@@   \n";
        String line10="    @@@@@@@@@@  @@@@@@@@@@@  @@@@@@@@@@    \n";
        String line11="     @@@@@@@@@@             @@@@@@@@@@     \n";
        String line12="       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@       \n";
        String line13="          @@@@@@@@@@@@@@@@@@@@@@@          \n";
        String line14="            @@@@@@@@@@@@@@@@@@@            \n";
        System.out.println(line+line2+line3+line4+line5+line6+line7+line8+line9+line10+line11+line12+line13+line14);

    }

    private void task5(){
        // code your task 5 here
        String s=null;
//        System.out.println(s.length());
//        the error id is NullPointerException
//        When calling the method that need an object, the variable that save null will cause the NullPointerException error
    }

}