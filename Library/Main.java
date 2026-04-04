package library;

public class Main {
    public static void main(String[] args) {
        Library library = new Library();
        library.addBook(new Book(1, "1984", "George Orwell"));
        library.addBook(new Book(2, "Kuyucaklı Yusuf", "Sabahattin Ali"));
        library.listBooks();
        library.removeBook(1);
        System.out.println("After removing a book:");
        library.listBooks();
    }
}
