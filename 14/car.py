class CarInfo:

    def __init__(self, car_name, color, hp, car_doors):

        self.car_name = car_name
        self.color = color
        self.hp = hp
        self.car_doors = car_doors
        self.car_on = False
    
    def turn_on_car(self):

        if self.car_on:
            print(f"car is already on")
        else: 
            print(f"starting the car {self.car_name}")
            self.car_on = True
            
    def turn_off_car(self):

        if self.car_on:
            print(f"turning off the car {self.car_name}")
            self.car_on = False
        else:
            print(f"car is already off")
    
    def verify_status_car(self):

        if self.car_on:
            status = "ON"
        else:
            status = "OFF"
        print(f"car status: {status}")

        return status
            
if __name__ == "__main__":
    
    car = CarInfo("Ferrari", "red", 579, "two")

    print(f"Car info: {car.car_name} {car.color} {car.hp} {car.car_doors}")

    car.verify_status_car()
    car.turn_on_car()
    car.turn_off_car()
    car.verify_status_car()