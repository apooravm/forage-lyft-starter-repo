from datetime import datetime
from engine.model.car import Car

# Importing appropriate engine, battery, tyre
from engine.engines import WilloughbyEngine
from engine.batteries import SpindlerBattery
from engine.tyres import CarriganTyre

class Glissade(Car):
    def __init__(self, last_service_date, current_mileage, last_service_mileage, indicator_warning, tyreSensorArray) -> None:
        super().__init__(last_service_date, current_mileage, last_service_mileage, indicator_warning, tyreSensorArray)

    def update_parts(self):
        self.engine = WilloughbyEngine(self.current_mileage, self.last_service_mileage, self.indicator_warning)
        self.battery = SpindlerBattery(self.last_service_date)
        self.tyre = CarriganTyre(self.tyreSensorArray)
