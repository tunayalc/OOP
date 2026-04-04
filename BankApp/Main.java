package BankApp;

public class Main {
    public static void main(String[] args) {
        BankAccount account = new BankAccount(1, "John Doe", 1000.0);
        account.deposit(500);
        System.out.println("Balance after deposit: " + account.getBalance());
        account.withdraw(200);
        System.out.println("Balance after withdrawal: " + account.getBalance());
        account.withdraw(1500);
    }
}
