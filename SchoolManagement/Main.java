package SchoolManagement;

public class Main {
    public static void main(String[] args) {
        School school = new School();
        school.addStudent(new Student(1, "Alice", "A"));
        school.addTeacher(new Teacher(1, "Mr. Smith", "Mathematics"));
        school.listStudents();
        school.listTeachers();
    }
}
