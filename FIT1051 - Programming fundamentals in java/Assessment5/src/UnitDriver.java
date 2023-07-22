public class UnitDriver {
    public static void main(String[] args) {
//        //successful attempt
//        Unit theUnit=new Unit("FIT1051",6,"Faculty of IT");
//        theUnit.setOfferedThisSemester(true);
//        System.out.println(theUnit.toString());
//        System.out.println(theUnit.getUnitName());
//
//        //setting unit name for the unit
//        theUnit.setUnitName("Programming fundamentals in java");
//        System.out.println(theUnit.getUnitName());
//
//        //unsuccessful attempt
//        Unit unsuccessfulUnit=new Unit("FIT101010010101",-1,"FIT");
//        unsuccessfulUnit.setOfferedThisSemester(true);
//        System.out.println(unsuccessfulUnit.toString());
//
//        Unit unsuccessfulUnit2=new Unit("FIT2222",6,"Faculty of Information and Technology");
//        unsuccessfulUnit2.setOfferedThisSemester(true);
//        System.out.println(unsuccessfulUnit2.toString());
//        //resetting new unit in theUnit
//        theUnit.setUnitCode("FIT1008");
//        theUnit.setUnitName("Computer Science");
//        theUnit.setCreditHour(6);
//        theUnit.setOfferFaculty("Faculty of IT");
//        System.out.println(theUnit.toString());
//
//        //testing customCreditHour
//        theUnit.customCreditHour("FIT1999",6);
//        System.out.println(theUnit);
//        theUnit.customCreditHour("FIT1008",12);
//        //check if the custom credit is changed
//        theUnit.customCreditHour("MAT1830",12);
//        System.out.println(theUnit);
//        theUnit.customCreditHour("MAT1841",3);
//        System.out.println(theUnit);
        // creating Assessment 1
        Assessment A1=new Assessment();
        A1.setAssessmentName("Mid-Term Test");
        A1.setAssessmentValue(60);
        // creating Assessment 2
        Assessment A2=new Assessment();
        A2.setAssessmentName("Coding Task");
        A2.setAssessmentValue(40);
        // creating Assessment 3
        Assessment A3=new Assessment();
        A3.setAssessmentName("Final Exam");
        A3.setAssessmentValue(100);
        //Inserting assessment 1 into unit assessment
        UnitAssessment theUnitAssessment=new UnitAssessment("FIT1051",6,"Faculty Of Info Tech",A1);
        System.out.println(theUnitAssessment);
        //insert A2
        theUnitAssessment.addAssessment(A2);
        System.out.println(theUnitAssessment);
        //insert A3
        theUnitAssessment.addAssessment(A3);
        System.out.println(theUnitAssessment);



    }


}
