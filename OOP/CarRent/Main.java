package CarRent;

public class Main {
    public static void main(String[] args) {
        CarRental rental = new CarRental();
        rental.addVehicle(new Vehicle(1, "Toyota", "Corolla", 50.0));
        rental.addVehicle(new Vehicle(2, "BMW", "X5", 150.0));
        rental.listVehicles();
        rental.removeVehicle(1);
        System.out.println("After removing a vehicle:");
        rental.listVehicles();
    }
}
