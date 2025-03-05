from abc import ABC, abstractmethod


class Car(ABC):

    @abstractmethod
    def drive(self):
        pass

    @property
    @abstractmethod
    def max_speed(self):
        pass

class Diesel(ABC):

    @property
    @abstractmethod
    def tank_capacity(self):
        pass

    @property
    @abstractmethod
    def diesel(self):
        pass


class Electro(ABC):

    @property
    @abstractmethod
    def acc_capacity(self):
        pass

    @property
    @abstractmethod
    def kw(self):
        pass


class DieselAuto(Car, Diesel):
    def __init__(self, max_speed, tank_capacity, diesel):
        self._max_speed = max_speed
        self._tank_capacity = tank_capacity
        self._diesel = diesel

    @property
    def max_speed(self):
        return self._max_speed

    @property
    def tank_capacity(self):
        return self._tank_capacity

    @property
    def diesel(self):
        return self._diesel

    def drive(self):
        print(
            f"Ємність баку: {self.tank_capacity}л, Остаток палива: {self.diesel}л, Максимальна швидкість: {self.max_speed}км/год"
        )


class ElectroCar(Car, Electro):

    def __init__(self, max_speed, acc_capacity, kw):
        self._max_speed = max_speed
        self._acc_capacity = acc_capacity
        self._kw = kw

    @property
    def max_speed(self):
        return self._max_speed

    @property
    def acc_capacity(self):
        return self._acc_capacity

    @property
    def kw(self):
        return self._kw
    def drive(self):
        print(
            f"Ємність аккумулятора: {self.acc_capacity}kW, Заряд аккумулятора: {self.kw}kW, Максимальна швидкість: {self.max_speed}км/год"
        )


audi = DieselAuto(180, 65, 40)
tesla = ElectroCar(200, 170, 140)
audi.drive()
tesla.drive()