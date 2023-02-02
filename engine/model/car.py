from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self, last_service_date, current_mileage, last_service_mileage, indicator_warning, tyreSensorArray) -> None:
        self.last_service_date = last_service_date
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        self.indicator_warning = indicator_warning
        self.tyreSensorArray = tyreSensorArray
        self.engine = None
        self.battery = None
        self.tyre = None

        self.update_parts()

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service() or self.tyre.needs_service()

    @abstractmethod
    def update_parts(self):
        pass