from abc import ABC, abstractmethod
from engine.model.calliope import  Calliope


class Car(ABC):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    @abstractmethod
    def needs_service(self):
        pass

"""
class Engine abstract
EngineA(Engine) EngineB(Engine)
class Battery asbtract
BatteryA(Battery) BatteryB(Battery)
class Car():
    def __init__(self, last_service_date, current_mileage, current_mileage, indicator):
        self.engine = EngineA(current_mileage, current_mileage, indicator)
        self.battery = BatteryA(last_service_date)
"""
