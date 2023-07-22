public class Assessment {
    private String assessmentName;
    private int assessmentValue;

    public String getAssessmentName() {
        return assessmentName;
    }

    public int getAssessmentValue() {
        return assessmentValue;
    }

    public boolean setAssessmentName(String assessmentName) {
        boolean flag=false;
        if (assessmentName.length()<=20) {
            this.assessmentName = assessmentName;
            flag=true;}
            return flag;
    }

    public boolean setAssessmentValue(int assessmentValue) {
        boolean flag=false;
        if(assessmentValue>=0&&assessmentValue<=100) {
            this.assessmentValue = assessmentValue;
            flag=true;}
            return flag;
    }

    @Override
    public String toString() {
        return
                "assessmentName: " + getAssessmentName()  +
                ", assessmentValue:" + getAssessmentValue()+"\n" ;

    }
}
