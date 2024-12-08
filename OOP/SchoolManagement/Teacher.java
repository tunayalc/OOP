package SchoolManagement;

public class Teacher {
    private int teacherId;
    private String name;
    private String subject;

    public Teacher(int teacherId, String name, String subject) {
        this.teacherId = teacherId;
        this.name = name;
        this.subject = subject;
    }

    public int getTeacherId() {
        return teacherId;
    }

    public String getName() {
        return name;
    }

    public String getSubject() {
        return subject;
    }
}
