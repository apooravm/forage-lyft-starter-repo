from abc import ABC, abstractmethod
from datetime import datetime

# Batteries
class Battery(ABC):
    def __init__(self, last_service_date) -> None:
        self.last_service_date = last_service_date

    @abstractmethod
    def needs_service(self):
        pass


class SpindlerBattery(Battery):
    def __init__(self, last_service_date) -> None:
        super().__init__(last_service_date)

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if service_threshold_date < datetime.today().date():
            return True
        else:
            return False

class NubbinBattery(Battery):
    def __init__(self, last_service_date) -> None:
        super().__init__(last_service_date)

    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if service_threshold_date < datetime.today().date():
            return True
        else:
            return False