import java.util.ArrayList;
public class UnitAssessment extends Unit{


    public ArrayList<Assessment> assessmentList;
    public Assessment typeOfAssessment;
    public UnitAssessment(String init_UnitCode, int init_creditHour, String init_offerFaculty, Assessment initOfAssessment){
        super(init_UnitCode,init_creditHour,init_offerFaculty);
        typeOfAssessment=initOfAssessment;
        assessmentList=new ArrayList<Assessment>();
        assessmentList.add(typeOfAssessment);
    }

    public boolean addAssessment(Assessment newAssessment){
        if (assessmentList.size()<=10) {
            assessmentList.add(newAssessment);
            return true;
        }
        return false;


    }

    @Override
    public String toString() {
        return
                super.toString()+
                "typeOfAssessment= " + assessmentList
                ;
    }

}
