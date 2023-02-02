from datetime import datetime
from engine.model.car import Car

# Importing appropriate engine, battery
from engine.engines import CapuletEngine
from engine.batteries import NubbinBattery


class Thovex(Car):
    def __init__(self, last_service_date, current_mileage, last_service_mileage, indicator_warning) -> None:
        super().__init__(last_service_date, current_mileage, last_service_mileage, indicator_warning)

    def update_parts(self):
        self.engine = CapuletEngine(self.current_mileage, self.last_service_mileage, self.indicator_warning)
        self.battery = NubbinBattery(self.last_service_date)
