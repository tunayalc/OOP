package SchoolManagement;

import java.util.ArrayList;
import java.util.List;

public class School {
    private List<Student> students;
    private List<Teacher> teachers;

    public School() {
        this.students = new ArrayList<>();
        this.teachers = new ArrayList<>();
    }

    public void addStudent(Student student) {
        students.add(student);
    }

    public void addTeacher(Teacher teacher) {
        teachers.add(teacher);
    }

    public void listStudents() {
        for (Student student : students) {
            System.out.println("ID: " + student.getStudentId() + ", Name: " + student.getName() + ", Grade: " + student.getGrade());
        }
    }

    public void listTeachers() {
        for (Teacher teacher : teachers) {
            System.out.println("ID: " + teacher.getTeacherId() + ", Name: " + teacher.getName() + ", Subject: " + teacher.getSubject());
        }
    }
}
