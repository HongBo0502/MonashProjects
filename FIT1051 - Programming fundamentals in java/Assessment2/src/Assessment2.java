/*
 * Assessment 2
 *
 * Copyright (c) 2022  Monash University
 *
 * Written by  Jonny Low
 *
 *
 */
import java.util.Scanner;
public class Assessment2 {
    public static void main(String[] args){

        Assessment2 a2 = new Assessment2();

        // Instruction: To run your respective task, uncomment below individually
//        a2.task1();
//        a2.task2();
//        a2.task3();
//        a2.task4();

//        test your task 5 here
        System.out.println(a2.pythagorasTheorem(4,5));
    }

    private void task1() {
        // code your task 1 here
        int n ;
        boolean intTest;
        n=0;
        intTest = (n >= 1 && n < 40) || (n % 2 != 0 && n >= 40 && n <= 50) || (n > 50 && n <= 100);
        System.out.println("n:" + n + " expect false get " + intTest);
        n=1;
        intTest = (n >= 1 && n < 40) || (n % 2 != 0 && n >= 40 && n <= 50) || (n > 50 && n <= 100);
        System.out.println("n:" + n + " expect true get " + intTest);
        n=2;
        intTest = (n >= 1 && n < 40) || (n % 2 != 0 && n >= 40 && n <= 50) || (n > 50 && n <= 100);
        System.out.println("n:" + n + " expect true get " + intTest);
        n=39;
        intTest = (n >= 1 && n < 40) || (n % 2 != 0 && n >= 40 && n <= 50) || (n > 50 && n <= 100);
        System.out.println("n:" + n + " expect true get " + intTest);
        n=40;
        intTest = (n >= 1 && n < 40) || (n % 2 != 0 && n >= 40 && n <= 50) || (n > 50 && n <= 100);
        System.out.println("n:" + n + " expect false get " + intTest);
        n=41;
        intTest = (n >= 1 && n < 40) || (n % 2 != 0 && n >= 40 && n <= 50) || (n > 50 && n <= 100);
        System.out.println("n:" + n + " expect true get " + intTest);
        n=42;
        intTest = (n >= 1 && n < 40) || (n % 2 != 0 && n >= 40 && n <= 50) || (n > 50 && n <= 100);
        System.out.println("n:" + n + " expect false get " + intTest);
        n=49;
        intTest = (n >= 1 && n < 40) || (n % 2 != 0 && n >= 40 && n <= 50) || (n > 50 && n <= 100);
        System.out.println("n:" + n + " expect true get " + intTest);
        n=50;
        intTest = (n >= 1 && n < 40) || (n % 2 != 0 && n >= 40 && n <= 50) || (n > 50 && n <= 100);
        System.out.println("n:" + n + " expect false get " + intTest);
        n=51;
        intTest = (n >= 1 && n < 40) || (n % 2 != 0 && n >= 40 && n <= 50) || (n > 50 && n <= 100);
        System.out.println("n:" + n + " expect true get " + intTest);
        n=99;
        intTest = (n >= 1 && n < 40) || (n % 2 != 0 && n >= 40 && n <= 50) || (n > 50 && n <= 100);
        System.out.println("n:" + n + " expect true get " + intTest);
        n=100;
        intTest = (n >= 1 && n < 40) || (n % 2 != 0 && n >= 40 && n <= 50) || (n > 50 && n <= 100);
        System.out.println("n:" + n + " expect true get " + intTest);
        n=101;
        intTest = (n >= 1 && n < 40) || (n % 2 != 0 && n >= 40 && n <= 50) || (n > 50 && n <= 100);
        System.out.println("n:" + n + " expect false get " + intTest);
        n=-100;
        intTest = (n >= 1 && n < 40) || (n % 2 != 0 && n >= 40 && n <= 50) || (n > 50 && n <= 100);
        System.out.println("n:" + n + " expect false get " + intTest);
        n=400;
        intTest = (n >= 1 && n < 40) || (n % 2 != 0 && n >= 40 && n <= 50) || (n > 50 && n <= 100);
        System.out.println("n:" + n + " expect false get " + intTest);
    }
    private void task2(){
        // code your task 2 here
        boolean theTrue=true;
        boolean theFalse=false;
        boolean theTemp;
        System.out.println(theTrue);
        System.out.println(theFalse);
        theTemp=theTrue;
        theTrue=theFalse;
        theFalse=theTemp;
        System.out.println(theTrue);
        System.out.println(theFalse);
    }

    private void task3(){
        // code your task 3 here
    final double BUILDING_HEIGHT=20.00;
    final double ANGLE_ALPHA=53.13;
    final double ANGLE_BETA=41.00;
    final int AREA_STONE_STAB=1;
    double lengthAlpha;
    double lengthBeta;
    int areaBetweenBuilding;
    lengthAlpha=BUILDING_HEIGHT/Math.tan(ANGLE_ALPHA*Math.PI/180);//finding the length between the building A and B
    lengthBeta=BUILDING_HEIGHT/Math.tan(ANGLE_BETA*Math.PI/180);//finding the length of the building A
    areaBetweenBuilding= (int)(Math.ceil(lengthAlpha*lengthBeta));
        System.out.println(areaBetweenBuilding);
    }

    private void task4(){
        // code your task 4 here
        int x;
        int y;
        int bitwiseAnd;
        int bitwiseXOR;
        Scanner inputX= new Scanner(System.in);
        System.out.println("Enter value x: ");
        x=inputX.nextInt();
        System.out.println("Enter value y: ");
        Scanner inputY= new Scanner(System.in);
        y=inputY.nextInt();
        bitwiseAnd=x&y;
        bitwiseXOR=x^y;
        System.out.println("The bitwise and of x and y: "+bitwiseAnd);
        System.out.println("The bitwise exclusive or of x and y: "+bitwiseXOR);


    }

    // Code your task 5 method here
    private double pythagorasTheorem(double a, double b){
            double c;
            c=Math.sqrt(a*a+b*b);
            return c;

    }
}

