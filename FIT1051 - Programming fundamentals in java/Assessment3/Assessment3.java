/*
 * Assessment 3
 *
 * Copyright (c) 2022  Monash University
 *
 * Written by  Jonny Low
 *
 *
 */
import org.w3c.dom.ls.LSOutput;

import java.util.Arrays;
import java.util.ArrayList;
public class Assessment3 {

    public static void main(String[] args){

        Assessment3 a3 = new Assessment3();

        // Instruction: To run your respective task, uncomment below individually
//        a3.task1a();
//        a3.task2();
//        a3.task3();
//        a3.gradeScale("80");
//        a3.daysOfTheWeek("2");
//        a3.task6();
        a3.task7();

    }


    private void task1a(){
        // code your task 1a (calling method) here
        double[] array={1.23,1.34,2.45,6.32,12.09};
        System.out.println("Value Type:" + array[0]);
        System.out.println("Reference Type:"+ Arrays.toString(array));
        task1b(array,array[0]);
        System.out.println("Value Type:" + array[0]); // the value type doesn't change
        System.out.println("Reference Type:"+ Arrays.toString(array)); // the value in the array was incremented

    }

    private void task1b(double[] a, double b){
        // code your task1b (called method) here
        a[1]++; // the called method increment the second value of array
        b++;// the called method will increment the value of the double
    }

    private void task2(){
        // code your task 2 here
        String result = String.format("%4d\n"+"%4d\n"+"%4d\n"+"%4d\n",1,10,100,1000);
        // the %4 will add 4 spaces then the value will be inserted to the right most spaces and so on
        System.out.println(result);
    }

    private void task3(){
        // code your task 3 here
        ArrayList<String> myList=new ArrayList<>(10);

        myList.add("one");
        myList.add("seven");
        myList.add("five");
        myList.add("three");
        myList.add("eight");
        myList.add("ten");

        myList.add(3,"eleven");

        System.out.println(myList);

        myList.remove(5);

        System.out.println(myList.contains("seven"));

    }

    // code your task 4 here. You should create your own method shell.
    private String gradeScale(String mark){
        int a=Integer.parseInt(mark);
        String result_Grade;
        if (a>100){
            result_Grade = "Out of bound";}
        else if (a>=80&&a<=100) {
            result_Grade = "High Distinction";}
        else if (a>=70){
            result_Grade="Distinction";
        }
        else if (a>=60){
            result_Grade="Credit";
        }
        else if (a>=50){
            result_Grade="Pass";
        }
        else if (a>=0){
            result_Grade="Fail";
        }
        else{
            result_Grade="Out of bound.";
        }
        System.out.println(result_Grade);
        return result_Grade;
    }

    // code your task 5 here. You should create your own method shell.
    private String daysOfTheWeek(String day){
        String theDay;
        switch(day){
            case "1":
                theDay="Monday";
                break;
            case "2":
                theDay="Tuesday";
                break;
            case "3":
                theDay="Wednesday";
                break;
            case "4":
                theDay="Thursday";
                break;
            case "5":
                theDay="Friday";
                break;
            case "6":
                theDay="Saturday";
                break;
            case "7":
                theDay="Sunday";
                break;
            default:
                theDay="The day is not within range.";
            }
        System.out.println(theDay);
        return theDay;
        }


    private void task6(){
        // code your task 6 here
        int radiusOf_Circle=1;// initialize the radius to 1 since the value will start from 1
        double areaOf_Circle=Math.PI * radiusOf_Circle*radiusOf_Circle;//calculate the area of the circle
        double circumferenceOf_Circle=2*Math.PI*radiusOf_Circle;// calculate the circumference of the circle
        double ratioOf_AC=areaOf_Circle/circumferenceOf_Circle;// calculate the ratio of area and the circumference
        while (ratioOf_AC<30){
            System.out.println(ratioOf_AC);
            radiusOf_Circle+=1;
            areaOf_Circle=Math.PI * radiusOf_Circle*radiusOf_Circle;
            circumferenceOf_Circle=2*Math.PI*radiusOf_Circle;
            ratioOf_AC=areaOf_Circle/circumferenceOf_Circle;

        }
    }


    private void task7() {
        // code your task 7 here
        int size = 10;
        String Output = "";
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                if (i == j) {
                    Output += "*";
                } else if (i + j == size - 1) {
                    Output += "*";
                } else {
                    Output += " ";
                }

            }
            Output+="\n";
        }
        System.out.println(Output);
    }
}