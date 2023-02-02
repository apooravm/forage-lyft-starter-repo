from abc import ABC, abstractmethod

class Engine(ABC):
    def __init__(self, current_mileage, last_service_mileage, indicator_warning) -> None:
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        self.indicator_warning = indicator_warning

    @abstractmethod
    def needs_service(self):
        pass

class CapuletEngine(Engine):
    def __init__(self, current_mileage, last_service_mileage, indicator_warning) -> None:
        super().__init__(current_mileage, last_service_mileage, indicator_warning)

    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > 30000

class WilloughbyEngine(Engine):
    def __init__(self, current_mileage, last_service_mileage, indicator_warning) -> None:
        super().__init__(current_mileage, last_service_mileage, indicator_warning)

    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > 60000

class SternmanEngine(Engine):
    def __init__(self, current_mileage, last_service_mileage, indicator_warning) -> None:
        super().__init__(current_mileage, last_service_mileage, indicator_warning)

    def needs_service(self):
        return self.indicator_warning