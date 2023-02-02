from abc import ABC, abstractmethod

class ITyre(ABC):
    def __init__(self, tyreSensorArray):
        self.tyreSensorArray = tyreSensorArray

    @abstractmethod
    def needs_service(self): pass

class CarriganTyre(ITyre):
    def __init__(self, tyreSensorArray):
        super().__init__(tyreSensorArray)

    def needs_service(self):
        for x in self.tyreSensorArray:
            if x >= 0.9:
                return True

        return False

class Octoprime(ITyre):
    def __init__(self, tyreSensorArray):
        super().__init__(tyreSensorArray)

    def needs_service(self):
        return (sum(self.tyreSensorArray) >= 3)