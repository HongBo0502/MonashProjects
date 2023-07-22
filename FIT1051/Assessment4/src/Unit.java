public class Unit {

    // Task 1: Instance Variables
    private String unitCode;
    private String unitName;
    private int creditHour ;
    private String offerFaculty;
    private boolean offeredThisSemester;

    // Task 2: constructors
    public Unit(String init_unicode, int init_creditHour, String init_offerFaculty) {

        setUnitCode(init_unicode);
        setCreditHour(init_creditHour);
        setOfferFaculty(init_offerFaculty);
        offeredThisSemester = false;
        unitName = "Not yet set";
    }

    // Task 3: Getter
    public String getUnitCode() {
        return unitCode;
    }

    public String getUnitName() {
        return unitName;

    }

    public int getCreditHour() {
        return creditHour;

    }

    public String getOfferFaculty() {
        return offerFaculty;
    }

    public boolean getOfferedThisSemester() {
        return offeredThisSemester;
    }

    // Task 4: Setter
    public void setUnitCode(String newUnitCode) {
        if (newUnitCode.length()==7)
            unitCode = newUnitCode;
    }

    public void setUnitName(String newUnitName) {
        if(newUnitName.length()<=40)
            unitName = newUnitName;
    }

    public void setCreditHour(int newCreditHour) {
        if(newCreditHour>0)
        creditHour = newCreditHour;
    }

    public void setOfferFaculty(String newOfferFaculty) {
        if(newOfferFaculty.length()<=20)
            offerFaculty = newOfferFaculty;
    }

    public void setOfferedThisSemester(boolean newOfferedThisSemester) {
        offeredThisSemester = newOfferedThisSemester;
    }

    // Task 5: toString method
    public String toString() {
        String outString;
        String prompt;
        if (unitCode==null || creditHour==0 || offerFaculty==null){
            setOfferedThisSemester(false);
            prompt="=======Unsuccessful Attempt=======\n";
        }
        else
            prompt="=======Successful Attempt=======\n";
        outString = "Unit Code: " + unitCode + "\nOffered Faculty: " + offerFaculty + "\nCreditHour: " + creditHour + "\nOffered in this Semester? : " + offeredThisSemester+"\n";
        return prompt+outString;
    }

    // Task 6: customCreditHour method
    public void customCreditHour(String custUnitCode,int custCreditHour) {
        String ErrorStr="Error. This is FIT unit and the no of credit hours is 6 by default";
        if (custUnitCode.charAt(0)=='F' && custUnitCode.charAt(1)=='I'&&custUnitCode.charAt(2)=='T'&&custCreditHour!=6){

            System.out.println(ErrorStr);
        }
        else{
            setUnitCode(custUnitCode);
            setCreditHour(custCreditHour);
        }

    }
}
