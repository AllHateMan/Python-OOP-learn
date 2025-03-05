class Car:
    def __init__(self, brand, model, year, mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.__mileage = mileage

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"

    @property
    def mileage(self):
        return self.__mileage

    def drive(self, km):
        self.__mileage += km

    def get_model(self):
        print(f"Модель авто: {self.model}")

    def display_info(self):
        print(f"Марка авто: {self.brand}| Модель авто: {self.model}| Рік випуску: {self.year}| Пробіг: {self.__mileage}")


class ElectricCar(Car):
    def __init__(self, brand, model, year, mileage, battery_capacity, battery_charge):
        super().__init__(brand, model, year, mileage)
        self.battery = Battery(battery_capacity, battery_charge)

    def display_info(self):
        super().display_info()
        print(f"Ємність аккумулятора: {self.battery.battery_capacity}kW | Заряд аккумулятора: {self.battery.battery_charge} %")


class Battery:
    def __init__(self, battery_capacity, battery_charge):
        self.battery_capacity = battery_capacity
        self.battery_charge = battery_charge

    def charge(self, charge_procent):
        new_charge = self.battery_charge + charge_procent
        if new_charge > 100:
            new_charge = 100
        elif new_charge < 0:
            new_charge = 0
        self.battery_charge = new_charge
        return self.battery_charge

    def info(self):
        print(f"Заряд аккумулятора: {self.battery_charge}%")

Acar = Car("Audi", "A4", 2004, 200030)
Bcar = Car("Mercedes-Benz", "A-Class", 2004, 123000)
Ccar = Car("Volkswagen", "Polo", 2002, 145003)

Ecar = ElectricCar("Nissan", "Leaf", 2012, 155000, 177, 55)

Ecar.display_info()
Ecar.battery.charge(25)
Ecar.battery.info()
print(Bcar)



