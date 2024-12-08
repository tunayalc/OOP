package CarRent;

import java.util.ArrayList;
import java.util.List;

public class CarRental {
    private List<Vehicle> vehicles;

    public CarRental() {
        this.vehicles = new ArrayList<>();
    }

    public void addVehicle(Vehicle vehicle) {
        vehicles.add(vehicle);
    }

    public void removeVehicle(int vehicleId) {
        vehicles.removeIf(vehicle -> vehicle.getVehicleId() == vehicleId);
    }

    public void listVehicles() {
        for (Vehicle vehicle : vehicles) {
            System.out.println("ID: " + vehicle.getVehicleId() + ", Brand: " + vehicle.getBrand() + 
                ", Model: " + vehicle.getModel() + ", Price/Day: " + vehicle.getPricePerDay());
        }
    }
}
