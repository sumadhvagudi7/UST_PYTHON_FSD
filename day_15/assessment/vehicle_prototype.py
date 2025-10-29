# ----------------------------------------
# Automated Vehicle Manufacturing System
# Using Factory + Builder Patterns
# ----------------------------------------

# ---------------------------
# Vehicle Base Class
# ---------------------------
class Vehicle:
    def __init__(self, vehicle_type, model):
        self.vehicle_type = vehicle_type
        self.model = model
        self.engine = None
        self.wheels = None
        self.color = None
        self.features = []

    def __str__(self):
        return (f"--- Vehicle Created ---\n"
                f"Type: {self.vehicle_type}\n"
                f"Model: {self.model}\n"
                f"Engine: {self.engine}\n"
                f"Wheels: {self.wheels}\n"
                f"Color: {self.color}\n"
                f"Features: {', '.join(self.features)}")


# ---------------------------
# Factory Pattern
# ---------------------------
class VehicleFactory:
    @staticmethod
    def create_vehicle(vehicle_type, model):
        vehicle_type = vehicle_type.lower()
        if vehicle_type == "car":
            return Vehicle("Car", model)
        elif vehicle_type == "bike":
            return Vehicle("Bike", model)
        elif vehicle_type == "truck":
            return Vehicle("Truck", model)
        else:
            raise ValueError("Unknown vehicle type!")


# ---------------------------
# Builder Base Class
# ---------------------------
class VehicleBuilder:
    def __init__(self, vehicle):
        self.vehicle = vehicle

    def set_engine(self):
        pass

    def set_wheels(self):
        pass

    def set_color(self):
        pass

    def set_features(self):
        pass

    def get_vehicle(self):
        return self.vehicle


# ---------------------------
# Concrete Builders
# ---------------------------
class CarBuilder(VehicleBuilder):
    def set_engine(self):
        if self.vehicle.model == "Sport":
            self.vehicle.engine = "V8 Turbo"
        elif self.vehicle.model == "Basic":
            self.vehicle.engine = "V4 Petrol"
        elif self.vehicle.model == "Luxury":
            self.vehicle.engine = "V8 Hybrid"
        return self

    def set_wheels(self):
        self.vehicle.wheels = "4 Alloy Wheels"
        return self

    def set_color(self):
        color_map = {"Sport": "Red", "Basic": "White", "Luxury": "Black Pearl"}
        self.vehicle.color = color_map.get(self.vehicle.model, "Silver")
        return self

    def set_features(self):
        feature_map = {
            "Sport": ["Sports Mode", "Leather Seats", "ABS"],
            "Basic": ["Manual AC", "Fabric Seats"],
            "Luxury": ["Panoramic Sunroof", "GPS", "Heated Seats"]
        }
        self.vehicle.features = feature_map.get(self.vehicle.model, [])
        return self


class BikeBuilder(VehicleBuilder):
    def set_engine(self):
        model = self.vehicle.model
        if model == "Basic":
            self.vehicle.engine = "150cc"
        elif model == "Sport":
            self.vehicle.engine = "300cc Racing Engine"
        elif model == "Luxury":
            self.vehicle.engine = "500cc Twin Cylinder"
        return self

    def set_wheels(self):
        self.vehicle.wheels = "2 Steel Wheels"
        return self

    def set_color(self):
        color_map = {"Basic": "Black", "Sport": "Red", "Luxury": "Matte Blue"}
        self.vehicle.color = color_map.get(self.vehicle.model, "Silver")
        return self

    def set_features(self):
        feature_map = {
            "Basic": ["Standard Brakes"],
            "Sport": ["ABS", "Digital Meter"],
            "Luxury": ["GPS", "Heated Grips", "Smart Lock"]
        }
        self.vehicle.features = feature_map.get(self.vehicle.model, [])
        return self


class TruckBuilder(VehicleBuilder):
    def set_engine(self):
        model = self.vehicle.model
        if model == "Basic":
            self.vehicle.engine = "V8 Diesel"
        elif model == "Sport":
            self.vehicle.engine = "V10 Turbo Diesel"
        elif model == "Luxury":
            self.vehicle.engine = "V12 Heavy Duty"
        return self

    def set_wheels(self):
        self.vehicle.wheels = "6 Off-Road Wheels"
        return self

    def set_color(self):
        color_map = {"Basic": "Grey", "Sport": "Black", "Luxury": "Metallic Blue"}
        self.vehicle.color = color_map.get(self.vehicle.model, "Silver")
        return self

    def set_features(self):
        feature_map = {
            "Basic": ["Standard Cabin"],
            "Sport": ["Reinforced Suspension", "Towing Assist"],
            "Luxury": ["GPS", "AC Cabin", "Trailer Assist"]
        }
        self.vehicle.features = feature_map.get(self.vehicle.model, [])
        return self


# ---------------------------
# Director Class
# ---------------------------
class VehicleDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct_vehicle(self):
        return (self.builder
                .set_engine()
                .set_wheels()
                .set_color()
                .set_features()
                .get_vehicle())


# ---------------------------
# Client Code
# ---------------------------
if __name__ == "__main__":
    # SPORT CAR
    car = VehicleFactory.create_vehicle("Car", "Sport")
    car_builder = CarBuilder(car)
    car_director = VehicleDirector(car_builder)
    sport_car = car_director.construct_vehicle()
    print(sport_car, "\n")

    # BASIC BIKE
    bike = VehicleFactory.create_vehicle("Bike", "Basic")
    bike_builder = BikeBuilder(bike)
    bike_director = VehicleDirector(bike_builder)
    basic_bike = bike_director.construct_vehicle()
    print(basic_bike, "\n")

    # LUXURY TRUCK
    truck = VehicleFactory.create_vehicle("Truck", "Luxury")
    truck_builder = TruckBuilder(truck)
    truck_director = VehicleDirector(truck_builder)
    luxury_truck = truck_director.construct_vehicle()
    print(luxury_truck)
