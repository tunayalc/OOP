package SchoolManagement;

public class Student {
    private int studentId;
    private String name;
    private String grade;

    public Student(int studentId, String name, String grade) {
        this.studentId = studentId;
        this.name = name;
        this.grade = grade;
    }

    public int getStudentId() {
        return studentId;
    }

    public String getName() {
        return name;
    }

    public String getGrade() {
        return grade;
    }
}
